# aiDocs

Documentation and coding workflow framework for AI-assisted development. Add to your project via `git subtree add --prefix=docs`.

**LLMs:** Start at [AGENTS.md](AGENTS.md)

**Navigation:** See [INDEX.md](INDEX.md)


## Integration

```bash
# Add to your project
git subtree add --prefix=docs https://github.com/noskule/aiDocs.git main --squash

# Update later
git subtree pull --prefix=docs https://github.com/noskule/aiDocs.git main --squash
```

### Setup after adding

1. Copy `docs/claude/` → `.claude/` in your project root
2. Copy `docs/CLAUDE.md.template` → `CLAUDE.md` in your project root
3. Rename `.template` files and customize for your project


## Structure

```
AGENTS.md                           # LLM entry point and router
INDEX.md                            # Navigation map
DOCUMENTATION_GUIDELINES.md         # Documentation standards reference
INFORMATION_MINIMALISM.md           # 3-question test
creating-agents.md                  # How to create skills and agents
wiki.md                             # Wiki setup
issue-tracker.md                    # Issue tracker conventions

claude/                             # Skills & agents (copy to .claude/)
├── skills/
│   ├── coding-workflow/SKILL.md
│   ├── architecture-rules/SKILL.md.template
│   ├── documentation/SKILL.md
│   ├── validate-docs/SKILL.md
│   ├── test-runner/SKILL.md.template
│   └── test-recommender/SKILL.md.template
└── agents/
    ├── validation-docs.md
    ├── validation-llm.md
    ├── project-manager.md.template
    └── agent-name.template.md

features/feature.template.md
tools/JOBS.md
platform-*.template.md
CLAUDE.md.template
CODEX.md.template
```

UPPERCASE = framework files / lowercase = your project content


## License

MIT
