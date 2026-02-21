# aiDocs

A **documentation and coding workflow framework** for AI-assisted development.

For developers using AI coding assistants. Works with any language, platform, or AI tool.

- **11-step coding workflow** — Structured process from feature branch to merged PR with clear LLM instructions
- **Information minimalism** — Only document what a seasoned developer or LLM couldn't figure out from the code alone
- **Just-in-time information** — Read indexes upfront, load details only when needed
- **3 documentation levels**
  - **Code** — Intent, rationale, edge cases (docstrings, inline "why" comments)
  - **/docs** — Developer operations (build, test, run, release)
  - **Wiki** — How the software works (features, architecture, domain concepts)
- **Skills** — Lightweight auto-triggered and slash-command actions for Claude Code (job runners, architecture enforcement, documentation rules)
- **Sub-agents** — Specialized instruction sets for testing, documentation, and validation
- **Code index** — Auto-generated AST-based index of public APIs for fast LLM orientation
- **Code analysis** — Structural health analyzers that flag god classes, layer violations, and complexity issues
- **Jobs registry** — Central list of runnable tasks with triggers for when to run each
- **AI-tool independent** — One workflow for Claude, Copilot, Cursor, and Codex via a single [AGENTS.md](docs/AGENTS.md)


## Quick Start

1. Copy the `docs/` folder to your project
2. Copy `.claude/skills/` to your project (for Claude Code users)
3. Configure `docs/README.md` with project info and wiki location
4. Create `[platform]-development.md`, `[platform]-index.md`, etc. for your platform
5. Rename `.template` files in `.claude/skills/` to `SKILL.md` and customize for your project
6. Keep UPPERCASE template files as-is
7. Use wiki for feature documentation

**For AI Assistants:** Start at [docs/AGENTS.md](docs/AGENTS.md)

**Full Navigation:** See [docs/INDEX.md](docs/INDEX.md)


## Features

### Skills (Claude Code)

Lightweight instructions in `.claude/skills/` that extend Claude Code with project-specific capabilities:

- **Job skills** — Slash commands (`/generate-index`, `/run-analysis`, `/validate-docs`) that run tools with one command
- **Convention skills** — Auto-triggered or invokable rules for testing (`/test-runner`), documentation (`/documentation`), and test recommendations (`/test-recommender`)
- **Architecture enforcement** — Auto-triggered skill reads `[platform]-architecture-rules.md` before writing new code, preventing duplication and layer violations

Skills coexist with sub-agents: skills handle lightweight auto-triggered actions, sub-agents handle heavy isolated computation. See [subagents/README.md](docs/subagents/README.md) for the distinction.

### Just-in-Time Documentation

Read indexes upfront, read content only when you reach that situation. Documentation is organized by situation, not by hierarchy — `AGENTS.md` routes you to the right file at the right time.

### LLM Coding Workflow

A structured development process designed for AI-assisted coding.

- **11-Step Development Process** — From feature branch to merged PR: implement, test, review, document, ship. Each step has clear LLM behavioral instructions. See [CODING_GUIDELINES.md](docs/CODING_GUIDELINES.md).
- **Sub-Agents** — Specialized instruction sets for complex domain-specific tasks. Instead of one general-purpose AI handling everything, sub-agents provide focused expertise (testing, documentation, validation). See [subagents/](docs/subagents/index.md).

### Documentation Levels

| Level     | Contains                                              | Examples                          |
|-----------|-------------------------------------------------------|-----------------------------------|
| **Code**  | Intent, rationale, edge cases                         | Docstrings, inline "why" comments |
| **/docs** | Developer operations, platform guides                 | Build, test, run, release         |
| **Wiki**  | How software functions, architecture, domain concepts | Features, behavior, system design |

- **Information Minimalism** — Before documenting, pass the 3-question test: Would a skilled developer need this? Is it obvious from the code? Does it duplicate existing content? If it fails any question, don't write it. See [INFORMATION_MINIMALISM.md](docs/INFORMATION_MINIMALISM.md).
- **Behavior vs. Platform** — Documentation separates what the software does (cross-platform requirement) from how it's built on a specific platform. Platform-specific quirks are marked with `// PLATFORM:` — everything else is implicitly a requirement for any implementation. See [DOCUMENTATION_GUIDELINES.md](docs/DOCUMENTATION_GUIDELINES.md).

### Code Analysis

Python analyzers consume the same AST declarations as the code index and produce structured findings reports. An LLM subagent (`CODE_ANALYSIS`) then interprets those findings qualitatively — hybrid approach: deterministic metrics from Python, judgment from LLM.

- **Structural health analyzer** — 8 checks: god classes, parameter bloat, data class explosion, fat/thin interfaces, layer violations, documentation gaps, package imbalance
- **Configurable thresholds** — All defaults can be overridden in `aidocs.yaml`
- **Extensible** — Add new analyzers by implementing the `Analyzer` ABC

See [tools/code-index/README.md](docs/tools/code-index/README.md) for analyzer details.

### Jobs Registry

A central registry of all runnable tasks — code generation, analysis, validation — with clear triggers for when to run each. LLMs check [tools/JOBS.md](docs/tools/JOBS.md) to discover what's available.

### Validation

Two built-in validation agents keep the system healthy:

- `VALIDATION_DOCS` — Structural checks: broken links, orphan pages, stale content, index consistency
- `VALIDATION_LLM` — Effectiveness test: can a fresh LLM navigate the docs and correctly understand the project?


## Project Structure

```
.claude/
└── skills/                             # Claude Code skills (auto-triggered + slash commands)
    ├── generate-index/SKILL.md         # /generate-index — regenerate code-index
    ├── run-analysis/SKILL.md           # /run-analysis — run structural health analyzer
    ├── review-analysis/SKILL.md        # /review-analysis — classify findings (forked)
    ├── fix-analysis/SKILL.md           # /fix-analysis — fix mechanical findings (forked)
    ├── validate-docs/SKILL.md          # /validate-docs — validate doc structure (forked)
    ├── documentation/SKILL.md          # /documentation — documentation writing rules
    ├── test-runner/SKILL.md.template   # /test-runner — run tests by category
    ├── test-recommender/SKILL.md.template  # /test-recommender — recommend test category
    └── architecture-rules/SKILL.md.template  # auto-triggered — enforce architecture rules

docs/
├── AGENTS.md                       # LLM entry point and workflow router
├── CODING_GUIDELINES.md            # 11-step development process
├── DOCUMENTATION_GUIDELINES.md     # What/where/how much to document
├── INDEX.md                        # Navigation map
├── INFORMATION_MINIMALISM.md       # 3-question test
├── wiki.md                         # Wiki setup and configuration
├── features/                       # Feature documentation
│   └── feature.template.md
├── project/                        # Worklog, changelog, tasks
│   └── changelog.template.md
├── subagents/                      # Specialized AI agents (knowledge reference)
│   ├── CODE_ANALYSIS.md
│   ├── VALIDATION_DOCS.md
│   └── VALIDATION_LLM.md
├── tools/
│   ├── JOBS.md                     # Runnable jobs registry
│   └── code-index/                 # AST-based code index + analyzers
│       ├── generate.py
│       ├── analyze.py
│       ├── pipeline.py
│       ├── generator.py
│       ├── grouping.py
│       ├── analyzers/
│       └── languages/
├── platform-architecture-rules.template.md
├── platform-development.template.md
└── platform-index.template.md
aidocs.yaml.template                # Code-index config template
```

UPPERCASE = framework files (keep as-is) / lowercase = your project content


## License

MIT
