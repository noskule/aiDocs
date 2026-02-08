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
| Writing code            | `[platform]-development.md`   |
| Writing tests           | `[platform]-testing.md`       |
| Writing documentation   | `DOCUMENTATION_GUIDELINES.md` |
| Validating docs         | `subagents/VALIDATION_DOCS.md`|
| Testing docs for LLMs   | `subagents/VALIDATION_LLM.md` |
| Starting a task         | `CODING_GUIDELINES.md`        |
| Creating sub-agents     | `subagents/README.md`         |
| Unsure about approach   | Ask the user                  |

**Don't know which doc?** Check [INDEX.md](INDEX.md) for section headers.


## Sub-Agents

Specialized agents for complex domain-specific tasks. Located in `docs/subagents/`.

Use these when the task matches the agent's specialty. Invoke via Task tool.

> **Setup:** See [subagents/README.md](subagents/README.md) for how to create and integrate agents.

**Read agent file before use** - contains patterns, examples, and checklists.


## Agent Triggers

Quick lookup for when to invoke agents during workflow:

| If you're doing... | Invoke... |
|--------------------|-----------|
| `<domain-task>` | `<agent-name>` |
| Writing tests | `test-writer-*` |
| Running tests | `test-runner` |
| Validating documentation | `VALIDATION_DOCS` |
| Testing LLM readiness   | `VALIDATION_LLM` |

> **Customize:** Replace examples with your project's agents from `docs/subagents/`.


**Last Updated:** 2026-02-08
