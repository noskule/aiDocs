# Sub-Agents Guide

How to create and integrate specialized AI sub-agents for your project.


## What Are Sub-Agents?

Sub-agents are specialized instruction sets for complex domain-specific tasks. Instead of one general-purpose AI, you define experts for specific areas (database, testing, UI, etc.).

**Benefits:**
- Domain expertise concentrated in one place
- Consistent patterns across similar tasks
- Context-efficient (loaded only when needed)
- Reusable across conversations


## File Structure

```
docs/
└── subagents/
    ├── db-expert.md
    ├── unit-test.md
    ├── ui-component.md
    └── ...
```


## Agent File Format

Each agent is a markdown file with:

```markdown
# agent-name

One-line description of what this agent does.

## Purpose

Brief explanation of the agent's role.

## Responsibilities

- Specific task 1
- Specific task 2
- ...

## Key Files

| File | Purpose |
|------|---------|
| `path/to/file.kt` | What it contains |

## Patterns

Code patterns and examples the agent should follow.

## Checklist

- [ ] Step 1
- [ ] Step 2

## References

Links to relevant docs and files.
```


## Integrating with AGENTS.md

Add a Sub-Agents section to `docs/AGENTS.md`:

```markdown
## Sub-Agents

Specialized agents for complex domain-specific tasks. Located in `docs/subagents/`.

| Agent | Use When... |
|-------|-------------|
| `agent-name` | Brief description of when to use |
| `another-agent` | Another use case |

**Read agent file before use** - contains patterns, examples, and checklists.
```

This gives the LLM:
1. Awareness that sub-agents exist
2. Quick lookup of which agent fits the task
3. Pointer to detailed instructions


## Creating a New Agent

1. Identify a complex, repeatable task area
2. Create `docs/subagents/agent-name.md`
3. Document: purpose, patterns, key files, checklist
4. Add entry to AGENTS.md Sub-Agents table
5. Test by invoking on a real task


## When to Create a Sub-Agent

**Good candidates:**
- Tasks with specific patterns (migrations, tests)
- Areas requiring domain knowledge (BLE, Wear OS)
- Repeatable workflows with checklists
- Complex integrations (charts, responsive UI)

**Skip if:**
- One-off task
- Simple, obvious implementation
- Already covered by existing agent


## Agent Naming

Use lowercase, hyphenated names:
- `db-expert` not `DatabaseExpert`
- `unit-test` not `UnitTesting`
- `device-ble` not `BLEDevice`


**Last Updated:** 2026-01-12
