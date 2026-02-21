# Jobs

Runnable tasks for code generation, analysis, and validation. This is the central registry — check here to see what's available.

## Available Jobs

| Job | Command | Output | Skill |
|-----|---------|--------|-------|
| [Generate index](#generate-index) | `python docs/tools/code-index/generate.py --config aidocs.yaml` | `docs/code-index/index.md` | `/generate-index` |
| [Run analysis](#run-analysis) | `python docs/tools/code-index/analyze.py --config aidocs.yaml` | `docs/code-index/analysis.md` | `/run-analysis` |
| [Review analysis](#review-analysis) | Invoke `code-analysis` agent (review mode) | Prioritized action list | `/review-analysis` |
| [Fix analysis findings](#fix-analysis-findings) | Invoke `code-analysis` agent (fix mode) | Fixed findings + remaining count | `/fix-analysis` |
| [Validate docs](#validate-docs) | Invoke `validation` agent | Pass/fail checklist | `/validate-docs` |

## When to Run

| After... | Run... |
|----------|--------|
| Modifying public APIs (add/remove/rename classes, functions) | Generate index |
| Completing a refactoring task | Run analysis |
| Running analysis | Review analysis |
| Reviewing analysis, ready to fix | Fix analysis findings |
| Writing or updating documentation | Validate docs |
| Starting a new iteration/sprint | Run analysis (baseline) |

## Job Details

### Generate index

Parses source ASTs and produces a two-level markdown index for LLM orientation.

```bash
cd docs/tools/code-index && .venv/Scripts/python generate.py --config ../../../aidocs.yaml
```

Commit the updated `docs/code-index/` files with your change.

### Run analysis

Runs analyzers against parsed declarations and generates a findings report.

```bash
cd docs/tools/code-index && .venv/Scripts/python analyze.py --config ../../../aidocs.yaml
```

Review the report before committing — findings are informational, not all require action.

### Review analysis

Interprets the analysis report and classifies findings as actionable, acceptable, or deferred.

1. Invoke the `code-analysis` agent (auto-discovered from `.claude/agents/`) in **review mode**
2. The agent reads its detailed instructions from `docs/subagents/CODE_ANALYSIS.md` automatically
3. Output: prioritized list of actions with refactoring suggestions

### Fix analysis findings

Automatically fixes mechanical findings (documentation gaps, layer violations). Skips findings requiring design decisions.

1. Invoke the `code-analysis` agent in **fix mode**
2. Prerequisite: review mode must have run first
3. Output: fix summary with what was changed and what remains

### Validate docs

Checks documentation structure and consistency.

1. Invoke the `validation` agent (auto-discovered from `.claude/agents/`)
2. The agent reads its detailed instructions from `docs/subagents/VALIDATION_DOCS.md` automatically
3. Output: pass/fail checklist with issues to fix

## Configuration

All tool jobs use `aidocs.yaml` at the project root. See [code-index/README.md](code-index/README.md) for config details.
