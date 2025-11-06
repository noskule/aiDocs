# Documentation Guide

## Overview

This is a **documentation template** optimized for AI-assisted development:

- **LLM-Friendly:** Structured for AI coding assistants (Claude, Copilot, ChatGPT) with dedicated behavioral instructions
- **Feature-First:** Organized by what software does (features), not how code is structured (modules/backend/frontend)
- **AI-Documented:** Designed for human + LLM collaboration - developers write architecture, LLMs help generate feature docs
- **Portable:** Copy entire `docs/` folder to any project for instant consistency

---

## Feature-Driven Approach

**Organize by features (what software does), not code structure (how it's built).**

**Use `features/` for:**
- Cross-cutting features spanning multiple modules
- User-facing functionality (translation pipeline, PDF generation)
- Complete stories from input to output

**Use `fundamentals/` for:**
- Core concepts underpinning multiple features
- Architectural patterns and principles
- Domain knowledge needed to understand the system

**Examples:**
- ✅ `features/translation-pipeline/` - How translation works across components
- ✅ `fundamentals/manual-types.md` - Concept of manual types (Superadmin, User)
- ❌ `backend/translator.md` - Code-driven (avoid)

---

## Feature Folder Contents

**For complex features, use folder structure with multiple files representing different aspects:**

**Core files:**
- `README.md` - Feature overview and purpose
- `workflow.md` - Step-by-step process (how it works end-to-end)

**Interface files:**
- `api.md` - API/programmatic interface
- `ui.md` - User interface (if applicable)
- `cli.md` - Command-line interface (if applicable)

**Implementation files:**
- `implementation.md` - Technical implementation details
- `architecture.md` - Feature-specific architectural decisions
- `data.md` - Data structures, formats, schemas

**Usage files:**
- `examples.md` - Usage examples and common patterns
- `configuration.md` - How to configure the feature
- `integration.md` - How to integrate with other systems

**Support files:**
- `troubleshooting.md` - Common issues and solutions
- `testing.md` - How to test this feature
- `security.md` - Security considerations (if applicable)

**Example:**
```
features/translation-pipeline/
├── README.md           # What is translation pipeline?
├── workflow.md         # Source → Glossary → Translate → Output
├── api.md              # TranslationService API
├── configuration.md    # Engines, languages, glossary setup
├── troubleshooting.md  # API failures, rate limits
└── examples.md         # Common translation patterns
```

**Principle:** Files represent **what users/developers need to know**, not how code is organized.

---

## Reusable Template

**Copy as-is (reusable across projects):**
- `README.md` - This structure guide
- `AGENTS.md` - LLM behavioral instructions
- `CODING_GUIDELINES.md` - Development workflow and rules
- Folder structure: `features/`, `fundamentals/`, `testing/`, `project/`

**Update per project (project-specific):**
- `INSTALLATION.md` - Your prerequisites and setup
- `ARCHITECTURE.md` - Your system design and tech stack
- `USAGE.md` - How to use your tool
- Content within folders

**Root README:**
- Manually written by developer for each project
- Describes project identity (what it is)
- Points to `docs/` for complete documentation

---

## Complete Structure

```
PROJECT_ROOT/
├── README.md                     # Project overview (manual, project-specific)
│
└── docs/
    ├── README.md                 # This file - documentation guide
    ├── AGENTS.md                 # LLM behavioral instructions
    ├── INSTALLATION.md           # Setup and prerequisites
    ├── ARCHITECTURE.md           # System design & tech stack
    ├── USAGE.md                  # Usage guide and key files
    ├── CODING_GUIDELINES.md      # Development and documentation rules
    │
    ├── features/                 # Feature-driven documentation
    │   ├── [feature].md          # Simple feature (single file)
    │   └── [feature]/            # Complex feature (folder)
    │       ├── README.md         # Feature overview
    │       ├── implementation.md # How it's implemented
    │       └── examples.md       # Usage examples
    │
    ├── fundamentals/             # Core concepts
    │   └── [topic].md            # Fundamental topics
    │
    ├── testing/                  # Testing documentation
    │   ├── README.md             # Testing overview
    │   ├── QUICK_START.md        # How to run/write tests
    │   └── EVALUATION.md         # Coverage analysis
    │
    └── project/                  # Project management
        ├── README.md             # Project status
        ├── ROADMAP.md            # Development roadmap
        └── CHANGELOG.md          # Version history
```

**About AGENTS.md:**
- LLM-addressed instructions for AI coding assistants
- Contains: Mandatory workflow, critical constraints, interaction patterns
- References CODING_GUIDELINES.md and ARCHITECTURE.md (no duplication)

---

## Content Ownership

**Principle:** Each piece of information lives in **exactly ONE location**. All other documents reference, never duplicate.

### Ownership Table

| Content Type | Owner | Notes |
|--------------|-------|-------|
| **Technology Stack** | `ARCHITECTURE.md` | Dependencies, versions, rationale |
| **Installation** | `INSTALLATION.md` | Prerequisites, setup, troubleshooting |
| **Usage** | `USAGE.md` | How to run, configuration, workflows |
| **System Design** | `ARCHITECTURE.md` | Components, data flow, decisions |
| **Development Workflow** | `CODING_GUIDELINES.md` | Branch → code → test → review → PR |
| **Features** | `features/` | Feature deep-dives |
| **Core Concepts** | `fundamentals/` | Essential concepts |
| **Testing** | `testing/` | How to run/write tests, coverage |
| **Roadmap** | `project/ROADMAP.md` | Milestones, future plans |
| **Version History** | `project/CHANGELOG.md` | Release notes, breaking changes |
| **LLM Instructions** | `AGENTS.md` | AI assistant workflow |

### Rules

1. **Never duplicate** - Link instead
2. **One owner** - Single authoritative source
3. **Reference freely** - Cross-link everywhere
4. **Update source only** - Change once, correct everywhere

### Examples

✅ **Correct:**
```markdown
For installation, see [Installation Guide](INSTALLATION.md).
```

❌ **Incorrect:**
```markdown
Prerequisites: Python 3.13+, Poetry, Pandoc...
(Duplicating INSTALLATION.md content)
```

---

## Principles

### 1. Single Source of Truth
Each fact lives in ONE place. Cross-reference instead of duplicate.

### 2. Mandatory Documentation
All feature implementations and architectural changes require documentation updates. PRs without docs will be rejected.

### 3. Updated with Code
Documentation updates are part of development, not afterthought. Update in same commit.

### 4. Simple Structure
Clear names, flat structure (max 3 levels), good cross-linking, technical audience.

---

## Quick Reference

- **Installation issues?** → [INSTALLATION.md](INSTALLATION.md#troubleshooting)
- **How to use?** → [USAGE.md](USAGE.md)
- **How does it work?** → [ARCHITECTURE.md](ARCHITECTURE.md)
- **Development rules?** → [CODING_GUIDELINES.md](CODING_GUIDELINES.md)
- **Testing?** → [testing/QUICK_START.md](testing/QUICK_START.md)

---

**Last Updated:** 2025-11-06
