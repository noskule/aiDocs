---
name: update-aidocs
description: Update this project's aiDocs standard files from the upstream aiDocs repository. Use when the user asks to update aiDocs or pull the latest standard.
argument-hint: "[git ref, default: upstream main HEAD]"
---

Pull upstream changes of the aiDocs standard into this project without touching anything the project owns.

## Ownership Contract

Every file classifies into exactly one of:

| Class | Files | On update |
|-------|-------|-----------|
| **Upstream-owned** | UPPERCASE `.md` in `docs/` (except `README.md`), `*.template.md` / `*.template`, `docs/subagents/*.md` (except `index.md`), `docs/tools/`, upstream-shipped files under `.claude/` | apply changes |
| **Project-owned** | Filled template copies (`coding-guidelines.md`, `architecture-rules.md`, ...), `docs/README.md`, `docs/project-index.md`, `docs/subagents/index.md`, project's own docs/skills/agents, `docs/.aidocs-version` | never touch |

## Procedure

1. **Read the stamp** — `docs/.aidocs-version` holds the adopted upstream commit and source URL:

   ```text
   commit: <full sha>
   source: https://github.com/noskule/aiDocs
   updated: YYYY-MM-DD
   ```

   No stamp? Ask the user for the approximate adoption point, or fall back to reviewing every upstream-owned file with a 2-way diff and per-file confirmation.

2. **Fetch upstream** — clone the source into a temp dir. Old ref = stamp commit; new ref = `$ARGUMENTS` or upstream main HEAD.

3. **Compute the delta** — `git diff --name-status <old>..<new>` in the clone. Classify each path by the ownership contract.

4. **Apply, with 3-way safety** — for each upstream-owned change:
   - Project copy identical to the OLD upstream version → apply silently (copy new file / delete removed file)
   - Project copy differs from the old upstream version → **conflict**: show the user both diffs (their local change, the upstream change), ask before touching
   - File doesn't exist locally → add it
   - **`.claude/` is strictly additive**: never overwrite an existing file that differs — always confirm first

5. **Notify on template drift** — when a `*.template.md` changed and the project has a filled copy, don't touch the copy; report the template's diff so the user can port relevant changes manually.

6. **Stamp and report** — write the new commit to `docs/.aidocs-version`, then summarize: updated / added / deleted / skipped (project-owned) / conflicts / template-drift notices. Recommend `/validate-docs`.

## Rules

- Never modify project-owned files, ever — not even formatting
- Deletions are proposals, not actions: confirm each one
- If the ownership class of a file is ambiguous, treat it as project-owned and report it
