# Sub-Agents Index

Available specialized agents for this project. Read the agent file before use.

Some subagents have companion **skills** (`.claude/skills/`) for auto-triggering and slash command support. Their reference docs here remain the full knowledge source.


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

## Documentation Agents

| Agent | Purpose | Skill |
|-------|---------|-------|
| [`documentation`](documentation.md) | Write docs following project guidelines | `/documentation` |

## Validation Agents

| Agent | Purpose | Skill |
|-------|---------|-------|
| [`validation-docs`](validation-docs.md) | Validate docs structure and consistency | `/validate-docs` |
| [`validation-llm`](validation-llm.md) | Test docs effectiveness via LLM knowledge test | — |
| [`code-analysis`](code-analysis.md) | Interpret the auto-generated code-index analysis report | — |


**Last Updated:** 2026-02-21
