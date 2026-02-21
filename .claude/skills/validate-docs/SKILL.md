---
name: validate-docs
description: Validates documentation structure and consistency across docs/ and wiki/.
argument-hint: "[scope: docs|wiki|both]"
context: fork
agent: general-purpose
---

You are validating documentation quality. Follow these steps:

1. **Read** `docs/subagents/VALIDATION_DOCS.md` for detailed validation instructions
2. **Determine scope:** validate `docs/`, `wiki/`, or both (check $ARGUMENTS, default to `docs/`)
3. **Run the validation checklist:**
   - Index cross-check (INDEX.md, subagents/index.md, platform indexes)
   - Internal link validation
   - Orphan file detection
   - Duplicate content detection
   - File organization check
   - Staleness check (Last Updated dates)
4. **Output** a pass/fail checklist with issues to fix
5. **Ask** the user: fix now, save report, or create GitHub issues?
