"""Kotlin language adapter for code-index tool using tree-sitter."""

from __future__ import annotations

import re
from pathlib import Path

from tree_sitter_language_pack import get_parser

from .base import Declaration, LanguageAdapter

# Annotations worth surfacing in the index (architecture-relevant)
RELEVANT_ANNOTATIONS = {
    "AndroidEntryPoint",
    "Composable",
    "Dao",
    "Database",
    "Entity",
    "HiltAndroidApp",
    "HiltViewModel",
    "Immutable",
    "Inject",
    "InstallIn",
    "Module",
    "Serializable",
    "Singleton",
    "Stable",
}

# Annotations to skip entirely
SKIP_ANNOTATIONS = {"Preview", "Suppress", "SuppressLint"}


class KotlinAdapter(LanguageAdapter):
    """Extracts declarations from Kotlin source files using tree-sitter."""

    def __init__(self) -> None:
        self._parser = get_parser("kotlin")

    def file_extension(self) -> str:
        return ".kt"

    def parse_file(self, file_path: Path, source_root: Path) -> list[Declaration]:
        source_bytes = file_path.read_bytes()
        tree = self._parser.parse(source_bytes)
        root = tree.root_node

        package = self._extract_package(root)
        rel_path = str(file_path.relative_to(source_root)).replace("\\", "/")

        declarations: list[Declaration] = []
        children = root.children
        skip_next = False

        for i, node in enumerate(children):
            if skip_next:
                skip_next = False
                continue

            decl = self._extract_declaration(
                node, source_bytes, children, i, package, rel_path
            )
            if decl is not None:
                # Handle @Inject constructor pattern: class_declaration followed by
                # ERROR node containing the constructor and class body
                if (
                    node.type == "class_declaration"
                    and i + 1 < len(children)
                    and children[i + 1].type == "ERROR"
                ):
                    error_node = children[i + 1]
                    extra = self._extract_inject_constructor_members(
                        error_node, source_bytes, package, rel_path
                    )
                    if extra is not None:
                        inject_ann, members = extra
                        if inject_ann and "Inject" not in decl.annotations:
                            decl.annotations.append("Inject")
                        decl.children.extend(members)
                        skip_next = True

                declarations.append(decl)

        return declarations

    # ── Package extraction ──────────────────────────────────────────

    def _extract_package(self, root) -> str:
        for child in root.children:
            if child.type == "package_header":
                for c in child.children:
                    if c.type == "identifier":
                        return c.text.decode("utf-8")
        return ""

    # ── Declaration extraction ──────────────────────────────────────

    def _extract_declaration(
        self, node, source_bytes: bytes, siblings: list, index: int,
        package: str, rel_path: str,
    ) -> Declaration | None:
        if node.type == "class_declaration":
            return self._extract_class(node, source_bytes, siblings, index, package, rel_path)
        elif node.type == "object_declaration":
            return self._extract_object(node, source_bytes, siblings, index, package, rel_path)
        elif node.type == "function_declaration":
            return self._extract_function(node, source_bytes, siblings, index, package, rel_path)
        elif node.type == "property_declaration":
            return self._extract_property(node, source_bytes, siblings, index, package, rel_path)
        return None

    # ── Class extraction ────────────────────────────────────────────

    def _extract_class(
        self, node, source_bytes: bytes, siblings: list, index: int,
        package: str, rel_path: str,
    ) -> Declaration | None:
        visibility = self._get_visibility(node)
        if visibility in ("private", "internal"):
            return None

        name = self._get_type_name(node)
        kind = self._determine_class_kind(node)
        annotations = [a for a in self._get_annotations(node) if a in RELEVANT_ANNOTATIONS]
        doc = self._find_kdoc(source_bytes, siblings, index)
        modifiers = self._get_modifiers(node)

        # Build signature
        sig = self._build_class_signature(node, kind, name, annotations)

        # Extract children (class body members)
        children = self._extract_class_members(node, source_bytes, package, rel_path)

        return Declaration(
            kind=kind,
            name=name,
            signature=sig,
            doc_summary=doc,
            annotations=annotations,
            visibility=visibility,
            file_path=rel_path,
            package=package,
            children=children,
            modifiers=modifiers,
        )

    def _determine_class_kind(self, node) -> str:
        """Determine the kind of class from modifiers and keywords."""
        has_interface = False
        has_enum = False
        has_data = False
        has_sealed = False

        for child in node.children:
            if child.type == "interface":
                has_interface = True
            elif child.type == "enum":
                has_enum = True
            elif child.type == "modifiers":
                for mod in child.children:
                    if mod.type == "class_modifier":
                        mod_text = mod.text.decode("utf-8")
                        if mod_text == "data":
                            has_data = True
                        elif mod_text == "sealed":
                            has_sealed = True
                        elif mod_text == "enum":
                            has_enum = True
                    elif mod.text.decode("utf-8") == "data":
                        has_data = True
                    elif mod.text.decode("utf-8") == "sealed":
                        has_sealed = True

        if has_interface:
            return "interface"
        if has_enum:
            return "enum class"
        if has_sealed:
            return "sealed class"
        if has_data:
            return "data class"
        return "class"

    def _build_class_signature(self, node, kind: str, name: str, annotations: list[str]) -> str:
        """Build a one-line class signature."""
        parts = []
        if annotations:
            parts.append(" ".join(f"@{a}" for a in annotations))
        parts.append(f"{kind} {name}")

        # Add constructor params for data classes
        if kind == "data class":
            ctor = self._find_child(node, "primary_constructor")
            if ctor:
                params = self._extract_constructor_params(ctor)
                if params:
                    parts[-1] += f"({', '.join(params)})"

        # Add supertype
        for child in node.children:
            if child.type == "delegation_specifier":
                super_text = child.text.decode("utf-8")
                # Strip constructor invocation parens for readability
                if super_text.endswith("()"):
                    super_text = super_text[:-2]
                parts[-1] += f" : {super_text}"
                break

        return " ".join(parts) if len(parts) > 1 else parts[0]

    def _extract_constructor_params(self, ctor_node) -> list[str]:
        """Extract constructor parameters (non-private, non-override)."""
        params = []
        for child in ctor_node.children:
            if child.type == "class_parameter":
                vis = "public"
                is_override = False
                for mod_node in child.children:
                    if mod_node.type == "modifiers":
                        for m in mod_node.children:
                            text = m.text.decode("utf-8")
                            if text in ("private", "internal"):
                                vis = text
                            elif text == "override":
                                is_override = True
                if vis in ("private", "internal"):
                    continue
                if is_override:
                    continue
                # Build param string: val/var name: Type
                binding = ""
                param_name = ""
                param_type = ""
                for c in child.children:
                    if c.type == "binding_pattern_kind":
                        binding = c.text.decode("utf-8")
                    elif c.type == "simple_identifier":
                        param_name = c.text.decode("utf-8")
                    elif c.type in ("user_type", "nullable_type", "function_type"):
                        param_type = c.text.decode("utf-8")
                if param_name and param_type:
                    prefix = f"{binding} " if binding else ""
                    params.append(f"{prefix}{param_name}: {param_type}")
        return params

    # ── @Inject constructor ERROR node handling ──────────────────────

    def _extract_inject_constructor_members(
        self, error_node, source_bytes: bytes, package: str, rel_path: str,
    ) -> tuple[bool, list[Declaration]] | None:
        """Extract members from an ERROR node caused by @Inject constructor on new line.

        Returns (has_inject_annotation, members) or None if not the expected pattern.
        """
        has_inject = False
        body_node = None

        for child in error_node.children:
            if child.type == "annotation":
                ann_name = self._get_annotation_name(child)
                if ann_name == "Inject":
                    has_inject = True
            elif child.type == "lambda_literal":
                body_node = child

        if body_node is None:
            return None

        # Find statements inside the lambda_literal (which is really the class body)
        members: list[Declaration] = []
        stmts_node = None
        for child in body_node.children:
            if child.type == "statements":
                stmts_node = child
                break

        if stmts_node is None:
            return (has_inject, members)

        children = stmts_node.children
        for i, child in enumerate(children):
            decl = None
            if child.type == "function_declaration":
                decl = self._extract_function(
                    child, source_bytes, children, i, package, rel_path, is_member=True
                )
            elif child.type == "property_declaration":
                decl = self._extract_property(
                    child, source_bytes, children, i, package, rel_path, is_member=True
                )
            elif child.type == "class_declaration":
                decl = self._extract_class(
                    child, source_bytes, children, i, package, rel_path
                )
            elif child.type == "object_declaration":
                decl = self._extract_object(
                    child, source_bytes, children, i, package, rel_path
                )
            if decl is not None:
                members.append(decl)

        return (has_inject, members)

    # ── Object extraction ───────────────────────────────────────────

    def _extract_object(
        self, node, source_bytes: bytes, siblings: list, index: int,
        package: str, rel_path: str,
    ) -> Declaration | None:
        visibility = self._get_visibility(node)
        if visibility in ("private", "internal"):
            return None

        name = self._get_type_name(node)
        annotations = [a for a in self._get_annotations(node) if a in RELEVANT_ANNOTATIONS]
        doc = self._find_kdoc(source_bytes, siblings, index)

        sig = f"object {name}"
        # Add supertype
        for child in node.children:
            if child.type == "delegation_specifier":
                super_text = child.text.decode("utf-8")
                if super_text.endswith("()"):
                    super_text = super_text[:-2]
                sig += f" : {super_text}"
                break

        children = self._extract_class_members(node, source_bytes, package, rel_path)

        return Declaration(
            kind="object",
            name=name,
            signature=sig,
            doc_summary=doc,
            annotations=annotations,
            visibility=visibility,
            file_path=rel_path,
            package=package,
            children=children,
            modifiers=[],
        )

    # ── Function extraction ─────────────────────────────────────────

    def _extract_function(
        self, node, source_bytes: bytes, siblings: list, index: int,
        package: str, rel_path: str, is_member: bool = False,
    ) -> Declaration | None:
        visibility = self._get_visibility(node)
        if visibility in ("private", "internal"):
            return None

        modifiers = self._get_modifiers(node)
        # Skip override functions (they duplicate interface definitions)
        if "override" in modifiers:
            return None

        name = self._get_simple_name(node)
        all_annotations = self._get_all_annotation_names(node)

        # Skip @Preview composables
        if "Preview" in all_annotations:
            return None

        annotations = [a for a in all_annotations if a not in SKIP_ANNOTATIONS]

        doc = self._find_kdoc(source_bytes, siblings, index)
        sig = self._build_function_signature(node, modifiers, name)

        return Declaration(
            kind="fun",
            name=name,
            signature=sig,
            doc_summary=doc,
            annotations=[a for a in annotations if a in RELEVANT_ANNOTATIONS],
            visibility=visibility,
            file_path=rel_path,
            package=package,
            children=[],
            modifiers=modifiers,
        )

    def _build_function_signature(self, node, modifiers: list[str], name: str) -> str:
        """Build function signature: [suspend] fun name(params): ReturnType"""
        parts = []
        if "suspend" in modifiers:
            parts.append("suspend")
        parts.append("fun")
        parts.append(name)

        # Parameters
        params_node = self._find_child(node, "function_value_parameters")
        if params_node:
            params = self._extract_function_params(params_node)
            parts[-1] += f"({', '.join(params)})"
        else:
            parts[-1] += "()"

        # Return type
        ret_type = self._get_return_type(node)
        if ret_type:
            return " ".join(parts) + f": {ret_type}"
        return " ".join(parts)

    def _extract_function_params(self, params_node) -> list[str]:
        """Extract function parameter signatures (name: Type, no defaults)."""
        params = []
        for child in params_node.children:
            if child.type == "parameter":
                param_name = ""
                param_type = ""
                for c in child.children:
                    if c.type == "simple_identifier":
                        param_name = c.text.decode("utf-8")
                    elif c.type in ("user_type", "nullable_type", "function_type"):
                        param_type = c.text.decode("utf-8")
                if param_name and param_type:
                    params.append(f"{param_name}: {param_type}")
                elif param_name:
                    params.append(param_name)
        return params

    def _get_return_type(self, node) -> str:
        """Get function return type (node after ':' separator)."""
        found_colon = False
        for child in node.children:
            if child.type == ":" and not found_colon:
                found_colon = True
                continue
            if found_colon and child.type in ("user_type", "nullable_type", "function_type"):
                return child.text.decode("utf-8")
        return ""

    # ── Property extraction ─────────────────────────────────────────

    def _extract_property(
        self, node, source_bytes: bytes, siblings: list, index: int,
        package: str, rel_path: str, is_member: bool = False,
    ) -> Declaration | None:
        visibility = self._get_visibility(node)
        if visibility in ("private", "internal"):
            return None

        modifiers = self._get_modifiers(node)
        if "override" in modifiers:
            return None

        name = ""
        prop_type = ""
        binding_kind = "val"

        for child in node.children:
            if child.type == "binding_pattern_kind":
                binding_kind = child.text.decode("utf-8")
            elif child.type == "variable_declaration":
                # Name and optional type
                for vc in child.children:
                    if vc.type == "simple_identifier":
                        name = vc.text.decode("utf-8")
                    elif vc.type in ("user_type", "nullable_type", "function_type"):
                        prop_type = vc.text.decode("utf-8")
                # Also check for type after : in variable_declaration
                if not prop_type:
                    name_text = child.text.decode("utf-8")
                    if ":" in name_text:
                        parts = name_text.split(":", 1)
                        name = parts[0].strip()
                        prop_type = parts[1].strip()

        if not name:
            return None

        # Also check for type after the variable_declaration (at property level)
        if not prop_type:
            found_colon = False
            for child in node.children:
                if child.type == ":":
                    found_colon = True
                    continue
                if found_colon and child.type in ("user_type", "nullable_type", "function_type"):
                    prop_type = child.text.decode("utf-8")
                    break

        annotations = self._get_annotations(node)
        doc = self._find_kdoc(source_bytes, siblings, index)

        # Build signature
        prefix_parts = []
        if "const" in modifiers:
            prefix_parts.append("const")
        prefix_parts.append(binding_kind)
        sig = f"{' '.join(prefix_parts)} {name}"
        if prop_type:
            sig += f": {prop_type}"

        return Declaration(
            kind=binding_kind,
            name=name,
            signature=sig,
            doc_summary=doc,
            annotations=[a for a in annotations if a in RELEVANT_ANNOTATIONS],
            visibility=visibility,
            file_path=rel_path,
            package=package,
            children=[],
            modifiers=modifiers,
        )

    # ── Class member extraction ─────────────────────────────────────

    def _extract_class_members(
        self, class_node, source_bytes: bytes, package: str, rel_path: str,
    ) -> list[Declaration]:
        """Extract public members from a class/object body."""
        members: list[Declaration] = []
        body = self._find_child(class_node, "class_body")
        if body is None:
            # Check enum body
            body = self._find_child(class_node, "enum_class_body")
            if body is None:
                return members

        children = body.children
        for i, child in enumerate(children):
            decl = None
            if child.type == "function_declaration":
                decl = self._extract_function(
                    child, source_bytes, children, i, package, rel_path, is_member=True
                )
            elif child.type == "property_declaration":
                decl = self._extract_property(
                    child, source_bytes, children, i, package, rel_path, is_member=True
                )
            elif child.type == "class_declaration":
                decl = self._extract_class(
                    child, source_bytes, children, i, package, rel_path
                )
            elif child.type == "object_declaration":
                decl = self._extract_object(
                    child, source_bytes, children, i, package, rel_path
                )
            elif child.type == "companion_object":
                comp_members = self._extract_companion_members(
                    child, source_bytes, package, rel_path
                )
                members.extend(comp_members)
                continue

            if decl is not None:
                members.append(decl)

        return members

    def _extract_companion_members(
        self, comp_node, source_bytes: bytes, package: str, rel_path: str,
    ) -> list[Declaration]:
        """Extract public members from a companion object."""
        members: list[Declaration] = []
        body = self._find_child(comp_node, "class_body")
        if body is None:
            return members

        children = body.children
        for i, child in enumerate(children):
            decl = None
            if child.type == "function_declaration":
                decl = self._extract_function(
                    child, source_bytes, children, i, package, rel_path, is_member=True
                )
            elif child.type == "property_declaration":
                decl = self._extract_property(
                    child, source_bytes, children, i, package, rel_path, is_member=True
                )
            if decl is not None:
                members.append(decl)

        return members

    # ── Annotation extraction ───────────────────────────────────────

    def _get_all_annotation_names(self, node) -> list[str]:
        """Get all annotation names from a declaration node (unfiltered)."""
        annotations = []
        for child in node.children:
            if child.type == "modifiers":
                for mod in child.children:
                    if mod.type == "annotation":
                        ann_name = self._get_annotation_name(mod)
                        if ann_name:
                            annotations.append(ann_name)
        return annotations

    def _get_annotations(self, node) -> list[str]:
        """Get relevant annotations from a declaration node (filtered)."""
        return [a for a in self._get_all_annotation_names(node) if a not in SKIP_ANNOTATIONS]

    def _get_annotation_name(self, ann_node) -> str:
        """Extract annotation name from annotation node."""
        for child in ann_node.children:
            if child.type == "user_type":
                # Get just the type name, not the full qualified name
                for tc in child.children:
                    if tc.type == "type_identifier":
                        return tc.text.decode("utf-8")
                return child.text.decode("utf-8")
            elif child.type == "constructor_invocation":
                # Annotation with arguments: @Preview(showBackground = true)
                for tc in child.children:
                    if tc.type == "user_type":
                        for uc in tc.children:
                            if uc.type == "type_identifier":
                                return uc.text.decode("utf-8")
                        return tc.text.decode("utf-8")
        return ""

    # ── Visibility extraction ───────────────────────────────────────

    def _get_visibility(self, node) -> str:
        """Get visibility modifier (public if none specified)."""
        for child in node.children:
            if child.type == "modifiers":
                for mod in child.children:
                    if mod.type == "visibility_modifier":
                        return mod.text.decode("utf-8")
        return "public"

    # ── Modifier extraction ─────────────────────────────────────────

    def _get_modifiers(self, node) -> list[str]:
        """Get non-annotation modifiers (suspend, override, const, abstract, etc.)."""
        modifiers = []
        for child in node.children:
            if child.type == "modifiers":
                for mod in child.children:
                    if mod.type == "annotation":
                        continue
                    if mod.type == "visibility_modifier":
                        continue
                    text = mod.text.decode("utf-8")
                    modifiers.append(text)
        return modifiers

    # ── KDoc extraction ─────────────────────────────────────────────

    def _find_kdoc(self, source_bytes: bytes, siblings: list, index: int) -> str:
        """Find KDoc comment for a declaration by checking previous sibling or source text."""
        # Method 1: Check previous sibling
        if index > 0:
            prev = siblings[index - 1]
            if prev.type == "multiline_comment":
                text = prev.text.decode("utf-8")
                if text.startswith("/**"):
                    return self._parse_kdoc_summary(text)

        # Method 2: Search backwards in source bytes for KDoc before this node
        current_node = siblings[index] if index < len(siblings) else None
        if current_node:
            start_byte = current_node.start_byte
            # Look backwards up to 500 bytes for a KDoc comment
            search_start = max(0, start_byte - 500)
            preceding = source_bytes[search_start:start_byte].decode("utf-8", errors="replace")
            # Find last /** ... */ in the preceding text
            match = re.search(r'/\*\*[\s\S]*?\*/', preceding)
            if match:
                # Make sure there's only whitespace between the KDoc end and the declaration
                after_kdoc = preceding[match.end():]
                if after_kdoc.strip() == "":
                    return self._parse_kdoc_summary(match.group())

        return ""

    def _parse_kdoc_summary(self, kdoc: str) -> str:
        """Extract first sentence from KDoc comment."""
        # Remove /** and */
        text = kdoc.strip()
        if text.startswith("/**"):
            text = text[3:]
        if text.endswith("*/"):
            text = text[:-2]

        # Remove leading * from each line
        lines = []
        for line in text.split("\n"):
            line = line.strip()
            if line.startswith("*"):
                line = line[1:].strip()
            lines.append(line)

        text = " ".join(lines).strip()

        # Stop at @param, @return, etc.
        at_idx = text.find("@param")
        if at_idx == -1:
            at_idx = text.find("@return")
        if at_idx == -1:
            at_idx = text.find("@property")
        if at_idx > 0:
            text = text[:at_idx].strip()

        # Take first sentence
        # Look for sentence-ending punctuation followed by space or end
        match = re.match(r'^(.*?[.!?])(?:\s|$)', text)
        if match:
            return match.group(1).strip()

        # If no sentence-ending punctuation, take first line/paragraph
        if "\n" in text:
            return text.split("\n")[0].strip()

        return text.strip()

    # ── Utility methods ─────────────────────────────────────────────

    def _get_type_name(self, node) -> str:
        """Get the type identifier name from a class/object declaration."""
        for child in node.children:
            if child.type == "type_identifier":
                return child.text.decode("utf-8")
        return ""

    def _get_simple_name(self, node) -> str:
        """Get simple_identifier name from a function/property declaration."""
        for child in node.children:
            if child.type == "simple_identifier":
                return child.text.decode("utf-8")
        return ""

    def _find_child(self, node, child_type: str):
        """Find first child of given type."""
        for child in node.children:
            if child.type == child_type:
                return child
        return None
