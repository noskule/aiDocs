# Sub-Agents Index

Available specialized agents for this project. Read the agent file before use.

Some subagents have companion **skills** (`.claude/skills/`) for auto-triggering and slash command support. Their reference docs here remain the full knowledge source.


## Domain Agents

> Add your domain-specific agents here (database, devices, UI patterns, etc.)
>
> Example entry:
> | Agent | Purpose | Skill |
> |-------|---------|-------|
> | [`agent-name`](agent-name.md) | Describe what this agent does | `/skill-name` or — |


## Test Agents

| Agent | Purpose | Skill |
|-------|---------|-------|
| [`test-runner`](test-runner.md) | Execute tests by category | `/test-runner` |


## Project Management Agents

| Agent | Purpose | Skill |
|-------|---------|-------|
| [`project-manager`](project-manager.template.md) | Issue and project board management (template) | — |

## Documentation Agents

| Agent | Purpose | Skill |
|-------|---------|-------|
| [`documentation`](documentation.md) | Write docs following project guidelines | `/documentation` |

## Validation Agents

| Agent | Purpose | Skill |
|-------|---------|-------|
| [`VALIDATION_DOCS`](VALIDATION_DOCS.md) | Validate docs structure and consistency | `/validate-docs` |
| [`VALIDATION_LLM`](VALIDATION_LLM.md) | Test docs effectiveness via LLM knowledge test | — |


**Last Updated:** 2026-02-21
