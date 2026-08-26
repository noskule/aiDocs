# Triage Evals

Eval cases for the documentation system: bug-report-phrased questions with ground truth. The `validation-llm` agent runs them against a fresh agent to measure whether the docs — especially `feature-map.md` — route triage to the right entry point. See Triage Eval Mode in `.claude/agents/validation-llm.md`.

## Case Format

One row per case. Expected entry points use the same grep-able identifiers as `feature-map.md`.

| # | Question (bug-report phrasing) | Expected entry point | Expected source |
|---|--------------------------------|----------------------|-----------------|
| 1 | [e.g. "Scanning hangs when the gateway is offline — where do you start reading?"] | `[ClassName.method]` | [feature-map.md row / wiki page] |

**Last Updated:** [date]
