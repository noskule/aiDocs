# AI Agent Guidelines

**Audience:** AI coding assistants (LLMs) working on this project

Behavioral instructions and workflow for AI assistants. This is a project-independent template.


## Navigation

**[INDEX.md](INDEX.md)** - Full contents of all docs (consult to find what you need)


## Situational References

Read these **when you reach that situation**, not upfront:

| When you're... | Read... |
|----------------|---------|
| Finding platform docs | `[platform]-index.md` |
| Setting up / installing | `[platform]-installation.md` |
| Writing code | `[platform]-development.md` |
| Writing tests | `[platform]-testing.md` |
| Writing documentation | `DOCUMENTATION_GUIDELINES.md` |
| Creating a PR | `CODING_GUIDELINES.md` |
| Unsure about approach | Ask the user |

**Don't know which doc?** Check [INDEX.md](INDEX.md) for section headers.


## Workflow Overview

Follow the complete workflow in CODING_GUIDELINES.md. Summary:

```
1. Create branch
2. Implement code
3. Write tests (if required)
4. Run tests - ALL must pass
5. Report to user (what to test + how via platform guide)
6. User manually tests and reviews
7. Capture technical discoveries
8. Write documentation
9. Create pull request
10. User merges PR
11. Continue
```

### Documentation Timing

**CRITICAL:** Only write documentation AFTER user approves the implementation.

1. Implement code -> 2. User tests -> 3. User approves -> 4. THEN document

Never document before approval - implementation may change.

**Details for each step:** See CODING_GUIDELINES.md


## LLM Behavioral Instructions

### When to Ask the User

Ask before proceeding when:
- Architecture decision needed (which pattern, which layer)
- Multiple valid implementation approaches exist
- Requirements are unclear or ambiguous
- Breaking changes are required
- Significant refactoring needed
- Adding new dependencies
- Changing existing APIs
- Unsure about expected behavior

### Progress Reporting

After implementing code and tests, report to user:

```
- Code implemented: [brief description]
- Tests written: [coverage summary]
- All tests passing: [results]

Ready for your review and testing.
```


## Best Practices

### DO:
- Read existing code before writing new code
- Follow existing patterns and conventions
- Write tests for new functionality
- Update documentation with code changes
- Run build and tests before requesting review
- Keep changes focused and atomic

### DON'T:
- Commit directly to main/master
- Skip tests for new features
- Skip documentation for significant changes
- Mix unrelated changes in one commit
- Document before user approval
- Guess when you should ask


## Information Minimalism

Before documenting anything, apply the 3-question test (see INFORMATION_MINIMALISM.md):

1. Would a skilled developer need this? (NO -> Don't document)
2. Is it obvious from code/structure? (YES -> Don't document)
3. Does it duplicate existing content? (YES -> Reference, don't duplicate)


**Last Updated:** 2026-01-07
