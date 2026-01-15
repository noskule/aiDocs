# Documentation Validation Checklist

Run before major releases or quarterly. Apply to docs/ or wiki/.


## How to Use

1. Choose scope:
    1. `docs/`
    2. `wiki`
2. Update index files first (`[platform]-index.md`, wiki index per `README.md`)
3. Check each criterion
4. Report issues found (CLI summary)
5. Fix or track: fix immediately, save report, or create GitHub issues

**LLM Behavior:** After validation, ask user:
- Fix issues now?
- Save report to `docs/project/validation-report.md`?
- Create GitHub issues for each problem?


## Index Cross-Check

Verify indexes reflect actual content:
- [ ] `[platform]-index.md` matches platform file sections
- [ ] Wiki index matches wiki pages (see `README.md` for wiki location)


## File Organization

- [ ] Each file has single, clear purpose
- [ ] File length < 200 lines (docs/) or < 600 lines (wiki/)
- [ ] UPPERCASE = templates, lowercase = content
- [ ] Related content grouped logically


## Structure & Scannability

- [ ] Max 4 heading levels (H1 → H2 → H3 → H4)
- [ ] Clear, descriptive headers
- [ ] Bullet points for lists
- [ ] Tables for comparisons
- [ ] No walls of text (< 5 line paragraphs)
- [ ] Code blocks properly formatted


## Navigation

- [ ] All internal links work
- [ ] Index file current (see `README.md` for wiki index)
- [ ] "See X for details" pattern used consistently
- [ ] No orphan pages (unreachable from navigation)


## Single Source of Truth

- [ ] No duplicated information
- [ ] References used instead of copying
- [ ] Content ownership clear (one topic = one location)


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


**Last Updated:** 2026-01-08