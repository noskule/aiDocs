---
name: review-analysis
description: Reviews code analysis findings, classifies them as actionable, acceptable, or deferred.
argument-hint: ""
context: fork
agent: general-purpose
---

You are reviewing code analysis findings. Follow these steps:

1. **Read** `docs/subagents/CODE_ANALYSIS.md` for detailed instructions
2. **Read** `docs/code-index/analysis.md` for the current findings
3. **Read** `docs/[platform]-architecture-rules.md` for project architecture rules (if it exists)
4. **Classify** each finding as:
   - **Actionable** — should be fixed now
   - **Acceptable** — known trade-off, no action needed
   - **Deferred** — valid but not priority
5. **Output** a prioritized action list with refactoring suggestions

This is **review mode** — classify and prioritize only, do not modify code.
