# Coding and Documentation Guidelines

## Core Principle

The primary goal of this this documentation guideline is to enable a seasoned developer to reconstruct the project as quickly as possible without needing tribal knowledge.

**Document what a seasoned developer would want to know - skip trivial fixes.**

Document anything that would take measurable time for an experienced engineer to rediscover — configuration logic, architectural decisions, workflow setup — but skip details that are obvious or easily re-derived (such as precise library versions or trivial syntax).

## When to Document

### ✅ Requires Documentation

- **Architectural/structural changes** - New modules, refactoring, async conversions, splitting modules
- **Technology/library decisions** - Choosing OpenAI vs DeepL, selecting libraries, switching dependencies
- **Performance optimizations** - Refactoring for efficiency, caching strategies
- **Security vulnerabilities and fixes** - Any security-related changes
- **Complex logic bugs** - If the bug was hard to figure out or fix
- **Database/schema changes** - Any data structure modifications
- **New features or behavior changes** - Anything that changes user-facing behavior
- **Configuration changes** - New config options, changed defaults

### ❌ Does NOT Require Documentation

- **Typo fixes** - Error messages, comments, variable names
- **Simple bug fixes** - Off-by-one errors, null checks, obvious logic fixes
- **Code formatting** - Linting, whitespace, style adjustments
- **Trivial refactoring** - Renaming variables, extracting simple functions (no behavior change)

### Examples

| Change                                        | Document? | Why                            |
| --------------------------------------------- | --------- | ------------------------------ |
| Fix typo in error message                     | ❌ No      | Trivial                        |
| Fix off-by-one error in loop                  | ❌ No      | Simple bug                     |
| Fix logic bug that changes behavior (complex) | ✅ Yes     | Complex, affects understanding |
| Fix security vulnerability                    | ✅ Yes     | Important for security history |
| Refactor function to be more efficient        | ✅ Yes     | Performance decision           |
| Switching from OpenAI to DeepL                | ✅ Yes     | Architectural decision         |
| Adding a new caching layer                    | ✅ Yes     | Structural change              |
| Changing function from sync to async          | ✅ Yes     | Affects usage                  |
| Splitting large module into smaller ones      | ✅ Yes     | Structural reorganization      |

## What Goes Where

### Documentation (docs/) - Information to Rebuild the Project

**Focus:** Information needed to **rebuild the project from scratch**

**Target Audience:** Seasoned developer new to the project

#### Complete Documentation Structure

```
ROOT/
├── README.md                     # Main entry point, project overview
│
└── docs/
    ├── README.md                 # Documentation structure guide
    ├── AGENTS.md                 # LLM behavioral instructions
    ├── INSTALLATION.md           # Prerequisites, setup, troubleshooting
    ├── ARCHITECTURE.md           # System design, tech stack, decisions
    ├── USAGE.md                  # How to use, configuration, workflows
    ├── CODING_GUIDELINES.md      # This file
    │
    ├── features/                 # Feature documentation
    │   └── [feature].md          # Individual feature deep-dives
    │
    ├── fundamentals/             # Core concepts and principles
    │   └── [topic].md            # Fundamental topics explained
    │
    ├── testing/                  # Testing documentation
    │   ├── README.md             # Testing overview and status
    │   ├── QUICK_START.md        # How to run/write tests
    │   └── EVALUATION.md         # Coverage analysis and roadmap
    │
    └── project/                  # Project management
        ├── README.md             # Project status and metrics
        ├── ROADMAP.md            # Milestones and timeline
        └── CHANGELOG.md          # Version history
```

#### Content Ownership by File

##### `README.md` (Root)

- **Project overview** - What the project does (brief, compelling description)
- **Key features** - Main capabilities and benefits
- **Documentation structure** - Complete directory tree showing all docs
- **Content ownership table** - What content lives where (single source of truth)
- **Documentation principles** - Rules for maintaining docs
- **Getting help** - Quick links to common questions/docs
- **Not included:** Installation steps (→ INSTALLATION.md), detailed architecture (→ ARCHITECTURE.md), usage details (→ USAGE.md)

##### `docs/AGENTS.md`

- **Why in docs:** Part of reusable documentation template
- **Audience:** AI coding assistants (LLM-addressed)
- **Contains:**
  - Mandatory workflow for AI assistants (check → code → test → report → wait)
  - Critical constraints (never commit without tests, never proceed without approval)
  - LLM-specific behaviors (report and wait pattern, include summarized prompts)
  - References to CODING_GUIDELINES.md and ARCHITECTURE.md (no duplication)
- **Note:** Does NOT duplicate content from other docs, only LLM interaction patterns

##### `docs/INSTALLATION.md`

- **Prerequisites** - Required software, versions, external services
- **Installation steps** - Platform-specific setup (Windows/Linux/Mac)
- **Configuration** - Environment variables, config files, API keys
- **Verification** - How to test installation succeeded
- **Troubleshooting** - Common issues and solutions
- **Updating** - How to update dependencies and project

##### `docs/ARCHITECTURE.md`

- **Technology Stack** - All dependencies, versions, rationale
- **Technology Decisions** - Why OpenAI over DeepL, why Pandoc+LaTeX, etc.
- **System Architecture** - Components, connections, responsibilities
- **Data Flow** - Pipeline stages, transformations, I/O
- **Module Organization** - 11 modules, their purposes, relationships
- **Data Structures** - Directory layout, file formats, naming conventions
- **Business Rules** - What to skip, how to process, configuration logic
- **Algorithm Pseudocode** - High-level process flows (not implementation)
- **Git Versioning Workflow** - Tag-based versioning, release process
- **Design Decisions** - Architectural choices and trade-offs

##### `docs/USAGE.md`

- **Running the application** - Command-line usage, GUI options
- **Configuration** - config.json structure, key settings
- **Common workflows** - Typical usage patterns
- **Key files** - Important files and their purposes
- **File naming conventions** - Generated file formats
- **Environment variables** - Required and optional vars

##### `docs/CODING_GUIDELINES.md`

- **When to document** - What requires docs, what doesn't
- **What goes where** - This breakdown
- **Documentation workflow** - When to update, PR requirements
- **Code examples** - Good and bad patterns

##### `docs/features/`

- **Individual feature deep-dives** - Detailed explanation of specific features
- **Feature architecture** - How a feature is implemented across modules
- **Feature usage** - Advanced use cases and examples
- **Feature decisions** - Why this feature was designed this way
- **Examples:** `translation-pipeline.md`, `pdf-generation.md`, `glossary-system.md`

##### `docs/fundamentals/`

- **Core concepts** - Essential concepts developers need to understand
- **Design principles** - Guiding principles of the project
- **Key abstractions** - Important abstractions and patterns used
- **Domain knowledge** - Business domain explanations
- **Examples:** `manual-types.md`, `language-handling.md`, `wiki-structure.md`

##### `docs/testing/README.md`

- **Testing overview** - Current status, coverage metrics
- **Test structure** - How tests are organized
- **Quick commands** - Most common test operations

##### `docs/testing/QUICK_START.md`

- **Running tests** - All test execution methods
- **Writing tests** - How to add new tests
- **Test markers** - Available markers and usage
- **Debugging tests** - Common issues and solutions

##### `docs/testing/EVALUATION.md`

- **Coverage analysis** - Module-by-module breakdown
- **Testing roadmap** - What needs tests, priorities
- **Coverage goals** - Target percentages and timelines

##### `docs/project/README.md`

- **Project overview** - Current status and phase
- **Metrics** - Code stats, activity, dependencies
- **Team** - Roles and responsibilities
- **Key decisions** - Major project decisions log

##### `docs/project/ROADMAP.md`

- **Milestones** - Major project phases
- **Timeline** - Expected completion dates
- **Future features** - Planned enhancements
- **Technical debt** - Known issues to address

##### `docs/project/CHANGELOG.md`

- **Version history** - Release notes by version
- **Breaking changes** - Migration guides
- **Bug fixes** - Significant fixes
- **New features** - What was added when

#### Content Type Mapping

| What to Document                  | Which File                | Example                                                      |
| --------------------------------- | ------------------------- | ------------------------------------------------------------ |
| **Project description**           | `README.md`               | "Automated multilingual manual generation pipeline for GG+ software and hardware products" |
| **Documentation structure**       | `README.md`               | "Complete directory tree showing all docs folders"           |
| **Content ownership rules**       | `README.md`               | "Technology Stack → ARCHITECTURE.md, Installation → INSTALLATION.md" |
| **Technology choice & rationale** | `ARCHITECTURE.md`         | "Chose OpenAI over DeepL because it handles markdown formatting better and provides better context awareness" |
| **Component architecture**        | `ARCHITECTURE.md`         | "TranslationService handles all translation operations using configurable engines (OpenAI/DeepL)" |
| **Data pipeline flow**            | `ARCHITECTURE.md`         | "Pipeline: Git pull wiki → Copy to de/ → Translate to en/fr/it → Merge per MATRIX.md → Generate PDFs" |
| **Module structure**              | `ARCHITECTURE.md`         | "11 modules: manual_generator (orchestrator), translator (AI translation), git_connector (wiki sync)..." |
| **File/data formats**             | `ARCHITECTURE.md`         | "Manual naming: `[product]_[version]_[date]_[lang]_[role].pdf`" |
| **Business/processing rules**     | `ARCHITECTURE.md`         | "Skip folders: `.git`, `.attachments`; Translation uses GLOSSARY.md for terminology" |
| **High-level algorithms**         | `ARCHITECTURE.md`         | "Header adjustment: read file → detect headers → increment level +1 → write back" |
| **Git versioning process**        | `ARCHITECTURE.md`         | "Version controlled by git tags, auto-increment between releases" |
| **Installation prerequisites**    | `INSTALLATION.md`         | "Python 3.13+, Poetry, Pandoc, LaTeX, OpenAI API key"        |
| **Setup steps**                   | `INSTALLATION.md`         | "1. Clone repo, 2. Install Poetry, 3. Run poetry install..." |
| **Configuration**                 | `USAGE.md`                | "config.json structure, environment variables, settings"     |
| **How to run/use**                | `USAGE.md`                | "poetry shell && python scripts/run_ManualGenerator.py"      |
| **LLM behavioral instructions**   | `docs/AGENTS.md`          | "Mandatory workflow for AI assistants: check → code → test → report → wait for approval" |
| **Test strategy**                 | `testing/README.md`       | "Current coverage: 18%, target: 70%, pytest with markers"    |
| **How to run tests**              | `testing/QUICK_START.md`  | "poetry run pytest --cov=src"                                |
| **Coverage details**              | `testing/EVALUATION.md`   | "Module-by-module breakdown, testing roadmap"                |
| **Project status**                | `project/README.md`       | "Phase 2: Quality & Testing, active development"             |
| **Roadmap/milestones**            | `project/ROADMAP.md`      | "Q1 2025: 70% coverage, Q2 2025: CI/CD pipeline"             |
| **Release history**               | `project/CHANGELOG.md`    | "v1.0.0 - Initial release with translation pipeline"         |
| **Feature deep-dive**             | `features/[name].md`      | "How the translation pipeline works end-to-end with glossary integration" |
| **Core concepts**                 | `fundamentals/[topic].md` | "Understanding manual types: Superadmin, Technician, User roles" |

**What to Include in Documentation:**

- **Why** - Rationale for decisions, alternatives considered, trade-offs
- **What** - Purpose and responsibilities of components
- **How (High-Level)** - Process overview, data flow, interactions
- **Structure** - Module organization, major classes, relationships
- **Standards** - Naming conventions, file formats, configuration
- **Decisions** - What was decided and why (for reconstruction)

### Code (docstrings, comments) - Implementation Details

**Focus:** Implementation details for developers **working with the code**

**Target Audience:** Developer modifying this specific code

| Content Type       | Location      | Example                                                      |
| ------------------ | ------------- | ------------------------------------------------------------ |
| **Implementation** | Code comments | `# Use regex r'^(#+)' to match headers, then prepend '#'`    |
| **API Reference**  | Docstrings    | Function parameters, return types, exceptions                |
| **Edge Cases**     | Code comments | `# Handle empty glossary: skip injection if file missing`    |
| **Error Handling** | Code comments | `# Retry 3 times with exponential backoff on network errors` |
| **Complex Logic**  | Code comments | `# Adjust paths: replace 'Wiki/' with 'Translations/de/'`    |

**What to Include:**

- **How (Implementation)** - Specific algorithms, regex patterns, loop logic
- **API Contracts** - Function signatures, parameters, return values
- **Gotchas** - Edge cases, special handling, workarounds
- **Context** - Why this specific code pattern, tricky bits explained

## Development Workflow

### Complete Feature Development Process

When implementing new features or making significant changes, follow this workflow:

#### 1. **Create Feature Branch**

```bash
git checkout -b feature/descriptive-name
```

#### 2. **Implement Code**

- Write the feature/fix implementation
- Follow existing code patterns and project conventions
- Keep changes focused and atomic

#### 3. **Write Tests**

**Test Coverage Requirements:**

- **Use common sense, risk-driven approach** - Not everything needs exhaustive tests
- **Consult "When to Document"** - If it requires documentation, it requires tests
- **Consult "Core Principle"** - Would a seasoned developer need tests to understand this?

**What Requires Tests:**

- ✅ New features - Core functionality must be tested
- ✅ Bug fixes (complex) - Test the fix and prevent regression
- ✅ Refactoring - Ensure behavior hasn't changed
- ✅ Public APIs - All public interfaces need tests
- ❌ Trivial changes - Typos, comments, simple formatting
- ❌ Documentation-only changes - No code tests needed

**Test Quality:**

- Focus on critical paths and edge cases
- Risk-driven: More critical code = more thorough tests
- Tests should be maintainable and clear

#### 4. **Run Tests**

```bash
poetry run pytest
poetry run pytest --cov=src --cov-report=html
```

Verify all tests pass and coverage is appropriate for the risk level.

#### 5. **Report to User for Review**

**LLM Behavior:** Inform the user that code and tests are ready:

```
✅ Code implemented: [brief description]
✅ Tests written: [test coverage summary]
✅ All tests passing: [test results]

Ready for your review and testing. Please verify functionality.
```

#### 6. **User Reviews and Tests**

- User manually tests the functionality
- User reviews code quality and approach
- User provides feedback or approval

#### 7. **Write Documentation** (After User Approval)

**Only after user confirms the implementation is correct:**

- Update relevant documentation (see "Where to Update" below)
- Add feature documentation if complex (see `docs/features/`)
- Include **summarized prompts** used during development
- Update CHANGELOG.md with changes
- Update "Last Updated" dates

#### 8. **Create Pull Request**

**LLM Behavior:** Create PR using GitHub CLI:

```bash
gh pr create --title "Feature: descriptive title" --body "$(cat <<'EOF'
## Summary
- [What was implemented]
- [Key changes]

## Testing
- [Tests added]
- [Test results]

## Documentation
- [Docs updated]

## Prompts Used
- [Summarized prompts that led to this implementation]

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

#### 9. **User Merges PR**

- User reviews PR on GitHub
- User merges when satisfied
- **User informs LLM:** "PR merged, continue"

#### 10. **Continue**

- LLM can proceed with next tasks
- Branch is merged and cleaned up

------

### Documentation Updates During Development

### Where to Update

| Change Type              | Update These Docs                                            |
| ------------------------ | ------------------------------------------------------------ |
| New feature              | `ARCHITECTURE.md` (component), `USAGE.md` (how to use), `CHANGELOG.md` (release notes), optionally `features/[name].md` (deep-dive) |
| Architecture change      | `ARCHITECTURE.md` (design section), `CHANGELOG.md` if breaking |
| Bug fix (complex)        | `ARCHITECTURE.md` (if design flaw), `CHANGELOG.md`           |
| Performance optimization | `ARCHITECTURE.md` (decision rationale)                       |
| New dependency           | `ARCHITECTURE.md` (tech stack + why), `INSTALLATION.md` (setup) |
| Config option            | `USAGE.md` (configuration section), `ARCHITECTURE.md` (if affects design) |
| Breaking change          | `CHANGELOG.md` (migration guide), relevant doc with new behavior |
| Complex feature          | `features/[feature].md` (detailed explanation of how it works across modules) |
| New core concept         | `fundamentals/[concept].md` (explain the concept, why it matters, how it's used) |

### Pull Request Requirements

**All PRs must follow the "Complete Feature Development Process" above.**

**PRs must include:**

- ✅ Code changes (implemented and reviewed)
- ✅ Tests for new functionality (all passing)
- ✅ Updated documentation (if required by "When to Document" guidelines)
- ✅ Summarized prompts used during development (in PR description)
- ✅ Updated "Last Updated" dates

**PRs will be rejected if:**

- ❌ New features lack tests (unless trivial per "When to Document")
- ❌ Tests are not passing
- ❌ Significant changes lack documentation updates
- ❌ Architecture changes not explained in ARCHITECTURE.md
- ❌ Breaking changes not documented in CHANGELOG.md
- ❌ Code not reviewed by user before PR creation

------

**Last Updated:** 2025-11-06 **Maintained By:** Project Team