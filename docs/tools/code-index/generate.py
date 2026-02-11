#!/usr/bin/env python3
"""CLI entry point for code-index generation.

Parses source files using tree-sitter, groups by package, and generates
a compact two-level markdown index for LLM orientation.

Usage:
    python generate.py --config aidocs.yaml
    python generate.py --src src/main/java --lang kotlin --out docs/code-index --module app --prefix com.example.myapp
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from generator import generate_module_index, generate_package_file, generate_root_index
from grouping import group_declarations
from languages.kotlin import KotlinAdapter


def get_adapter(language: str):
    """Get the language adapter for the given language."""
    if language == "kotlin":
        return KotlinAdapter()
    raise ValueError(f"Unsupported language: {language}")


def discover_files(source_dirs: list[Path], extension: str) -> list[Path]:
    """Discover all source files with the given extension."""
    files = []
    for src_dir in source_dirs:
        if not src_dir.exists():
            print(f"  Warning: source directory not found: {src_dir}", file=sys.stderr)
            continue
        files.extend(sorted(src_dir.rglob(f"*{extension}")))
    return files


def process_module(
    name: str,
    source_dirs: list[Path],
    prefix: str,
    language: str,
    output_dir: Path,
    merge_threshold: int,
    project_root: Path,
) -> dict | None:
    """Process a single module: discover, parse, group, generate.

    Returns module info dict for the root index, or None if no files found.
    """
    adapter = get_adapter(language)
    extension = adapter.file_extension()

    # Discover files
    files = discover_files(source_dirs, extension)
    if not files:
        print(f"  No {extension} files found in {source_dirs}")
        return None

    print(f"  Found {len(files)} {extension} files")

    # Parse all files
    all_declarations = []
    errors = 0
    for file_path in files:
        # Use first source dir as the root for relative paths
        src_root = source_dirs[0]
        try:
            decls = adapter.parse_file(file_path, src_root)
            all_declarations.extend(decls)
        except Exception as e:
            errors += 1
            print(f"  Error parsing {file_path}: {e}", file=sys.stderr)

    if errors:
        print(f"  {errors} files had parse errors")

    print(f"  Extracted {len(all_declarations)} top-level declarations")

    # Group by package
    groups = group_declarations(all_declarations, prefix, merge_threshold)
    print(f"  Grouped into {len(groups)} packages")

    # Count total declarations (top-level only)
    decl_count = sum(len(g.declarations) for g in groups)

    # Generate module index
    generate_module_index(name, groups, output_dir)

    # Generate per-package files
    for group in groups:
        generate_package_file(name, group, output_dir)

    return {
        "name": name,
        "groups": groups,
        "decl_count": decl_count,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate code index from source files",
    )
    parser.add_argument(
        "--config",
        type=Path,
        help="Path to aidocs.yaml config file",
    )
    parser.add_argument("--src", type=str, help="Source directory (comma-separated)")
    parser.add_argument("--lang", type=str, default="kotlin", help="Language (default: kotlin)")
    parser.add_argument("--out", type=Path, help="Output directory")
    parser.add_argument("--module", type=str, help="Module name")
    parser.add_argument("--prefix", type=str, help="Package prefix to strip")
    parser.add_argument("--merge-threshold", type=int, default=2, help="Merge depth threshold")

    args = parser.parse_args()

    # Determine project root (for resolving relative paths)
    if args.config:
        project_root = args.config.resolve().parent
    else:
        project_root = Path.cwd()

    modules_config = []

    if args.config:
        # Load from config file
        config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
        language = config.get("language", "kotlin")
        output_dir = project_root / config.get("output_dir", "docs/code-index")
        merge_threshold = config.get("merge_threshold", 2)

        for mod in config.get("modules", []):
            source_dirs = [project_root / d for d in mod["source_dirs"]]
            modules_config.append({
                "name": mod["name"],
                "source_dirs": source_dirs,
                "prefix": mod["prefix"],
                "language": language,
                "merge_threshold": merge_threshold,
            })
    else:
        # Use CLI args
        if not args.src or not args.module or not args.prefix:
            parser.error("--src, --module, and --prefix are required when not using --config")
        output_dir = args.out or (project_root / "docs/code-index")
        source_dirs = [project_root / d.strip() for d in args.src.split(",")]
        modules_config.append({
            "name": args.module,
            "source_dirs": source_dirs,
            "prefix": args.prefix,
            "language": args.lang,
            "merge_threshold": args.merge_threshold,
        })

    # Process each module
    module_results = []
    for mod_config in modules_config:
        name = mod_config["name"]
        print(f"Processing module: {name}")
        result = process_module(
            name=name,
            source_dirs=mod_config["source_dirs"],
            prefix=mod_config["prefix"],
            language=mod_config["language"],
            output_dir=output_dir,
            merge_threshold=mod_config["merge_threshold"],
            project_root=project_root,
        )
        if result:
            module_results.append(result)

    if not module_results:
        print("No modules produced output.")
        sys.exit(1)

    # Generate root index
    generate_root_index(module_results, output_dir)
    print(f"\nGenerated code index in {output_dir}")
    print(f"  Root index: {output_dir / 'index.md'}")
    for result in module_results:
        print(f"  {result['name']}: {result['decl_count']} declarations in {len(result['groups'])} packages")


if __name__ == "__main__":
    main()
