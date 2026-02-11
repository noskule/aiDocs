"""Package grouping and merge logic for code-index tool."""

from __future__ import annotations

from dataclasses import dataclass, field

from languages.base import Declaration

# Priority order for sorting declarations within a group
KIND_PRIORITY = {
    "interface": 0,
    "sealed class": 1,
    "class": 2,
    "data class": 3,
    "enum class": 4,
    "object": 5,
    "fun": 6,
    "val": 7,
    "var": 8,
}


@dataclass
class PackageGroup:
    """A group of declarations sharing the same (stripped) package name."""

    package: str  # Stripped package name (e.g., "core.hrv")
    declarations: list[Declaration] = field(default_factory=list)

    @property
    def display_path(self) -> str:
        """Convert package name to file path (e.g., 'core.hrv' -> 'core/hrv')."""
        if self.package == "_root":
            return "_root"
        return self.package.replace(".", "/")

    @property
    def file_name(self) -> str:
        """Markdown file name for this group (e.g., 'core/hrv.md')."""
        return f"{self.display_path}.md"


def strip_prefix(package: str, prefix: str) -> str:
    """Strip common package prefix, returning the relative package name."""
    if package.startswith(prefix):
        stripped = package[len(prefix):]
        if stripped.startswith("."):
            stripped = stripped[1:]
        return stripped
    return package


def group_declarations(
    declarations: list[Declaration],
    prefix: str,
    merge_threshold: int = 2,
) -> list[PackageGroup]:
    """Group declarations by stripped package name with depth-based merging.

    Args:
        declarations: All declarations from parsed source files.
        prefix: Common package prefix to strip (e.g., "com.example.myapp").
        merge_threshold: Package depth at which sub-packages merge into parent.
            depth-3+ packages flatten into their depth-2 parent.

    Returns:
        Sorted list of PackageGroup objects.
    """
    # Strip prefix and group by package
    raw_groups: dict[str, list[Declaration]] = {}
    for decl in declarations:
        stripped = strip_prefix(decl.package, prefix)
        if not stripped:
            stripped = "_root"
        raw_groups.setdefault(stripped, []).append(decl)

    # Apply merge rule: depth > merge_threshold flattens into parent
    merged_groups: dict[str, list[Declaration]] = {}
    for pkg, decls in raw_groups.items():
        merged_pkg = _merge_package(pkg, merge_threshold)
        merged_groups.setdefault(merged_pkg, []).extend(decls)

    # Build PackageGroup objects and sort
    groups = []
    for pkg, decls in sorted(merged_groups.items()):
        # Sort declarations within group: by file_path, then kind priority, then name
        decls.sort(key=lambda d: (d.file_path, KIND_PRIORITY.get(d.kind, 99), d.name))
        groups.append(PackageGroup(package=pkg, declarations=decls))

    return groups


def _merge_package(package: str, threshold: int) -> str:
    """Merge deep packages into their parent at the threshold depth.

    Examples with threshold=2:
        'data.db.converters' -> 'data.db'
        'data.db.dao' -> 'data.db'
        'domain.model.backup' -> 'domain.model'
        'ui.components.training' -> 'ui.components'
        'core.hrv' -> 'core.hrv' (depth=2, not merged)
        'data' -> 'data' (depth=1, not merged)
    """
    parts = package.split(".")
    if len(parts) > threshold:
        return ".".join(parts[:threshold])
    return package
