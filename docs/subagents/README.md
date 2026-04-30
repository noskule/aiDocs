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

**The cardinal rule: skills say "when and what", docs say "how".** A skill should never inline detailed tables, mappings, or examples that exist in `docs/subagents/`. Instead, the skill tells the LLM *when to act* and *what to do*, then delegates to `docs/subagents/` for the *how*. This eliminates duplication and ensures a single source of truth. If a mapping table or checklist changes, only the subagent doc needs updating.

**When to create a skill vs. a sub-agent:**
- **Skill only** — simple rule enforcement, slash command for a tool, lightweight knowledge
- **Sub-agent only** — produces long output, needs full isolation, requires many tool calls
- **Both** — domain knowledge that should auto-trigger (skill) but also supports deep implementation work (sub-agent)


## File Structure

```
.claude/agents/                # Agent wrappers (auto-discovered by Claude Code)
├── agent-name.template.md     #   Template for new agents
├── validation-docs.md         #   Example wrapper
└── ...

docs/subagents/                # Detailed reference documentation
├── VALIDATION_DOCS.md         #   Patterns, examples, checklists
├── project-manager.md
└── ...
```

**`.claude/agents/`** — Thin wrappers with YAML frontmatter (`name`, `description`, `tools`). Auto-discovered by Claude Code. Each points to its reference doc.

**`docs/subagents/`** — Full reference documentation read by agents at invocation time.

## Agent Wrapper Format (`.claude/agents/`)

See `agent-name.template.md` for the standard format. Key fields:

- `name` — lowercase hyphenated
- `description` — one line, matches AGENTS.md trigger
- `tools` — comma-separated list of tools the agent needs
- Body — role + pointer to `docs/subagents/` reference doc

## Agent Reference Format (`docs/subagents/`)

Each reference doc is a markdown file with:

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
2. Create `docs/subagents/agent-name.md` — reference doc
3. Create `.claude/agents/agent-name.md` — wrapper (copy from template)
4. Add entry to AGENTS.md Agent Triggers table
5. Add entry to `docs/subagents/index.md`
6. Test by invoking on a real task


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
