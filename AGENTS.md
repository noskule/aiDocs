# AI Agent Guidelines

**Audience:** AI coding assistants (LLMs) working on this project


## MANDATORY READING

**You MUST read the following files BEFORE starting any task:**
- This file (AGENTS.md) - situational references, available skills and agents
- [INDEX.md](INDEX.md) - documentation map
- `[platform]-index.md` - platform documentation maps (if exists)
- Wiki index (if exists) - see [wiki.md](wiki.md) for location


## Situational References

Read these **when you reach that situation**, not upfront:

| When you're...          | Read...                                |
|-------------------------|----------------------------------------|
| Finding platform docs   | `[platform]-index.md`                  |
| Setting up / installing | `[platform]-installation.md`           |
| Writing code            | `[platform]-architecture-rules.md`, `[platform]-development.md` |
| Writing tests           | `[platform]-testing.md`                |
| Writing documentation   | `docs/DOCUMENTATION_GUIDELINES.md`     |
| Creating agents/skills  | `docs/creating-agents.md`              |
| Creating issues         | `docs/issue-tracker.md`                |
| Running a job           | `docs/tools/JOBS.md`                   |
| Syncing design ↔ code   | `docs/design-sync.md`                  |
| Unsure about approach   | Ask the user                           |

**Don't know which doc?** Check [INDEX.md](INDEX.md) for section headers.


## Skills

Skills live in `.claude/skills/` with full instructions inline. They auto-trigger or are invoked as slash commands.

**Workflow skills** (auto-triggered):

| Skill | Triggers when... |
|-------|-------------------|
| `coding-workflow` | Starting a development task |
| `architecture-rules` | Implementing features or writing new code |

**Job skills** (slash commands):

| Skill | Purpose |
|-------|---------|
| `/validate-docs [scope]` | Validate doc structure (forked) |

**Convention skills** (slash commands + auto-triggered):

| Skill | Purpose |
|-------|---------|
| `/test-runner [category]` | Run tests by category |
| `/test-recommender` | Analyze changes, recommend test category |
| `/documentation` | Documentation writing rules |

> **Customize:** Skills with `.template` suffix need project-specific configuration.
>
> **Non-Claude LLMs:** Read `.claude/skills/*/SKILL.md` directly (ignore YAML frontmatter).


## Agents

Agents live in `.claude/agents/` with full instructions inline. They run in isolated context for heavy tasks.

| Agent | Use when... |
|-------|-------------|
| `validation-docs` | Validating documentation structure |
| `validation-llm` | Testing LLM documentation effectiveness |
| `project-manager` | Issue management (template — customize first) |

> **Customize:** Replace template agents and add your domain-specific agents.
>
> **Non-Claude LLMs:** Read `.claude/agents/*.md` directly (ignore YAML frontmatter).
>
> **Creating new agents:** See [creating-agents.md](creating-agents.md).


**Last Updated:** 2026-05-03
