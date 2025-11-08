# Features Folder

**Purpose:** This folder contains feature-driven documentation organized by what the software does, not how code is structured.

**Why this exists:** Features often span multiple modules and components. This documentation explains end-to-end workflows, cross-cutting concerns, and user-facing functionality.

---

## What Goes in features/

**Feature documentation explains:**
- What the feature does (purpose and scope)
- How it works end-to-end (workflow across components)
- How to use it (user-facing or API)
- How it's implemented (technical details)
- How to configure it (settings and options)

**Examples:**
- Translation pipeline (spans multiple services and modules)
- PDF generation workflow (file processing, templates, output)
- Authentication system (login, sessions, permissions)
- Glossary management (CRUD operations, validation, storage)

---

## Organization Pattern

### Simple Features (Single File)

For straightforward features, use a single `.md` file:

```
features/
├── dark-mode-toggle.md
├── export-functionality.md
└── search-filter.md
```

**When to use:** Feature can be explained in <200 lines, <1000 words

---

### Complex Features (Folder)

For multi-faceted features, use a folder with multiple files:

```
features/translation-pipeline/
├── README.md           # Overview and purpose
├── workflow.md         # End-to-end process
├── api.md              # Programmatic interface
├── configuration.md    # Setup and options
└── examples.md         # Usage patterns
```

**When to use:** Feature requires multiple perspectives or detailed documentation

**See:** [TEMPLATE.md](TEMPLATE.md) for complete folder structure guide

---

## Relationship with Other Documentation

**features/ vs architecture.md:**
- architecture.md = Component design, tech stack, system-level decisions
- features/ = Cross-component workflows, user-facing functionality

**features/ vs fundamentals/:**
- features/ = What the software DOES (translation, export, auth)
- fundamentals/ = Core CONCEPTS (manual types, language handling, design principles)

**features/ vs code (docstrings/comments):**
- features/ = High-level understanding for reconstruction
- Code = Implementation details for developers working with code

---

## Guidelines

**Keep it LLM-friendly:**
- Target: <200 lines per file
- Target: <1000 words per file
- Use clear headings (max 3 levels: H1 → H2 → H3)
- Include examples and workflows
- Link to related docs (don't duplicate)

**Focus on reconstruction:**
Document what a seasoned developer would need to rebuild the feature without tribal knowledge.

---

**Last Updated:** 2025-11-08