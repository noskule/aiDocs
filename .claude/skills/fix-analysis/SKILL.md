---
name: fix-analysis
description: Fixes mechanical code analysis findings (documentation gaps, layer violations).
argument-hint: ""
context: fork
agent: general-purpose
---

You are fixing mechanical code analysis findings. Follow these steps:

1. **Read** `docs/subagents/CODE_ANALYSIS.md` for detailed instructions
2. **Read** `docs/code-index/analysis.md` for the current findings
3. **Read** `docs/[platform]-architecture-rules.md` for project architecture rules (if it exists)
4. **Fix** mechanical issues only:
   - Documentation gaps
   - Layer violations
   - Simple naming issues
5. **Skip** findings that require design decisions — flag these for the user
6. **Report** what was fixed and what remains

**Prerequisite:** `/review-analysis` should have been run first to classify findings.
