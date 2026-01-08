# Documentation Validation Checklist

Run before major releases or quarterly. Apply to docs/ or wiki/.


## How to Use

1. Choose scope: `docs/` or `wiki/`
2. Check each criterion
3. Fix issues found
4. No need to save results - validation is a process, not a document


## Structure & Scannability

- [ ] Max 3 heading levels (H1 → H2 → H3)
- [ ] Clear, descriptive headers
- [ ] Bullet points for lists
- [ ] Tables for comparisons
- [ ] No walls of text (< 5 line paragraphs)
- [ ] Code blocks properly formatted


## File Organization

- [ ] Each file has single, clear purpose
- [ ] File length < 200 lines (docs/) or < 300 lines (wiki/)
- [ ] UPPERCASE = templates, lowercase = content
- [ ] Related content grouped logically


## Navigation

- [ ] All internal links work
- [ ] Index file current (INDEX.md or _Sidebar.md)
- [ ] "See X for details" pattern used consistently
- [ ] No orphan pages (unreachable from navigation)


## Single Source of Truth

- [ ] No duplicated information
- [ ] References used instead of copying
- [ ] Content ownership clear (one topic = one location)

## Index Cross-Check
Verify indexes reflect actual content:
- [ ] `[platform]-index.md` matches platform file sections
- [ ] Wiki index matches wiki pages (see `project.md` for wiki location)

## LLM Optimization

- [ ] Workflow steps numbered
- [ ] Constraints clearly marked
- [ ] Examples provided for complex concepts
- [ ] File naming convention followed


## Human Readability

- [ ] Progressive disclosure (overview → details)
- [ ] Consistent terminology
- [ ] Context provided (why, not just what)
- [ ] Scannable for quick answers


## Completeness

- [ ] All required sections present
- [ ] Last Updated dates current
- [ ] No broken references to deleted content
- [ ] Platform-specific content in platform files


**Last Updated:** 2026-01-07
