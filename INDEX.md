# Documentation Index

Quick navigation to all docs. Read only what you need, when you need it.


## LLM Entry Point

**[AGENTS.md](AGENTS.md)** - Start here
- Situational References
- Skills and Agents (available actions)


## Skills & Agents

Full instructions live in `docs/claude/` (copy to `.claude/` at project root).

**Skills** (`claude/skills/*/SKILL.md`):

| Skill | Purpose |
|-------|---------|
| `coding-workflow` | 10-step development workflow (auto-triggered) |
| `architecture-rules` | Layer boundaries and reuse enforcement (auto-triggered) |
| `documentation` | Writing rules and placement |
| `validate-docs` | Documentation validation (forked) |
| `test-runner` | Test execution (template) |
| `test-recommender` | Test category recommendation (template) |

**Agents** (`claude/agents/*.md`):

| Agent | Purpose |
|-------|---------|
| `validation-docs` | Documentation structure validation |
| `validation-llm` | LLM documentation effectiveness test |
| `project-manager` | Issue management (template) |


## Reference

**[DOCUMENTATION_GUIDELINES.md](DOCUMENTATION_GUIDELINES.md)** - Documentation standards reference
- What to Document / What to Skip
- Documentation Levels (Code, /docs, Wiki)
- Wiki structure (behavior first, then platform)
- Diagrams (Mermaid conventions)
- Platform-Specific Marker

**[INFORMATION_MINIMALISM.md](INFORMATION_MINIMALISM.md)** - 3-question test
- The Test (3 questions)
- Examples
- When to Document

**[creating-agents.md](creating-agents.md)** - How to create skills and agents
- Skills vs. Agents decision
- File format and frontmatter
- Step-by-step creation guide


## Design

**`design-sync.template.md`** - Bidirectional design ↔ code sync (template)
- File Map (Pencil frames → source files)
- Token Translation Tables (colors, typography, shapes)
- Component Mapping (frame → UI element parameters)
- Sync Rules (design→code, code→design, tokens)


## Tools

**[tools/JOBS.md](tools/JOBS.md)** - Runnable jobs registry
- Available jobs with commands and triggers
- When to run each job


## Platform Specific

**`[platform]-index.md`** - Platform documentation index (sections per file)

**`[platform]-installation.md`** - First time setup

**`[platform]-architecture-rules.md`** - Enforceable design principles
- Layer Boundaries, Reuse Rules, Anti-Patterns, Extension Points

**`[platform]-development.md`** - Writing code
- Tech Stack, Architecture, Code Patterns, File Organization
- Data Retention, Build Commands, Common Tasks

**`[platform]-testing.md`** - Running/writing tests

**`[platform]-release.md`** - Publishing


## Project Management

**[issue-tracker.md](issue-tracker.md)** - Issue tracker conventions
- Conventions (types, labels, sub-issues, project, estimates)
- Estimate Scale

**[changelog.md](changelog.md)** - Release history (template: `changelog.template.md`)


## Wiki (External)

**Wiki** - What software does
- Fundamentals (domain concepts)
- Architecture (system design)
- Features (user-facing functionality)


**Maintain this index:** When adding/removing sections, update this file.
