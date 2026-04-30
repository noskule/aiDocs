# Documentation Index

Quick navigation to all docs. Read only what you need, when you need it.


## LLM Entry Point

**[AGENTS.md](AGENTS.md)** - Start here
- Navigation
- Situational References
- Skills (lightweight auto-triggered and slash-command actions)
- Sub-Agents (specialized task agents in `docs/subagents/`)
- Workflow Overview


## Development Process

**[CODING_GUIDELINES.md](CODING_GUIDELINES.md)** - Development workflow
- Development Workflow (10 steps)
- Data Persistence

**[DOCUMENTATION_GUIDELINES.md](DOCUMENTATION_GUIDELINES.md)** - What/where to document
- Information Minimalism Test
- Documentation Levels (Code, /docs, Wiki)
- Diagrams (Mermaid conventions, when to use, placement)
- Documenting in Code
- Documenting in /docs (File Tree)
- Documenting in Wiki


## Skills

**`docs/skills/`** — LLM-agnostic skill instructions (any LLM reads directly)

| File | Purpose |
|------|---------|
| [`validate-docs.md`](skills/validate-docs.md) | Documentation validation steps |
| [`documentation.md`](skills/documentation.md) | Writing rules and placement |
| [`architecture-rules.md`](skills/architecture-rules.md) | Layer boundaries and reuse enforcement |
| [`test-runner.template.md`](skills/test-runner.template.md) | Test execution (template) |
| [`test-recommender.template.md`](skills/test-recommender.template.md) | Test category recommendation (template) |


## Reference

**[subagents/README.md](subagents/README.md)** - Creating specialized AI agents and skills
- File Structure
- The Cardinal Rule (wrappers point to docs)
- Skills vs. Sub-Agents
- Integrating with AGENTS.md

**[INFORMATION_MINIMALISM.md](INFORMATION_MINIMALISM.md)** - 3-question test
- The Test (3 questions)
- Examples
- When to Document


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

**[issue-tracker.md](issue-tracker.md)** - GitHub Issues and Projects v2
- Conventions (types, labels, sub-issues, project, estimates)
- Issue Structure (required sections per type)
- Wiki Mapping

**[changelog.md](changelog.md)** - Release history → GitHub Releases (template: `changelog.template.md`)


## Wiki (External)

**Wiki** - What software does
- Fundamentals (domain concepts)
- Architecture (system design)
- Features (user-facing functionality)
- Devices (hardware-specific findings)


**Maintain this index:** When adding/removing sections, update this file.
