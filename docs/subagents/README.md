# Sub-Agents Guide

How to create and integrate specialized AI sub-agents for your project.


## What Are Sub-Agents?

Sub-agents are specialized instruction sets for complex domain-specific tasks. Instead of one general-purpose AI, you define experts for specific areas (database, testing, UI, etc.).

**Benefits:**
- Domain expertise concentrated in one place
- Consistent patterns across similar tasks
- Context-efficient (loaded only when needed)
- Reusable across conversations


## Skills vs. Sub-Agents

Both are specialized instructions. Choose based on weight and trigger style:

| | Skills (`.claude/skills/`) | Sub-Agents (`docs/subagents/`) |
|---|---|---|
| **Context** | Runs inline in conversation | Runs in isolated context (forked) |
| **Trigger** | Auto-triggered by description match, or slash command | Explicitly invoked via Task tool |
| **Best for** | Lightweight rules, quick jobs, knowledge injection | Heavy computation, verbose output, multi-step workflows |
| **Overhead** | Minimal (~description loaded into context) | ~20k tokens per invocation |

**Coexistence pattern:** A subagent doc in `docs/subagents/` holds the full knowledge reference (readable by any AI tool). A companion skill in `.claude/skills/` embeds a subset for auto-triggering (Claude-specific). The skill points to the subagent doc for full details.

**When to create a skill vs. a sub-agent:**
- **Skill only** — simple rule enforcement, slash command for a tool, lightweight knowledge
- **Sub-agent only** — produces long output, needs full isolation, requires many tool calls
- **Both** — domain knowledge that should auto-trigger (skill) but also supports deep implementation work (sub-agent)


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


**Last Updated:** 2026-02-21
