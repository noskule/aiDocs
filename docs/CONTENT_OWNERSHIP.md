# Content Ownership Reference

**Principle:** Each piece of information lives in **exactly ONE location**. All other documents reference, never duplicate.

## Content Ownership by File

### `README.md` (Root)

- **Project overview** - What the project does (brief, compelling description)
- **Key features** - Main capabilities and benefits
- **Documentation structure** - Complete directory tree showing all docs
- **Not included:** Installation steps (→ installation.md), detailed architecture (→ architecture.md), usage details (→ usage.md)

### `docs/AGENTS.md`

- **Audience:** AI coding assistants (LLM-addressed)
- **Contains:** Project workflow awareness, mandatory workflow reference, critical constraints, LLM-specific behaviors
- **Note:** Does NOT duplicate content from other docs, only LLM interaction patterns and behavioral instructions

### `docs/documentation.md`

- **Main documentation entry point** - Curated, logically organized overview
- Project overview (what problem it solves, main capabilities)
- High-level architecture narrative (how pieces fit together)
- Functional organization (features grouped by logical areas, not code structure)
- Brief explanations with links to detailed features/ and fundamentals/ docs
- Common workflows and quick reference

### `docs/installation.md`

- Prerequisites, installation steps, configuration, verification, troubleshooting, updating

### `docs/architecture.md`

- Technology stack, technology decisions, system architecture, data flow
- Module organization, data structures, business rules
- Algorithm pseudocode, git versioning workflow, design decisions

### `docs/usage.md`

- Running the application, configuration, common workflows
- Key files, file naming conventions, environment variables

### `docs/CODING_GUIDELINES.md`

- When to document, what goes where, documentation workflow, code examples

### `docs/features/`

- Individual feature deep-dives, feature architecture, feature usage, feature decisions
- Examples: `translation-pipeline.md`, `pdf-generation.md`, `glossary-system.md`

### `docs/fundamentals/`

- Core concepts, design principles, key abstractions, domain knowledge
- Examples: `manual-types.md`, `language-handling.md`, `wiki-structure.md`

### `docs/testing.md`

- Testing strategy (approach, what to test), running tests, writing tests, coverage goals

### `docs/project/README.md`

- Meta description: what this folder is FOR (not current status)

### `docs/project/roadmap.md`

- Strategic planning, quarterly goals, major initiatives (planning phase)

### `docs/project/tasks.md`

- Approved work queue, concrete tasks ready to start (approval checkpoint)
- Features, bugs, enhancements, tech debt awaiting execution

### `docs/project/worklog.md`

- Daily execution, session-by-session progress, blockers, next steps
- Tracks progress between PRs (multi-day work, interruptions, decisions-in-progress)

### `docs/project/changelog.md`

- Release history, shipped features, breaking changes (after PR merge and delivery)

## Content Type Mapping

| What to Document                  | Which File                | Example                                                      |
| --------------------------------- | ------------------------- | ------------------------------------------------------------ |
| **Project description**           | `README.md`               | "Automated multilingual manual generation pipeline" |
| **Documentation structure**       | `docs/README.md`          | "Complete directory tree showing all docs folders"           |
| **What software does (overview)** | `documentation.md`        | "High-level overview: features organized by function" |
| **Technology choice & rationale** | `architecture.md`         | "Chose OpenAI over DeepL because..." |
| **Component architecture**        | `architecture.md`         | "TranslationService handles all translation operations" |
| **Data pipeline flow**            | `architecture.md`         | "Pipeline: Git pull → Copy → Translate → Merge → PDF" |
| **Installation prerequisites**    | `installation.md`         | "Python 3.13+, Poetry, Pandoc, LaTeX, OpenAI API key"        |
| **Setup steps**                   | `installation.md`         | "1. Clone repo, 2. Install Poetry, 3. Run poetry install..." |
| **Configuration**                 | `usage.md`                | "config.json structure, environment variables, settings"     |
| **How to run/use**                | `usage.md`                | "poetry shell && python scripts/run.py"      |
| **LLM behavioral instructions**   | `AGENTS.md`               | "Project workflow awareness, mandatory constraints" |
| **Test strategy**                 | `testing.md`              | "Current coverage: 18%, target: 70%, pytest with markers"    |
| **Strategic planning**            | `project/roadmap.md`      | "Q2 2025: 70% coverage, Q3 2025: Performance optimization"   |
| **Approved work queue**           | `project/tasks.md`        | "Dark Mode Toggle - Approved 2025-01-08 (ready to start)"   |
| **Work sessions & blockers**      | `project/worklog.md`      | "2025-01-08: Implemented toggle, stuck on Safari CSS vars"   |
| **Current progress**              | `project/worklog.md`      | "Active: Dark mode (50%), Blocker: CSS naming convention"    |
| **Release history**               | `project/changelog.md`    | "v1.0.0 - Initial release with translation pipeline"         |
| **Feature deep-dive**             | `features/[name].md`      | "How the translation pipeline works end-to-end" |
| **Core concepts**                 | `fundamentals/[topic].md` | "Understanding manual types: Superadmin, Technician, User" |

## What to Include in Documentation

- **Why** - Rationale for decisions, alternatives considered, trade-offs
- **What** - Purpose and responsibilities of components
- **How (High-Level)** - Process overview, data flow, interactions
- **Structure** - Module organization, major classes, relationships
- **Standards** - Naming conventions, file formats, configuration
- **Decisions** - What was decided and why (for reconstruction)

## Code (docstrings, comments) - Implementation Details

**Focus:** Implementation details for developers **working with the code**

| Content Type       | Location      | Example                                                      |
| ------------------ | ------------- | ------------------------------------------------------------ |
| **Implementation** | Code comments | `# Use regex r'^(#+)' to match headers, then prepend '#'`    |
| **API Reference**  | Docstrings    | Function parameters, return types, exceptions                |
| **Edge Cases**     | Code comments | `# Handle empty glossary: skip injection if file missing`    |
| **Error Handling** | Code comments | `# Retry 3 times with exponential backoff on network errors` |
| **Complex Logic**  | code comments | `# Adjust paths: replace 'Wiki/' with 'Translations/de/'`    |

---

**Last Updated:** 2025-11-08
