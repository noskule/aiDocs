# Jobs

Runnable tasks for validation. This is the central registry — check here to see what's available.

## Available Jobs

| Job | Command | Output | Skill |
|-----|---------|--------|-------|
| [Validate docs](#validate-docs) | Invoke `validation-docs` agent | Pass/fail checklist | `/validate-docs` |

## When to Run

| After... | Run... |
|----------|--------|
| Writing or updating documentation | Validate docs |

## Job Details

### Validate docs

Checks documentation structure and consistency.

1. Invoke the `validation-docs` agent (auto-discovered from `.claude/agents/`)
2. The agent reads its detailed instructions from `docs/subagents/validation-docs.md` automatically
3. Output: pass/fail checklist with issues to fix
