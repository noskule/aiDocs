# AI Agent Guidelines

**Audience:** AI coding assistants (LLMs) working on projects using this template.

Behavioral instructions and workflow for AI assistants. This is a project-independent template.

---

## Mandatory Reading

**Before ANY work, read these files:**

1. **[CODING_GUIDELINES.md](CODING_GUIDELINES.md)** - Development workflow (MANDATORY)
2. **Platform-specific setup** - Build/test commands for your platform (if exists)

---

## Workflow Overview

Follow the complete workflow in CODING_GUIDELINES.md. Summary:

```
1. Create branch
2. Implement code
3. Write tests (if required)
4. Run tests - ALL must pass
5. Report to user for review
6. User reviews and tests
7. Write documentation (AFTER user approval)
8. Create pull request
9. User merges PR
10. Capture technical discoveries
11. Continue
```

**Details for each step:** See CODING_GUIDELINES.md

---

## Situational References

Read these **when you reach that situation**, not upfront:

| When you're... | Read... |
|----------------|---------|
| Setting up / building | Platform-specific dev guide (e.g., `android-development.md`) |
| Writing tests | Platform-specific dev guide + `testing.md` |
| Deciding what to document | CODING_GUIDELINES.md → "When to Document" |
| Writing documentation | CONTENT_OWNERSHIP.md → where content belongs |
| Creating a PR | CODING_GUIDELINES.md → "Pull Request Requirements" |
| Unsure about approach | Ask the user |

---

## LLM Behavioral Instructions

### Always Check Existing Solutions First

Before implementing anything:
1. Search codebase for similar patterns (Grep/Glob)
2. Check documentation for existing approaches
3. Ask: "Is there a better way using what we already have?"

### Progress Reporting

After implementing code and tests, report to user:

```
✅ Code implemented: [brief description]
✅ Tests written: [coverage summary]
✅ All tests passing: [results]

Ready for your review and testing.
```

### When to Ask the User

Ask before proceeding when:
- Architecture decision needed
- Multiple valid approaches exist
- Requirements are unclear
- Breaking changes required
- Adding new dependencies
- Unsure about expected behavior

### Documentation Timing

**CRITICAL:** Only write documentation AFTER user approves the implementation.

1. Implement code → 2. User tests → 3. User approves → 4. THEN document

Never document before approval - implementation may change.

---

## Critical Constraints

### NEVER:
- ❌ Commit code without passing tests
- ❌ Proceed without user approval at checkpoints
- ❌ Skip checking for existing solutions
- ❌ Create PR before user approves code/tests
- ❌ Duplicate documentation content (reference instead)
- ❌ Document before user approval

### ALWAYS:
- ✅ Check for existing solutions first
- ✅ Report and wait after code/tests ready
- ✅ Include summarized prompts in PRs
- ✅ Reference docs instead of duplicating

---

## Best Practices

### DO:
- ✅ Read existing code before writing new code
- ✅ Follow existing patterns and conventions
- ✅ Write tests for new functionality
- ✅ Update documentation with code changes
- ✅ Run build and tests before requesting review
- ✅ Keep changes focused and atomic

### DON'T:
- ❌ Commit directly to main/master
- ❌ Skip tests for new features
- ❌ Skip documentation for significant changes
- ❌ Mix unrelated changes in one commit
- ❌ Guess when you should ask

---

## Information Minimalism

Before documenting anything, apply the 3-question test (see INFO_MIN_TEST.md):

1. Would a skilled developer need this? (NO → Don't document)
2. Is it obvious from code/structure? (YES → Don't document)
3. Does it duplicate existing content? (YES → Reference, don't duplicate)

---

## Resources

- [CODING_GUIDELINES.md](CODING_GUIDELINES.md) - Complete workflow
- [CONTENT_OWNERSHIP.md](CONTENT_OWNERSHIP.md) - Where content belongs
- [INFO_MIN_TEST.md](INFO_MIN_TEST.md) - Documentation decision framework
- Platform-specific guide - Build, test, patterns for your platform

---

**Last Updated:** 2025-12-21
