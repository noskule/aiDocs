#!/usr/bin/env python3
"""Structural documentation checks for aiDocs-based projects (issue #33).

Single entry point, stdlib only. Exit 1 on errors, 0 otherwise (warnings
don't fail the build). Runs identically in a consuming project and in the
aiDocs standard repo: standardized per-project filenames that only exist
after /setup are reported as warnings, never errors.

Usage: python docs/tools/check-docs.py [--root <repo-root>]
"""

import argparse
import re
import sys
from pathlib import Path

# Standardized per-project names: created by /setup, so a dangling link to
# them is a warning (missing setup step), not a broken link.
PER_PROJECT = {
    "installation.md", "development.md", "testing.md", "release.md",
    "changelog.md", "coding-guidelines.md", "architecture-rules.md",
    "issue-tracker.md", "wiki.md", "design-sync.md", "project-index.md",
    "tools/jobs.md",
    # placeholder rows shipped in subagents/index.md
    "subagents/example-agent.md", "subagents/test-runner.md",
    "subagents/test-recommender.md", "subagents/documentation.md",
}

# Entry points and registries are never orphans.
NON_ORPHANS = {"INDEX.md", "AGENTS.md", "README.md", "project-index.md",
               "subagents/index.md"}

SKIP_DIRS = {".venv", "venv", "__pycache__", "node_modules", "site-packages"}


def md_files(base: Path):
    for md in base.rglob("*.md"):
        if not SKIP_DIRS & set(md.parts):
            yield md

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
WRAPPER_REF_RE = re.compile(r"docs/subagents/([\w.-]+\.md)")

errors, warnings = [], []


def error(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def exists_cased(path: Path) -> bool:
    """True if path exists with exactly this casing (NTFS hides case bugs
    that break on Linux CI)."""
    if not path.exists():
        return False
    cur = path
    while cur != cur.parent:
        if cur.name not in [p.name for p in cur.parent.iterdir()]:
            return False
        cur = cur.parent
    return True


def rel(root: Path, p: Path) -> str:
    return p.relative_to(root).as_posix()


def check_links(root: Path, docs: Path):
    """Every relative markdown link resolves, with exact casing."""
    linked = set()
    for md in md_files(docs):
        in_fence = False
        for lineno, line in enumerate(
                md.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
            if in_fence:
                continue
            for target in LINK_RE.findall(line):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = target.split("#")[0]
                if not target:
                    continue
                dest = (md.parent / target).resolve()
                where = f"{rel(root, md)}:{lineno}"
                if not dest.is_relative_to(root):
                    continue  # outside the repo (e.g. ../../wiki GitHub URL)
                try:
                    dest_rel = rel(docs, dest)
                except ValueError:
                    dest_rel = None  # points outside docs/ (e.g. ../SECURITY.md)
                if dest.exists():
                    if not exists_cased(dest):
                        error(f"{where}: link '{target}' differs in casing "
                              f"from the file on disk")
                    if dest_rel:
                        linked.add(dest_rel)
                elif dest_rel in PER_PROJECT:
                    warn(f"{where}: '{target}' not created yet "
                         f"(standardized per-project file - run /setup)")
                else:
                    error(f"{where}: broken link '{target}'")
    return linked


def check_orphans(docs: Path, linked: set):
    """Every docs page is reachable from some other page."""
    for md in md_files(docs):
        r = md.relative_to(docs).as_posix()
        if r in NON_ORPHANS or r in linked or ".template." in md.name:
            continue
        if r.startswith(("features/", "project/", "testing/")):
            continue  # collections, reached via their own conventions
        warn(f"docs/{r}: orphan - not linked from any other doc")


def check_bindings(root: Path, docs: Path):
    """Agent wrappers and subagent reference docs point at each other."""
    agents_dir = root / ".claude" / "agents"
    sub_dir = docs / "subagents"
    wrappers = {}
    if agents_dir.is_dir():
        for w in agents_dir.glob("*.md"):
            if ".template." in w.name or w.name.endswith(".template"):
                continue
            refs = WRAPPER_REF_RE.findall(w.read_text(encoding="utf-8", errors="replace"))
            wrappers[w.name] = refs
            for ref in refs:
                if not (sub_dir / ref).exists():
                    error(f".claude/agents/{w.name}: references missing "
                          f"docs/subagents/{ref}")
    if sub_dir.is_dir():
        wrapped = {r for refs in wrappers.values() for r in refs}
        for doc in sub_dir.glob("*.md"):
            if doc.name in ("index.md", "README.md"):
                continue
            if doc.name not in wrapped:
                warn(f"docs/subagents/{doc.name}: no .claude/agents/ wrapper "
                     f"(fine if skill-backed or invoked manually)")


def check_registration(root: Path, docs: Path):
    """Subagent docs and active skills are listed in subagents/index.md."""
    index = docs / "subagents" / "index.md"
    if not index.exists():
        error("docs/subagents/index.md missing")
        return
    text = index.read_text(encoding="utf-8", errors="replace")
    for doc in (docs / "subagents").glob("*.md"):
        if doc.name in ("index.md", "README.md"):
            continue
        if doc.name not in text:
            error(f"docs/subagents/{doc.name}: not listed in subagents/index.md")
    skills_dir = root / ".claude" / "skills"
    if skills_dir.is_dir():
        for skill in skills_dir.glob("*/SKILL.md"):
            if skill.parent.name not in text:
                warn(f".claude/skills/{skill.parent.name}: active skill not "
                     f"listed in subagents/index.md")


def check_template_copies(root: Path, docs: Path):
    """Templates are instantiate-and-delete: never next to their filled copy."""
    for area in (docs, root / ".claude"):
        if not area.is_dir():
            continue
        for tpl in area.rglob("*.template*"):
            filled = tpl.with_name(tpl.name.replace(".template", ""))
            if filled.exists():
                error(f"{rel(root, tpl)}: template coexists with its filled "
                      f"copy {filled.name} - delete the template "
                      f"(instantiate-and-delete)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="repo root (default: cwd)")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    docs = root / "docs"
    if not docs.is_dir():
        print(f"error: no docs/ under {root}", file=sys.stderr)
        return 1

    linked = check_links(root, docs)
    check_orphans(docs, linked)
    check_bindings(root, docs)
    check_registration(root, docs)
    check_template_copies(root, docs)

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\ncheck-docs: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
