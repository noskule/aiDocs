# aiDocs

A **documentation and coding workflow framework** for AI-assisted development.

For developers using AI coding assistants. Works with any language, platform, or AI tool.

- **10-step coding workflow** — Auto-triggered skill that guides feature branch to merged PR
- **Information minimalism** — Only document what a seasoned developer or LLM couldn't figure out from the code alone
- **Just-in-time information** — Read indexes upfront, load details only when needed
- **3 documentation levels**
  - **Code** — Intent, rationale, edge cases (docstrings, inline "why" comments)
  - **/docs** — Developer operations (build, test, run, release)
  - **Wiki** — How the software works (features, architecture, domain concepts)
- **Skills** — LLM-agnostic instructions in `skills/`, with Claude Code wrappers in `claude/` for auto-triggering and slash commands
- **Sub-agents** — Specialized instruction sets for testing, documentation, and validation
- **Jobs registry** — Central list of runnable tasks with triggers for when to run each
- **AI-tool independent** — One workflow for Claude, Copilot, Cursor, and Codex via a single [AGENTS.md](AGENTS.md)


## Integration

aiDocs is designed to be added to your project as a **git subtree** under `docs/`:

```bash
# Add aiDocs to your project
git subtree add --prefix=docs https://github.com/noskule/aiDocs.git main --squash

# Update later
git subtree pull --prefix=docs https://github.com/noskule/aiDocs.git main --squash
```

### Setup after adding

1. Copy `docs/CLAUDE.md.template` → `CLAUDE.md` in your project root
2. Copy `docs/claude/skills/` → `.claude/skills/` in your project root
3. Copy `docs/claude/agents/` → `.claude/agents/` in your project root (optional)
4. Rename `.template` files and customize for your project
5. Configure `docs/DOCS_README.template.md` as your `docs/README.md`
6. Create `[platform]-development.md`, `[platform]-index.md`, etc. as needed

**For AI Assistants:** Start at [AGENTS.md](AGENTS.md)

**Full Navigation:** See [INDEX.md](INDEX.md)


## Features

### Skills

Lightweight instructions that auto-trigger or can be invoked as slash commands:

- **Coding workflow** — Auto-triggered 10-step development process. See [skills/coding-workflow.md](skills/coding-workflow.md).
- **Architecture enforcement** — Auto-triggered rules that prevent duplication and layer violations
- **Documentation** — Writing rules following Information Minimalism
- **Job skills** — Slash commands (`/validate-docs`) that run tools with one command
- **Convention skills** — Test runner (`/test-runner`), test recommender (`/test-recommender`)

Skill instructions live in `skills/` (any LLM reads directly). Claude Code wrappers in `claude/skills/` provide auto-triggering and slash commands. See [subagents/README.md](subagents/README.md) for the pattern.

### Sub-Agents

Specialized instruction sets for complex domain-specific tasks. Instead of one general-purpose AI handling everything, sub-agents provide focused expertise (testing, documentation, validation). See [subagents/index.md](subagents/index.md).

### Documentation

- **Information Minimalism** — 3-question test: needed? obvious? duplicate? See [INFORMATION_MINIMALISM.md](INFORMATION_MINIMALISM.md).
- **Behavior vs. Platform** — Separate what the software does from how it's built. See [DOCUMENTATION_GUIDELINES.md](DOCUMENTATION_GUIDELINES.md).
- **Validation** — Two agents: `VALIDATION_DOCS` (structural checks) and `VALIDATION_LLM` (can a fresh LLM navigate the docs?).

### Jobs Registry

Central registry of runnable tasks with triggers. See [tools/JOBS.md](tools/JOBS.md).


## Repo Structure

```
AGENTS.md                           # LLM entry point and workflow router
INDEX.md                            # Navigation map
DOCUMENTATION_GUIDELINES.md         # Documentation standards reference
INFORMATION_MINIMALISM.md           # 3-question test
wiki.md                             # Wiki setup and configuration

skills/                             # Skill instructions (any LLM)
├── coding-workflow.md              #   10-step development workflow
├── architecture-rules.md           #   Layer boundaries and reuse enforcement
├── documentation.md                #   Writing rules and placement
├── validate-docs.md                #   Documentation validation steps
├── test-runner.template.md         #   Test execution (template)
└── test-recommender.template.md    #   Test category recommendation (template)

subagents/                          # Sub-agent instructions (any LLM)
├── README.md                       #   Guide for creating agents and skills
├── VALIDATION_DOCS.md              #   Doc structure validation
├── VALIDATION_LLM.md               #   LLM doc effectiveness test
├── index.md                        #   Available agents registry
└── project-manager.template.md     #   Issue management (template)

claude/                             # Claude Code wrappers (copy to .claude/)
├── skills/                         #   Thin redirects to skills/
└── agents/                         #   Thin redirects to subagents/

features/                           # Feature documentation
tools/                              # Jobs registry
platform-*.template.md              # Platform-specific templates
CLAUDE.md.template                  # Copy to project root as CLAUDE.md
CODEX.md.template                   # Copy to project root as CODEX.md
DOCS_README.template.md             # Copy as docs/README.md in your project
```

UPPERCASE = framework files (keep as-is) / lowercase = your project content


## License

MIT
