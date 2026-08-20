# Jobs

Runnable tasks for validation. This is the central registry — check here to see what's available.

## Available Jobs

| Job | Command | Output | Skill |
|-----|---------|--------|-------|
| [Check docs (mechanical)](#check-docs) | `python docs/tools/check-docs.py` | Errors/warnings, exit code | — |
| [Validate docs (judgment)](#validate-docs) | Invoke `validation-docs` agent | Pass/fail checklist | `/validate-docs` |

## When to Run

| After... | Run... |
|----------|--------|
| Any documentation change (also runs in CI) | Check docs |
| Before major releases, or quarterly | Validate docs |

## Job Details

### Check docs

Mechanical structural checks: link resolution (case-sensitive), orphan pages, index consistency, agent-wrapper bindings, template hygiene.

1. Run `python docs/tools/check-docs.py`
2. Exit code non-zero on errors; warnings don't fail the build

### Validate docs

Judgment checks a script can't do: duplicated knowledge, stale content, wiki structure, file focus.

1. Invoke the `validation-docs` agent (auto-discovered from `.claude/agents/`)
2. The agent runs check-docs.py first, then reads `docs/subagents/validation-docs.md` for the judgment checklist
3. Output: report with issues to fix
