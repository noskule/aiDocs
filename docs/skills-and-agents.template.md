# Skills & Agents

All available skills and specialized agents for this project. **Project-owned:** extend this file as you add skills and agents. Full instructions live in `.claude/` — this registry routes every AI tool (Claude Code discovers them natively; other tools read the linked files directly).


## Skills

**Job skills** (slash commands for runnable tasks):

| Skill | Purpose |
|-------|---------|
| [`/setup`](../.claude/skills/setup/SKILL.md) | Initial aiDocs setup in a project (interview form) |
| [`/update-aidocs`](../.claude/skills/update-aidocs/SKILL.md) | Pull upstream aiDocs standard updates |
| [`/validate-docs`](../.claude/skills/validate-docs/SKILL.md) | Validate doc structure (forked) |

**Convention skills** (slash commands + auto-triggered):

| Skill | Purpose |
|-------|---------|
| `/test-runner [category]` | Run tests by category |
| `/test-recommender` | Analyze changes, recommend test category |
| [`/documentation`](../.claude/skills/documentation/SKILL.md) | Documentation writing rules |

**Auto-triggered skills** (no slash command, invoked automatically):

| Skill | Triggers when... |
|-------|-------------------|
| `architecture-rules` | Implementing features or writing new code |
| `coding-workflow` | Starting a development task (tracks the 10 steps) |

> Skills with a `.template` suffix in `.claude/skills/` need activation and project-specific configuration.


## Agents

Full instructions in `.claude/agents/<name>.md`. Claude Code runs them forked; other tools read and follow the file inline.

| Agent | Purpose | Skill |
|-------|---------|-------|
| [`code-analysis`](../.claude/agents/code-analysis.md) | Interpret the auto-generated code-index analysis report | — |
| [`issue-writer`](../.claude/agents/issue-writer.md) | GitHub issue creation with correct type, labels, project fields | — |
| [`validation-docs`](../.claude/agents/validation-docs.md) | Validate docs quality (judgment half; script does structure) | `/validate-docs` |
| [`validation-llm`](../.claude/agents/validation-llm.md) | Test docs effectiveness via LLM knowledge test | — |

> Add your project's agents here (database, devices, UI patterns, test writers, ...)


**Last Updated:** YYYY-MM-DD
