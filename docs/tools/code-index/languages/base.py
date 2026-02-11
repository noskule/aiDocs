"""Declaration model and language adapter interface for code-index tool."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Declaration:
    """A single code declaration (class, function, property, etc.)."""

    kind: str  # class, data class, sealed class, interface, enum class, object, fun, val, var
    name: str
    signature: str  # Full signature line (e.g., "fun foo(x: Int): String")
    doc_summary: str = ""  # First sentence of KDoc/doc comment
    annotations: list[str] = field(default_factory=list)  # e.g., ["@Composable", "@Inject"]
    visibility: str = "public"  # public, private, protected, internal
    file_path: str = ""  # Relative path from source root
    package: str = ""  # e.g., "com.example.myapp.core"
    children: list[Declaration] = field(default_factory=list)  # Class members
    modifiers: list[str] = field(default_factory=list)  # e.g., ["suspend", "const", "override"]


class LanguageAdapter(ABC):
    """Abstract base class for language-specific AST extraction."""

    @abstractmethod
    def file_extension(self) -> str:
        """Return the file extension this adapter handles (e.g., '.kt')."""
        ...

    @abstractmethod
    def parse_file(self, file_path: Path, source_root: Path) -> list[Declaration]:
        """Parse a source file and return top-level declarations.

        Args:
            file_path: Absolute path to the source file.
            source_root: Root directory of the source tree (for relative paths).

        Returns:
            List of top-level Declaration objects found in the file.
        """
        ...
