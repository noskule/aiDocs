# AI Agent Guidelines

**Audience:** AI coding assistants (LLMs) working on this project

Behavioral instructions and workflow for AI assistants. This is a project-independent template.


## MANDATORY READING

**You MUST read the following files BEFORE starting any task:**
- This file (AGENTS.md) - workflow and situational references
- [INDEX.md](INDEX.md) - documentation map
- [CODING_GUIDELINES.md](CODING_GUIDELINES.md) - The Coding workflow you have to follow
- [subagents/index.md](subagents/index.md) - available specialized agents
- `[platform]-index.md` - platform documentation maps (if exists)
- Wiki index (if exists) - see [wiki.md](wiki.md) for location


## Situational References

Read these **when you reach that situation**, not upfront:

| When you're...          | Read...                       |
|-------------------------|-------------------------------|
| Finding platform docs   | `[platform]-index.md`         |
| Setting up / installing | `[platform]-installation.md`  |
| Writing code            | `[platform]-architecture-rules.md`, `[platform]-development.md` |
| Writing tests           | `[platform]-testing.md`       |
| Writing documentation   | `DOCUMENTATION_GUIDELINES.md` |
| Validating docs         | `subagents/VALIDATION_DOCS.md`|
| Testing docs for LLMs   | `subagents/VALIDATION_LLM.md` |
| Starting a task         | `CODING_GUIDELINES.md`        |
| Creating sub-agents     | `subagents/README.md`         |
| Creating GitHub issues  | `issue-tracker.md`            |
| Running a job           | `tools/JOBS.md`               |
| Syncing design ↔ code   | `design-sync.md`              |
| Unsure about approach   | Ask the user                  |

**Don't know which doc?** Check [INDEX.md](INDEX.md) for section headers.


## Skills

Lightweight instructions that auto-trigger or can be invoked as slash commands.

**Instructions:** `docs/skills/` (any LLM reads these directly)
**Claude Code wrappers:** `.claude/skills/` (thin redirects with YAML frontmatter)

**Job skills** (slash commands for runnable tasks):

| Skill | Instructions | Purpose |
|-------|-------------|---------|
| `/validate-docs` | [`docs/skills/validate-docs.md`](skills/validate-docs.md) | Validate doc structure (forked) |

**Convention skills** (slash commands + auto-triggered):

| Skill | Instructions | Purpose |
|-------|-------------|---------|
| `/test-runner [category]` | [`docs/skills/test-runner.md`](skills/test-runner.template.md) | Run tests by category |
| `/test-recommender` | [`docs/skills/test-recommender.md`](skills/test-recommender.template.md) | Analyze changes, recommend test category |
| `/documentation` | [`docs/skills/documentation.md`](skills/documentation.md) | Documentation writing rules |

**Auto-triggered skills** (no slash command, Claude invokes automatically):

| Skill | Instructions | Triggers when... |
|-------|-------------|-------------------|
| `architecture-rules` | [`docs/skills/architecture-rules.md`](skills/architecture-rules.md) | Implementing features or writing new code |

> **Customize:** Skills with `.template` suffix need project-specific configuration. Copy without the suffix and customize.
>
> **Non-Claude LLMs:** Read the instructions file directly when the situation calls for it.


## Sub-Agents

Specialized agents for heavy, self-contained tasks that produce verbose output. Located in `docs/subagents/` with optional Claude agent wrappers in `.claude/agents/`.

Each agent reads its detailed instructions from `docs/subagents/` at invocation time.

> **Setup:** See [subagents/README.md](subagents/README.md) for how to create and integrate agents.


## Agent Triggers

Quick lookup for when to invoke agents during workflow:

| If you're doing...       | Invoke...        |
|--------------------------|------------------|
| `<domain-task>`          | `<agent-name>`   |
| Writing tests            | `test-writer-*`  |
| Creating GitHub issues   | `project-manager` |
| Reviewing code health    | `architecture-rules` skill (auto-triggered) |
| Validating documentation | `/validate-docs` or `VALIDATION_DOCS` agent |
| Testing LLM readiness   | `VALIDATION_LLM` |

> **Customize:** Replace examples with your project's agents from `docs/subagents/`.


**Last Updated:** 2026-02-21
