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
- **Sub-agents** — Specialized instruction sets for issue writing, code analysis, and documentation validation
- **Jobs registry** — Central list of runnable tasks with triggers for when to run each
- **AI-tool independent** — One workflow for Claude, Copilot, Cursor, and Codex via a single [AGENTS.md](docs/AGENTS.md)


## Quick Start

### Install

Works in fresh and existing projects — installs are **additive**, nothing that already exists gets overwritten.

1. Copy the `docs/` folder into your project
2. Copy the `.claude/` content into your project's `.claude/` (only add files that don't exist yet)
3. Run `/setup` — it walks through the rest in interview form: project info, template instantiation, skill activation, and the version stamp (`docs/.aidocs-version`)

Without Claude Code, do step 3 manually: configure `docs/README.md`, create `development.md` / `installation.md` etc. from the templates, rename `.template` files, keep UPPERCASE files as-is.

### Update

Run `/update-aidocs` — it diffs upstream against your version stamp and applies only upstream-owned changes: UPPERCASE standard files and `*.template.md` get updated, your filled copies and project files are never touched, and anything you modified is shown as a conflict before it's touched.

**For AI Assistants:** Start at [docs/AGENTS.md](docs/AGENTS.md)

**Full Navigation:** See [docs/INDEX.md](docs/INDEX.md)


## Features

### Skills (Claude Code)

Lightweight instructions in `.claude/skills/` that extend Claude Code with project-specific capabilities:

- **Job skills** — Slash commands (`/setup`, `/update-aidocs`, `/validate-docs`) that run tools with one command
- **Convention skills** — Auto-triggered or invokable rules for testing (`/test-runner`), documentation (`/documentation`), and test recommendations (`/test-recommender`)
- **Architecture enforcement** — Auto-triggered skill reads `architecture-rules.md` before writing new code, preventing duplication and layer violations
- **Workflow tracking** — Auto-triggered `coding-workflow` skill creates a task per workflow step and blocks silent step-skipping

Skills coexist with agents: skills handle lightweight auto-triggered actions, agents handle heavy isolated computation. See [CREATING_AGENTS.md](docs/CREATING_AGENTS.md) for the distinction.

### Just-in-Time Documentation

Read indexes upfront, read content only when you reach that situation. Documentation is organized by situation, not by hierarchy — `AGENTS.md` routes you to the right file at the right time.

### LLM Coding Workflow

A structured development process designed for AI-assisted coding.

- **10-Step Development Process** — From feature branch to merged PR: implement, test, review, document, ship. Each step has clear LLM behavioral instructions. See [coding-guidelines.template.md](docs/coding-guidelines.template.md). The auto-triggered `coding-workflow` skill tracks progress through the steps.
- **Agents** — Specialized instruction sets for complex domain-specific tasks. Instead of one general-purpose AI handling everything, agents provide focused expertise (issue writing, code analysis, validation). Full instructions live in `.claude/agents/`; the registry [skills-and-agents](docs/skills-and-agents.template.md) routes every AI tool there.

### Documentation Levels

| Level     | Contains                                              | Examples                          |
|-----------|-------------------------------------------------------|-----------------------------------|
| **Code**  | Intent, rationale, edge cases                         | Docstrings, inline "why" comments |
| **/docs** | Developer operations, platform guides                 | Build, test, run, release         |
| **Wiki**  | How software functions, architecture, domain concepts | Features, behavior, system design |

- **Information Minimalism** — Before documenting, pass the 3-question test: Would a skilled developer need this? Is it obvious from the code? Does it duplicate existing content? If it fails any question, don't write it. See [INFORMATION_MINIMALISM.md](docs/INFORMATION_MINIMALISM.md).
- **Behavior vs. Platform** — Documentation separates what the software does (cross-platform requirement) from how it's built on a specific platform. Platform-specific quirks are marked with `// PLATFORM:` — everything else is implicitly a requirement for any implementation. See [DOCUMENTATION_GUIDELINES.md](docs/DOCUMENTATION_GUIDELINES.md).

### Jobs Registry

A central registry of runnable tasks — validation, documentation checks — with clear triggers for when to run each. LLMs check [tools/jobs.md](docs/tools/jobs.template.md) to discover what's available.

### Validation

Mechanical checks run as a script, judgment stays with agents:

- `tools/check-docs.py` — Structural checks on every push: link resolution (case-sensitive), orphan pages, index consistency, agent-wrapper bindings, template hygiene
- `validation-docs` — Judgment checks: duplicated knowledge, stale content, wiki structure
- `validation-llm` — Effectiveness test: can a fresh LLM navigate the docs and correctly understand the project?


## Project Structure

```
.claude/
├── agents/                             # Full agent instructions (auto-discovered by Claude Code,
│   ├── agent-name.template.md          #   readable by any AI tool via the registry)
│   ├── code-analysis.md
│   ├── issue-writer.md
│   ├── validation-docs.md
│   └── validation-llm.md
└── skills/                             # Claude Code skills (auto-triggered + slash commands)
    ├── setup/SKILL.md                  # /setup — initial project setup (interview form)
    ├── update-aidocs/SKILL.md          # /update-aidocs — pull upstream standard updates
    ├── validate-docs/SKILL.md          # /validate-docs — validate doc structure (forked)
    ├── documentation/SKILL.md          # /documentation — documentation writing rules
    ├── test-runner/SKILL.md.template   # /test-runner — run tests by category
    ├── test-recommender/SKILL.md.template  # /test-recommender — recommend test category
    ├── architecture-rules/SKILL.md.template  # auto-triggered — enforce architecture rules
    └── coding-workflow/SKILL.md.template   # auto-triggered — track the 10-step workflow

docs/
├── AGENTS.md                       # LLM entry point and workflow router (fixed)
├── INDEX.md                        # Navigation map (fixed)
├── DOCUMENTATION_GUIDELINES.md     # What/where/how much to document
├── INFORMATION_MINIMALISM.md       # 3-question test
├── coding-guidelines.template.md   # 10-step development process
├── architecture-rules.template.md  # Enforceable design principles
├── development.template.md         # Tech stack, patterns, commands
├── issue-tracker.template.md       # Issue tracker conventions
├── wiki.template.md                # Wiki setup and configuration
├── changelog.template.md           # Release history template
├── design-sync.template.md         # Design ↔ code sync (Pencil)
├── skills-and-agents.template.md   # Registry routing every AI tool to .claude/
├── CREATING_AGENTS.md              # How to create and register skills and agents
└── tools/
    ├── check-docs.py               # Mechanical structural checks (CI + local)
    ├── code-index/                 # Code analysis tooling (feeds code-analysis agent)
    └── jobs.template.md            # Runnable jobs registry

AGENTS.md.template,                         # Root wrappers pointing each AI tool at
CLAUDE.md.template, .cursorrules.template,  # docs/AGENTS.md — rename to activate.
.github/copilot-instructions.md.template    # AGENTS.md (agents.md spec) covers Codex, Cursor & co.
```

UPPERCASE = framework files (keep as-is) / lowercase = your project content / `*.template.md` = copy and fill, dropping the `.template` suffix


## License

MIT
