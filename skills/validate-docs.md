# validate-docs

Validates documentation structure and consistency across docs/ and wiki/.

## Scope

Determine scope: `docs/`, `wiki/`, or both. Default to `docs/` if not specified.

## Steps

1. **Read** `docs/subagents/VALIDATION_DOCS.md` for detailed validation instructions
2. **Run the validation checklist:**
   - Index cross-check (INDEX.md, subagents/index.md, platform indexes)
   - Internal link validation
   - Orphan file detection
   - Duplicate content detection
   - File organization check
   - Staleness check (Last Updated dates)
3. **Output** a pass/fail checklist with issues to fix
4. **Ask** the user: fix now, save report, or create issues?
