# aiDocs

A **documentation and coding workflow framework** for AI-assisted development.

For developers using AI coding assistants. Works with any language, platform, or AI tool.

- **10-step coding workflow** — Structured process from feature branch to merged PR with clear LLM instructions
- **Information minimalism** — Only document what a seasoned developer or LLM couldn't figure out from the code alone
- **Just-in-time information** — Read indexes upfront, load details only when needed
- **3 documentation levels**
  - **Code** — Intent, rationale, edge cases (docstrings, inline "why" comments)
  - **/docs** — Developer operations (build, test, run, release)
  - **Wiki** — How the software works (features, architecture, domain concepts)
- **Skills** — Lightweight auto-triggered and slash-command actions for Claude Code (job runners, architecture enforcement, documentation rules)
- **Sub-agents** — Specialized instruction sets for testing, documentation, and validation
- **Jobs registry** — Central list of runnable tasks with triggers for when to run each
- **AI-tool independent** — One workflow for Claude, Copilot, Cursor, and Codex via a single [AGENTS.md](docs/AGENTS.md)


## Quick Start

1. Copy the `docs/` folder to your project
2. Copy `.claude/skills/` to your project (for Claude Code users)
3. Configure `docs/README.md` with project info and wiki location
4. Create `development.md`, `installation.md`, etc. for your platform
5. Rename `.template` files in `.claude/skills/` to `SKILL.md` and customize for your project
6. Keep UPPERCASE template files as-is
7. Use wiki for feature documentation

**Claude Code users:** run `/setup` instead of steps 3–7 — it walks through the whole setup in interview form.

**For AI Assistants:** Start at [docs/AGENTS.md](docs/AGENTS.md)

**Full Navigation:** See [docs/INDEX.md](docs/INDEX.md)


## Features

### Skills (Claude Code)

Lightweight instructions in `.claude/skills/` that extend Claude Code with project-specific capabilities:

- **Job skills** — Slash commands (`/setup`, `/validate-docs`) that run tools with one command
- **Convention skills** — Auto-triggered or invokable rules for testing (`/test-runner`), documentation (`/documentation`), and test recommendations (`/test-recommender`)
- **Architecture enforcement** — Auto-triggered skill reads `architecture-rules.md` before writing new code, preventing duplication and layer violations
- **Workflow tracking** — Auto-triggered `coding-workflow` skill creates a task per workflow step and blocks silent step-skipping

Skills coexist with sub-agents: skills handle lightweight auto-triggered actions, sub-agents handle heavy isolated computation. See [subagents/README.md](docs/subagents/README.md) for the distinction.

### Just-in-Time Documentation

Read indexes upfront, read content only when you reach that situation. Documentation is organized by situation, not by hierarchy — `AGENTS.md` routes you to the right file at the right time.

### LLM Coding Workflow

A structured development process designed for AI-assisted coding.

- **10-Step Development Process** — From feature branch to merged PR: implement, test, review, document, ship. Each step has clear LLM behavioral instructions. See [coding-guidelines.template.md](docs/coding-guidelines.template.md). The auto-triggered `coding-workflow` skill tracks progress through the steps.
- **Sub-Agents** — Specialized instruction sets for complex domain-specific tasks. Instead of one general-purpose AI handling everything, sub-agents provide focused expertise (testing, documentation, validation). See [subagents/](docs/subagents/index.md).

### Documentation Levels

| Level     | Contains                                              | Examples                          |
|-----------|-------------------------------------------------------|-----------------------------------|
| **Code**  | Intent, rationale, edge cases                         | Docstrings, inline "why" comments |
| **/docs** | Developer operations, platform guides                 | Build, test, run, release         |
| **Wiki**  | How software functions, architecture, domain concepts | Features, behavior, system design |

- **Information Minimalism** — Before documenting, pass the 3-question test: Would a skilled developer need this? Is it obvious from the code? Does it duplicate existing content? If it fails any question, don't write it. See [INFORMATION_MINIMALISM.md](docs/INFORMATION_MINIMALISM.md).
- **Behavior vs. Platform** — Documentation separates what the software does (cross-platform requirement) from how it's built on a specific platform. Platform-specific quirks are marked with `// PLATFORM:` — everything else is implicitly a requirement for any implementation. See [DOCUMENTATION_GUIDELINES.md](docs/DOCUMENTATION_GUIDELINES.md).

### Jobs Registry

A central registry of runnable tasks — validation, documentation checks — with clear triggers for when to run each. LLMs check [tools/jobs.md](docs/tools/jobs.md) to discover what's available.

### Validation

Two built-in validation agents keep the system healthy:

- `validation-docs` — Structural checks: broken links, orphan pages, stale content, index consistency
- `validation-llm` — Effectiveness test: can a fresh LLM navigate the docs and correctly understand the project?


## Project Structure

```
.claude/
└── skills/                             # Claude Code skills (auto-triggered + slash commands)
    ├── setup/SKILL.md                  # /setup — initial project setup (interview form)
    ├── validate-docs/SKILL.md          # /validate-docs — validate doc structure (forked)
    ├── documentation/SKILL.md          # /documentation — documentation writing rules
    ├── test-runner/SKILL.md.template   # /test-runner — run tests by category
    ├── test-recommender/SKILL.md.template  # /test-recommender — recommend test category
    ├── architecture-rules/SKILL.md.template  # auto-triggered — enforce architecture rules
    └── coding-workflow/SKILL.md.template   # auto-triggered — track the 10-step workflow

docs/
├── AGENTS.md                       # LLM entry point and workflow router
├── coding-guidelines.template.md   # 10-step development process
├── DOCUMENTATION_GUIDELINES.md     # What/where/how much to document
├── INDEX.md                        # Navigation map
├── INFORMATION_MINIMALISM.md       # 3-question test
├── wiki.md                         # Wiki setup and configuration
├── features/                       # Feature documentation
│   └── feature.template.md
├── project/                        # Worklog, changelog, tasks
│   └── changelog.template.md
├── subagents/                      # Specialized AI agents (knowledge reference)
│   ├── validation-docs.md
│   └── validation-llm.md
├── architecture-rules.template.md
├── development.template.md
├── tools/
│   └── jobs.md                     # Runnable jobs registry
```

UPPERCASE = framework files (keep as-is) / lowercase = your project content / `*.template.md` = copy and fill, dropping the `.template` suffix


## License

MIT
