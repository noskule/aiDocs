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

1. Invoke via `/validate-docs` skill or directly invoke the `validation-docs` agent
2. The agent has full instructions inline in `.claude/agents/validation-docs.md`
3. Output: pass/fail checklist with issues to fix
