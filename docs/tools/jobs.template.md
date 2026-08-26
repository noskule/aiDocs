# Jobs

Runnable tasks for validation. This is the central registry — check here to see what's available.

## Available Jobs

| Job | Command | Output | Skill |
|-----|---------|--------|-------|
| [Check docs (mechanical)](#check-docs) | `python docs/tools/check-docs.py` | Errors/warnings, exit code | — |
| [Validate docs (judgment)](#validate-docs) | Invoke `validation-docs` agent | Pass/fail checklist | `/validate-docs` |
| [Triage evals](#triage-evals) | Invoke `validation-llm` agent (Triage Eval Mode) | Hit-rate report | — |

## When to Run

| After... | Run... |
|----------|--------|
| Any documentation change (also runs in CI) | Check docs |
| Before major releases, or quarterly | Validate docs |

## Job Details

### Check docs

Mechanical structural checks: link resolution (case-sensitive), orphan pages, index consistency, agent-wrapper bindings, template hygiene, standard-set references.

1. Run `python docs/tools/check-docs.py`
2. Exit code non-zero on errors; warnings don't fail the build

### Validate docs

Judgment checks a script can't do: duplicated knowledge, stale content, wiki structure, file focus.

1. Invoke the `validation-docs` agent (auto-discovered from `.claude/agents/`)
2. The agent's instructions (`.claude/agents/validation-docs.md`) run check-docs.py first, then the judgment checklist
3. Output: report with issues to fix

### Triage evals

Routing-effectiveness test: bug-report-phrased questions from `evals.md` run against a fresh agent, scored on landing at the expected entry point (with/without `feature-map.md`).

1. Invoke the `validation-llm` agent — Triage Eval Mode runs when `tools/evals.md` exists
2. Output: hit-rate report per mode, misses diagnosed with navigation traces
