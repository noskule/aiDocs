# aiDocs

A **documentation and coding workflow framework** for AI-assisted development.

For developers using AI coding assistants. Works with any language, platform, or AI tool.

- **10-step coding workflow** — Auto-triggered skill that guides feature branch to merged PR
- **Information minimalism** — Only document what a seasoned developer or LLM couldn't figure out from the code alone
- **Just-in-time information** — Read indexes upfront, load details only when needed
- **3 documentation levels** — Code (intent/rationale), /docs (operations), Wiki (how software works)
- **Skills & Agents** — Full instructions in `docs/claude/`, auto-triggered or slash-invoked by Claude Code
- **Jobs registry** — Central list of runnable tasks with triggers for when to run each


## Integration

Add aiDocs to your project via **git subtree**:

```bash
# Add (first time)
git subtree add --prefix=docs https://github.com/noskule/aiDocs.git main --squash

# Update later
git subtree pull --prefix=docs https://github.com/noskule/aiDocs.git main --squash
```

### Setup after adding

1. Copy `docs/claude/` → `.claude/` in your project root
2. Copy `docs/CLAUDE.md.template` → `CLAUDE.md` in your project root
3. Configure `docs/README.md` with project info and wiki location
4. Rename `.template` files and customize for your project

**For AI Assistants:** Start at [docs/AGENTS.md](docs/AGENTS.md)

**Full Navigation:** See [docs/INDEX.md](docs/INDEX.md)


## Features

### Skills & Agents

Skills and agents live in `docs/claude/` with **full instructions inline** — no indirection.

- **Skills** (`.claude/skills/`) — auto-triggered or slash commands. Lightweight, inline in conversation.
- **Agents** (`.claude/agents/`) — explicitly invoked. Heavy tasks, isolated context.

Non-Claude LLMs read the same files directly (ignore YAML frontmatter).

See [docs/creating-agents.md](docs/creating-agents.md) for how to create new ones.

### Documentation

- **Information Minimalism** — 3-question test before writing docs. See [INFORMATION_MINIMALISM.md](docs/INFORMATION_MINIMALISM.md).
- **Documentation Levels** — Code comments, /docs folder, Wiki. See [DOCUMENTATION_GUIDELINES.md](docs/DOCUMENTATION_GUIDELINES.md).
- **Validation** — Two agents: `validation-docs` (structural) and `validation-llm` (effectiveness).

### Jobs Registry

Central registry of runnable tasks. See [tools/JOBS.md](docs/tools/JOBS.md).


## Project Structure

```
docs/                                   # Subtree'd into projects
├── AGENTS.md                           # LLM entry point and router
├── INDEX.md                            # Navigation map
├── DOCUMENTATION_GUIDELINES.md         # Documentation standards reference
├── INFORMATION_MINIMALISM.md           # 3-question test
├── creating-agents.md                  # How to create skills and agents
├── wiki.md                             # Wiki setup
├── issue-tracker.md                    # Issue tracker conventions
├── claude/                             # Skills & agents (copy to .claude/)
│   ├── skills/
│   │   ├── coding-workflow/SKILL.md
│   │   ├── architecture-rules/SKILL.md.template
│   │   ├── documentation/SKILL.md
│   │   ├── validate-docs/SKILL.md
│   │   ├── test-runner/SKILL.md.template
│   │   └── test-recommender/SKILL.md.template
│   └── agents/
│       ├── validation-docs.md
│       ├── validation-llm.md
│       ├── project-manager.md.template
│       └── agent-name.template.md
├── features/
│   └── feature.template.md
├── tools/
│   └── JOBS.md
├── platform-architecture-rules.template.md
├── platform-development.template.md
└── platform-index.template.md

CLAUDE.md.template                      # Copy to project root
CODEX.md.template                       # Copy to project root
```

UPPERCASE = framework files (keep as-is) / lowercase = your project content


## License

MIT
