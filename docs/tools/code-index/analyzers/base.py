"""Base types for code-index analyzers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from pipeline import ModuleData


@dataclass
class Finding:
    """A single analysis finding."""

    category: str     # "god-class", "parameter-bloat", etc.
    severity: str     # "error", "warning", "info"
    message: str      # Human-readable one-liner
    declaration: str  # Declaration name
    package: str      # Stripped package name
    file_path: str    # Relative source file path
    details: dict = field(default_factory=dict)  # Extra data (threshold, actual count, etc.)


class Analyzer(ABC):
    """Abstract base class for code analyzers."""

    @abstractmethod
    def name(self) -> str:
        """Return the analyzer's identifier (e.g., 'structural_health')."""
        ...

    @abstractmethod
    def analyze(self, modules: list[ModuleData]) -> list[Finding]:
        """Run analysis across all modules and return findings."""
        ...
