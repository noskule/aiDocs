# VALIDATION_DOCS

Validates documentation structure and consistency across docs/ and wiki/.


## Purpose

Automated documentation auditing. Run before major releases or quarterly to catch broken links, orphan files, stale content, and structural issues.


## Responsibilities

- Verify index files match actual content
- Find broken internal links
- Detect orphan pages (unreachable from navigation)
- Check for duplicated information
- Validate file organization and naming
- Report issues with actionable fixes


## When to Invoke

- Before major releases
- Quarterly maintenance
- After significant documentation changes
- When user requests docs validation


## Validation Process

### Step 1: Choose Scope

Ask user: Validate `docs/`, `wiki/`, or both?


### Step 2: Index Cross-Check

**Check platform index matches actual sections:**
```
1. Read [platform]-index.md
2. Read [platform]-development.md (and other platform files)
3. Compare listed sections vs actual H2 headers
4. Report missing or extra sections
```

**Check subagents index:**
```
1. Glob: docs/subagents/*.md
2. Read subagents/index.md
3. Compare listed agents vs actual files
4. Report missing or unlisted agents
```

**Check wiki index:**
```
1. Read wiki location from docs/wiki.md
2. Glob: ../[wiki-folder]/*.md
3. Read wiki index (_Sidebar.md or similar)
4. Compare listed pages vs actual files
```


### Step 3: Link Validation

**Find all internal links:**
```
Grep pattern: \[.*\]\((?!http)[^)]+\)
```

**For each link:**
1. Extract target path
2. Check if file exists
3. If anchor link (#section), verify section exists
4. Report broken links with file:line


### Step 4: Orphan Detection

**Find unreferenced files:**
```
1. Glob: docs/**/*.md
2. For each file, grep all other files for references
3. Files with zero references (except index files) are orphans
4. Report orphans
```


### Step 5: Duplicate Detection

**Check for repeated content patterns:**
- Same code blocks in multiple files
- Same explanatory paragraphs
- Tables with overlapping data

**Common duplication locations:**
- 3-question test (should be in INFORMATION_MINIMALISM.md only)
- Test categories (should be in [platform]-testing.md only)
- Workflow steps (should be in CODING_GUIDELINES.md only)


### Step 6: File Organization

**Check file lengths:**
```
For docs/: warn if > 200 lines
For wiki/: warn if > 600 lines
```

**Check naming convention:**
- UPPERCASE.md = templates/meta files
- lowercase.md = content files
- [platform]-*.md = platform-specific


### Step 7: Wiki Structure Check

**Verify behavior-first structure (wiki only):**

For each wiki page (except Home, README, _Sidebar):
1. Check for "## What It Does" section near top
2. Check for "## Why It Matters" section
3. Check for "## Android Implementation" section (if platform content exists)
4. Check for "## iOS Implementation" section (placeholder if Android exists)
5. Grep for `INTENT:` or `PLATFORM:` in headings — should not exist

**Report issues:**
- Missing required sections
- INTENT/PLATFORM markers still in headings
- Platform content outside implementation sections


### Step 8: Staleness Check

**Check Last Updated dates:**
```
Grep pattern: \*\*Last Updated:\*\* (\d{4}-\d{2}-\d{2})
```

- Flag files not updated in 30+ days
- Cross-reference with git log for actual changes


## Output Format

```markdown
## Validation Report

**Scope:** docs/ | wiki/ | both
**Date:** YYYY-MM-DD

### Critical Issues
- [ ] Issue 1 (file:line)
- [ ] Issue 2 (file:line)

### Warnings
- [ ] Warning 1
- [ ] Warning 2

### Summary
- Files checked: N
- Issues found: N
- Warnings: N
```


## Post-Validation

Ask user:
1. Fix issues now?
2. Save report to `docs/project/validation-report.md`?
3. Create GitHub issues for each problem?


## Key Files

| File | Purpose |
|------|---------|
| `docs/INDEX.md` | Main docs navigation |
| `docs/[platform]-index.md` | Platform docs index |
| `docs/subagents/index.md` | Subagents index |
| `docs/wiki.md` | Wiki location reference |


**Last Updated:** 2026-02-06
