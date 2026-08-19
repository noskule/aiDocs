"""Shared parse pipeline for code-index tool.

Discover, parse, and group source files into ModuleData for consumption
by both the index generator and analyzers.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from grouping import PackageGroup, group_declarations
from languages.base import Declaration
from languages.kotlin import KotlinAdapter


@dataclass
class ModuleData:
    """Parsed module with flat declarations and grouped packages."""

    name: str
    all_declarations: list[Declaration]  # Flat list (for cross-package checks)
    groups: list[PackageGroup]           # Grouped (for per-package checks)
    errors: int


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


def load_module(
    name: str,
    source_dirs: list[Path],
    prefix: str,
    language: str,
    merge_threshold: int,
) -> ModuleData | None:
    """Discover, parse, and group source files for a single module.

    Returns ModuleData, or None if no files found.
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

    return ModuleData(
        name=name,
        all_declarations=all_declarations,
        groups=groups,
        errors=errors,
    )
