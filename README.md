# aiDocs

A **documentation and coding workflow framework** for AI-assisted development.

AI coding assistants produce inconsistent results when documentation is bloated, scattered, or structured for human-only consumption. aiDocs provides a minimal, navigable structure that both LLMs and developers can work with effectively.


## Principle: Just-in-Time

Read indexes upfront, read content only when you reach that situation. Documentation is organized by situation, not by hierarchy — `AGENTS.md` routes you to the right file at the right time.


## Pillar 1: LLM Coding Workflow

A structured development process designed for AI-assisted coding.

**11-Step Development Process** — From feature branch to merged PR: implement, test, review, document, ship. Each step has clear LLM behavioral instructions. See [CODING_GUIDELINES.md](docs/CODING_GUIDELINES.md).

**Sub-Agents** — Specialized instruction sets for complex domain-specific tasks. Instead of one general-purpose AI handling everything, sub-agents provide focused expertise (testing, documentation, validation). See [subagents/](docs/subagents/index.md).


## Pillar 2: Documentation

What to document, where, and how much.

**3 Documentation Levels:**

| Level | Contains | Examples |
|-------|----------|----------|
| **Code** | Intent, rationale, edge cases | Docstrings, inline "why" comments |
| **/docs** | Developer operations, platform guides | Build, test, run, release |
| **Wiki** | How software functions, architecture, domain concepts | Features, behavior, system design |

**Information Minimalism** — Before documenting, pass the 3-question test: Would a skilled developer need this? Is it obvious from the code? Does it duplicate existing content? If it fails any question, don't write it. See [INFORMATION_MINIMALISM.md](docs/INFORMATION_MINIMALISM.md).

**Behavior vs. Platform** — Documentation separates what the software does (cross-platform requirement) from how it's built on a specific platform. Platform-specific quirks are marked with `// PLATFORM:` — everything else is implicitly a requirement for any implementation. See [DOCUMENTATION_GUIDELINES.md](docs/DOCUMENTATION_GUIDELINES.md).


## Structure and Conventions

**AI-Tool Independent** — Entry points for Claude, Copilot, Cursor, and Codex all funnel into a single [AGENTS.md](docs/AGENTS.md). Write the workflow once, every AI tool follows it.

**Template Convention** — UPPERCASE files (`AGENTS.md`, `CODING_GUIDELINES.md`) are framework files that stay as-is. Lowercase files (`android-development.md`) are project-specific content you create. Copy the `docs/` folder to any project and start filling in.

**Validation** — Two built-in validation agents keep the system healthy:
- `VALIDATION_DOCS` — Structural checks: broken links, orphan pages, stale content, index consistency
- `VALIDATION_LLM` — Effectiveness test: can a fresh LLM navigate the docs and correctly understand the project?


## Quick Start

1. Copy the `docs/` folder to your project
2. Configure `docs/README.md` with project info and wiki location
3. Create `[platform]-development.md`, `[platform]-index.md`, etc. for your platform
4. Keep UPPERCASE template files as-is
5. Use wiki for feature documentation

**For AI Assistants:** Start at [docs/AGENTS.md](docs/AGENTS.md)

**Full Navigation:** See [docs/INDEX.md](docs/INDEX.md)


## License

MIT
