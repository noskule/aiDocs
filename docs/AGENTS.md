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
| Validating docs         | `subagents/validation.md`     |
| Starting a task         | `CODING_GUIDELINES.md`        |
| Creating sub-agents     | `subagents/README.md`         |
| Unsure about approach   | Ask the user                  |

**Don't know which doc?** Check [INDEX.md](INDEX.md) for section headers.


## Workflow Overview

Follow the complete workflow in [CODING_GUIDELINES.md](CODING_GUIDELINES.md). Summary:

```
1. Create branch
2. Implement code
3. Write tests (if required)
4. Run tests - ALL must pass
5. Report to user (what to test + how via platform guide)
6. User manually tests and reviews
7. Capture technical discoveries
8. Write documentation
9. Create pull request
10. User merges PR
11. Continue
```


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
| Validating documentation | `validation` |

> **Customize:** Replace examples with your project's agents from `docs/subagents/`.


**Last Updated:** 2026-01-17
