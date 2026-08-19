# Skills & Agents Index

All available skills and specialized agents for this project. **Project-owned:** extend this file as you add skills and agents.

Some subagents have companion **skills** (`.claude/skills/`) for auto-triggering and slash command support. Their reference docs here remain the full knowledge source.


## Skills

**Job skills** (slash commands for runnable tasks):

| Skill | Purpose |
|-------|---------|
| `/setup` | Initial aiDocs setup in a project (interview form) |
| `/update-aidocs` | Pull upstream aiDocs standard updates into this project |
| `/validate-docs` | Validate doc structure (forked) |

**Convention skills** (slash commands + auto-triggered):

| Skill | Purpose |
|-------|---------|
| `/test-runner [category]` | Run tests by category |
| `/test-recommender` | Analyze changes, recommend test category |
| `/documentation` | Documentation writing rules |

**Auto-triggered skills** (no slash command, Claude invokes automatically):

| Skill | Triggers when... |
|-------|-------------------|
| `architecture-rules` | Implementing features or writing new code |
| `coding-workflow` | Starting a development task (tracks the 10 steps) |

> Skills with a `.template` suffix in `.claude/skills/` need activation and project-specific configuration.


## Domain Agents

| Agent | Purpose | Skill |
|-------|---------|-------|
| [`example-agent`](example-agent.md) | Example: describe what this agent does | — |

> Add your domain-specific agents here (database, devices, UI patterns, etc.)


## Test Agents

| Agent | Purpose | Skill |
|-------|---------|-------|
| [`test-runner`](test-runner.md) | Execute tests by category | `/test-runner` |

> Add test-writer agents as needed for your project.


## Project Management Agents

| Agent | Purpose | Skill |
|-------|---------|-------|
| [`issue-writer`](issue-writer.md) | GitHub issue creation with correct type, labels, project fields | — |

## Validation Agents

| Agent | Purpose | Skill |
|-------|---------|-------|
| [`validation-docs`](validation-docs.md) | Validate docs structure and consistency | `/validate-docs` |
| [`validation-llm`](validation-llm.md) | Test docs effectiveness via LLM knowledge test | — |
| [`code-analysis`](code-analysis.md) | Interpret the auto-generated code-index analysis report | — |


**Last Updated:** 2026-08-19
