"""Structural health analyzer — flags architectural and complexity issues."""

from __future__ import annotations

import statistics

from analyzers.base import Analyzer, Finding
from grouping import PackageGroup, strip_prefix
from languages.base import Declaration
from pipeline import ModuleData


# Default thresholds
GOD_CLASS_THRESHOLD = 12
PARAMETER_BLOAT_THRESHOLD = 5
DATA_CLASS_EXPLOSION_THRESHOLD = 8
FAT_INTERFACE_THRESHOLD = 6

# Default layer rules: annotation → allowed package segments
DEFAULT_LAYER_RULES: dict[str, list[str]] = {
    "Composable": ["ui", "presentation"],
    "Entity": ["data"],
    "Dao": ["data"],
    "HiltViewModel": ["presentation"],
}


def _count_params(signature: str) -> int:
    """Count parameters in a signature string.

    Handles nested generics (Map<String, List<Int>>) and lambdas by tracking
    <>, (), {} nesting depth and counting commas only at param depth.
    """
    # Find the parameter list between the first ( and its matching )
    paren_start = -1
    depth = 0
    for i, ch in enumerate(signature):
        if ch == "(":
            if depth == 0:
                paren_start = i
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                params_str = signature[paren_start + 1 : i].strip()
                break
    else:
        return 0

    if not params_str:
        return 0

    # Count commas at nesting depth 0
    count = 1
    angle = 0
    paren = 0
    brace = 0
    for ch in params_str:
        if ch == "<":
            angle += 1
        elif ch == ">":
            angle -= 1
        elif ch == "(":
            paren += 1
        elif ch == ")":
            paren -= 1
        elif ch == "{":
            brace += 1
        elif ch == "}":
            brace -= 1
        elif ch == "," and angle == 0 and paren == 0 and brace == 0:
            count += 1

    return count


class StructuralHealthAnalyzer(Analyzer):
    """Checks structural health: complexity, conventions, layer violations."""

    def __init__(self, config: dict | None = None):
        cfg = config or {}
        self._god_class = cfg.get("god_class_threshold", GOD_CLASS_THRESHOLD)
        self._param_bloat = cfg.get("parameter_bloat_threshold", PARAMETER_BLOAT_THRESHOLD)
        self._data_explosion = cfg.get("data_class_explosion_threshold", DATA_CLASS_EXPLOSION_THRESHOLD)
        self._fat_iface = cfg.get("fat_interface_threshold", FAT_INTERFACE_THRESHOLD)
        self._layer_rules: dict[str, list[str]] = cfg.get("layer_rules", DEFAULT_LAYER_RULES)

    def name(self) -> str:
        return "structural_health"

    def analyze(self, modules: list[ModuleData]) -> list[Finding]:
        findings: list[Finding] = []
        for mod in modules:
            findings.extend(self._check_god_classes(mod))
            findings.extend(self._check_parameter_bloat(mod))
            findings.extend(self._check_data_class_explosion(mod))
            findings.extend(self._check_fat_interfaces(mod))
            findings.extend(self._check_thin_interfaces(mod))
            findings.extend(self._check_layer_violations(mod))
            findings.extend(self._check_documentation_gaps(mod))
            findings.extend(self._check_package_imbalance(mod))
        return findings

    # ── God classes ─────────────────────────────────────────────────

    def _check_god_classes(self, mod: ModuleData) -> list[Finding]:
        findings = []
        for decl in mod.all_declarations:
            if decl.kind not in ("class", "sealed class", "data class", "object"):
                continue
            public_members = [c for c in decl.children if c.visibility == "public"]
            count = len(public_members)
            if count > self._god_class:
                findings.append(Finding(
                    category="god-class",
                    severity="warning",
                    message=f"{decl.name} has {count} public members (threshold: {self._god_class})",
                    declaration=decl.name,
                    package=decl.package,
                    file_path=decl.file_path,
                    details={"count": count, "threshold": self._god_class},
                ))
        return findings

    # ── Parameter bloat ─────────────────────────────────────────────

    def _check_parameter_bloat(self, mod: ModuleData) -> list[Finding]:
        findings = []
        for decl in mod.all_declarations:
            # Check top-level functions
            if decl.kind == "fun":
                findings.extend(self._check_params(decl))
            # Check class methods (skip data class constructors — they ARE the data)
            if decl.kind == "data class":
                for child in decl.children:
                    if child.kind == "fun":
                        findings.extend(self._check_params(child))
            elif decl.children:
                # For non-data classes, also check the constructor
                findings.extend(self._check_params(decl))
                for child in decl.children:
                    if child.kind == "fun":
                        findings.extend(self._check_params(child))
        return findings

    def _check_params(self, decl: Declaration) -> list[Finding]:
        count = _count_params(decl.signature)
        if count > self._param_bloat:
            return [Finding(
                category="parameter-bloat",
                severity="warning",
                message=f"{decl.name} has {count} parameters (threshold: {self._param_bloat})",
                declaration=decl.name,
                package=decl.package,
                file_path=decl.file_path,
                details={"count": count, "threshold": self._param_bloat},
            )]
        return []

    # ── Data class explosion ────────────────────────────────────────

    def _check_data_class_explosion(self, mod: ModuleData) -> list[Finding]:
        findings = []
        for group in mod.groups:
            data_classes = [d for d in group.declarations if d.kind == "data class"]
            count = len(data_classes)
            if count > self._data_explosion:
                findings.append(Finding(
                    category="data-class-explosion",
                    severity="warning",
                    message=f"Package {group.package} has {count} data classes (threshold: {self._data_explosion})",
                    declaration=f"{count} data classes",
                    package=group.package,
                    file_path=data_classes[0].file_path,
                    details={"count": count, "threshold": self._data_explosion},
                ))
        return findings

    # ── Fat interfaces ──────────────────────────────────────────────

    def _check_fat_interfaces(self, mod: ModuleData) -> list[Finding]:
        findings = []
        for decl in mod.all_declarations:
            if decl.kind != "interface":
                continue
            methods = [c for c in decl.children if c.kind == "fun"]
            count = len(methods)
            if count > self._fat_iface:
                findings.append(Finding(
                    category="fat-interface",
                    severity="warning",
                    message=f"{decl.name} has {count} methods (threshold: {self._fat_iface})",
                    declaration=decl.name,
                    package=decl.package,
                    file_path=decl.file_path,
                    details={"count": count, "threshold": self._fat_iface},
                ))
        return findings

    # ── Thin interfaces ─────────────────────────────────────────────

    def _check_thin_interfaces(self, mod: ModuleData) -> list[Finding]:
        findings = []
        for decl in mod.all_declarations:
            if decl.kind != "interface":
                continue
            methods = [c for c in decl.children if c.kind == "fun"]
            if len(methods) == 1:
                findings.append(Finding(
                    category="thin-interface",
                    severity="info",
                    message=f"{decl.name} has only 1 method — consider a function type",
                    declaration=decl.name,
                    package=decl.package,
                    file_path=decl.file_path,
                    details={"count": 1},
                ))
        return findings

    # ── Layer violations ────────────────────────────────────────────

    def _check_layer_violations(self, mod: ModuleData) -> list[Finding]:
        findings = []
        for decl in mod.all_declarations:
            if not decl.annotations:
                continue
            pkg_lower = decl.package.lower()
            for annotation in decl.annotations:
                allowed = self._layer_rules.get(annotation)
                if allowed is None:
                    continue
                if not any(segment in pkg_lower for segment in allowed):
                    findings.append(Finding(
                        category="layer-violation",
                        severity="error",
                        message=f"@{annotation} on {decl.name} in {decl.package} — expected in {'/'.join(allowed)} layer",
                        declaration=decl.name,
                        package=decl.package,
                        file_path=decl.file_path,
                        details={"annotation": annotation, "allowed_layers": allowed},
                    ))
        return findings

    # ── Documentation gaps ──────────────────────────────────────────

    def _check_documentation_gaps(self, mod: ModuleData) -> list[Finding]:
        findings = []
        for group in mod.groups:
            total = len(group.declarations)
            if total == 0:
                continue
            documented = sum(1 for d in group.declarations if d.doc_summary)
            pct = documented / total * 100
            if pct < 50:
                findings.append(Finding(
                    category="documentation-gap",
                    severity="warning",
                    message=f"Package {group.package}: {documented}/{total} declarations documented ({pct:.0f}%)",
                    declaration=f"{documented}/{total} documented",
                    package=group.package,
                    file_path=group.declarations[0].file_path,
                    details={"documented": documented, "total": total, "percentage": round(pct, 1)},
                ))
            elif pct < 80:
                findings.append(Finding(
                    category="documentation-gap",
                    severity="info",
                    message=f"Package {group.package}: {documented}/{total} declarations documented ({pct:.0f}%)",
                    declaration=f"{documented}/{total} documented",
                    package=group.package,
                    file_path=group.declarations[0].file_path,
                    details={"documented": documented, "total": total, "percentage": round(pct, 1)},
                ))
        return findings

    # ── Package imbalance ───────────────────────────────────────────

    def _check_package_imbalance(self, mod: ModuleData) -> list[Finding]:
        # Skip modules with fewer than 3 packages (e.g., wear module)
        if len(mod.groups) < 3:
            return []

        sizes = [len(g.declarations) for g in mod.groups]
        if len(sizes) < 3:
            return []

        mean = statistics.mean(sizes)
        stdev = statistics.stdev(sizes)
        threshold = mean + 2 * stdev

        findings = []
        for group, size in zip(mod.groups, sizes):
            if size > threshold:
                findings.append(Finding(
                    category="package-imbalance",
                    severity="warning",
                    message=f"Package {group.package} has {size} declarations (mean: {mean:.0f}, threshold: {threshold:.0f})",
                    declaration=f"{size} declarations",
                    package=group.package,
                    file_path=group.declarations[0].file_path,
                    details={"count": size, "mean": round(mean, 1), "stdev": round(stdev, 1), "threshold": round(threshold, 1)},
                ))
        return findings
