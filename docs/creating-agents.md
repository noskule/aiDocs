# Creating Agents and Skills

How to create and integrate specialized AI agents and skills for your project.


## Skills vs. Agents

| | Skills | Agents |
|---|---|---|
| **Context** | Runs inline in conversation | Runs in isolated context (forked) |
| **Trigger** | Auto-triggered by description match, or slash command | Explicitly invoked via Task tool |
| **Best for** | Lightweight rules, quick jobs, knowledge injection | Heavy computation, verbose output, multi-step workflows |
| **Overhead** | Minimal (~description loaded into context) | ~20k tokens per invocation |

**When to create a skill vs. an agent:**
- **Skill only** — simple rule enforcement, slash command for a tool, lightweight knowledge
- **Agent only** — produces long output, needs full isolation, requires many tool calls
- **Both** — domain knowledge that should auto-trigger (skill) but also supports deep implementation work (agent)


## File Structure

All skills and agents live in `docs/claude/` (shipped via subtree). Users copy to `.claude/` at their project root.

```
docs/claude/
├── skills/
│   ├── skill-name/SKILL.md          # Skill with full instructions
│   └── skill-name/SKILL.md.template # Template — customize per project
└── agents/
    ├── agent-name.md                 # Agent with full instructions
    └── agent-name.md.template        # Template — customize per project
```

After setup, project root has:
```
.claude/
├── skills/skill-name/SKILL.md
└── agents/agent-name.md
```


## Skill File Format

```markdown
---
name: skill-name
description: One-line description (used for auto-triggering)
argument-hint: "[optional args hint]"
user-invocable: false          # omit for slash-command skills
context: fork                  # optional: runs in isolated context
agent: general-purpose         # optional: agent type for forked context
---

# skill-name

Full instructions here. No redirects — everything the skill needs is inline.
```

Key frontmatter fields:
- `name` — lowercase hyphenated
- `description` — triggers auto-matching; also shown in slash command list
- `user-invocable: false` — skill triggers automatically, no slash command
- `argument-hint` — shown to user when invoking via slash command


## Agent File Format

```markdown
---
name: agent-name
description: One-line description matching the trigger from AGENTS.md
tools: Read, Grep, Glob, Bash
---

# agent-name

Full instructions here. Purpose, responsibilities, process, output format — everything inline.
```

Key frontmatter fields:
- `name` — lowercase hyphenated
- `description` — one line, matches AGENTS.md trigger
- `tools` — comma-separated list of tools the agent needs


## Creating a New Skill

1. Create `docs/claude/skills/skill-name/SKILL.md`
2. Add YAML frontmatter + full instructions
3. Add entry to AGENTS.md skills table
4. Copy to `.claude/skills/` in your project
5. Test by triggering

## Creating a New Agent

1. Create `docs/claude/agents/agent-name.md`
2. Add YAML frontmatter + full instructions
3. Add entry to AGENTS.md agents table
4. Copy to `.claude/agents/` in your project
5. Test by invoking on a real task


## When to Create an Agent

**Good candidates:**
- Tasks with specific patterns (migrations, tests)
- Areas requiring domain knowledge (BLE, Wear OS)
- Repeatable workflows with checklists
- Complex integrations (charts, responsive UI)

**Skip if:**
- One-off task
- Simple, obvious implementation
- Already covered by existing agent


## Naming

Use lowercase, hyphenated names:
- `db-expert` not `DatabaseExpert`
- `unit-test` not `UnitTesting`
- `device-ble` not `BLEDevice`


**Last Updated:** 2026-05-03
