---
name: validate-docs
description: Validates documentation structure and consistency across docs/ and wiki/.
argument-hint: "[scope: docs|wiki|both]"
context: fork
agent: general-purpose
---

# validate-docs

Validates documentation structure and consistency across docs/ and wiki/.

## Scope

Determine scope from $ARGUMENTS: `docs/`, `wiki/`, or both. Default to `docs/` if not specified.

## Steps

1. **Run the validation checklist:**
   - Index cross-check (INDEX.md, platform indexes)
   - Internal link validation
   - Orphan file detection
   - Duplicate content detection
   - File organization check
   - Staleness check (Last Updated dates)
2. **Output** a pass/fail checklist with issues to fix
3. **Ask** the user: fix now, save report, or create issues?

## Validation Details

### Index Cross-Check
- Every file in docs/ should be referenced in INDEX.md
- Every listed file in INDEX.md should exist
- Platform index files should list all platform docs

### Link Validation
- Find all markdown links `[text](path)`
- Verify each target file exists
- Report broken links with file and line number

### Orphan Detection
- Find files not referenced by any index or other file
- Exclude templates and dotfiles

### File Organization
- Warn if any doc exceeds 200 lines
- Verify UPPERCASE = framework, lowercase = project content
- Check file naming conventions

### Staleness Check
- Find files with `Last Updated:` dates older than 6 months
- Report as warnings (may be fine, but worth reviewing)
