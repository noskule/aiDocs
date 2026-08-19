# AI Agent Guidelines

**Audience:** AI coding assistants (LLMs) working on this project

Behavioral instructions and workflow for AI assistants. Fixed standard file — do not edit; project-specific skills and agents are listed in [subagents/index.md](subagents/index.md).


## MANDATORY READING

**You MUST read the following files BEFORE starting any task:**

- This file (AGENTS.md) - workflow and situational references
- [INDEX.md](INDEX.md) - documentation map
- [coding-guidelines.md](coding-guidelines.md) - The Coding workflow you have to follow
- [subagents/index.md](subagents/index.md) - available skills and specialized agents
- Wiki index (if exists) - see [wiki.md](wiki.md) for location


## Situational References

Read these **when you reach that situation**, not upfront:

| When you're...          | Read...                       |
|-------------------------|-------------------------------|
| Finding platform docs   | `INDEX.md`                   |
| Setting up / installing | `installation.md`            |
| Writing code            | `architecture-rules.md`, `development.md` |
| Writing tests           | `testing.md`                 |
| Writing documentation   | `DOCUMENTATION_GUIDELINES.md` |
| Validating docs         | `subagents/validation-docs.md`|
| Testing docs for LLMs   | `subagents/validation-llm.md` |
| Starting a task         | `coding-guidelines.md`        |
| Creating sub-agents     | `subagents/README.md`         |
| Creating GitHub issues  | `issue-tracker.md`            |
| Running a job           | `tools/jobs.md`               |
| Syncing design ↔ code   | `design-sync.md`              |
| Unsure about approach   | Ask the user                  |

**Project-specific situations** (threat model, special test docs, ...) are listed in [project-index.md](project-index.md), if it exists — never add rows to the table above.

**Don't know which doc?** Check [INDEX.md](INDEX.md) for section headers.


## Skills and Sub-Agents

Two kinds of specialized instructions:

- **Skills** (`.claude/skills/`) — lightweight, auto-triggered or invoked as slash commands
- **Sub-agents** (`docs/subagents/`) — heavy, self-contained tasks with verbose output; optional Claude wrappers in `.claude/agents/`, each reads its reference doc at invocation time

**Which skill or agent fits the task?** Check [subagents/index.md](subagents/index.md) — it lists every available skill and agent with its trigger.

> **Setup:** See [subagents/README.md](subagents/README.md) for how to create and integrate skills and agents.


**Last Updated:** 2026-08-19
