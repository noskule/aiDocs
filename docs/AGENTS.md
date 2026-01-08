# AI Agent Guidelines

**Audience:** AI coding assistants (LLMs) working on this project

Behavioral instructions and workflow for AI assistants. This is a project-independent template.


## Memorize for Session

Retain these for orientation throughout the session:
- This file (AGENTS.md) - workflow and situational references
- [INDEX.md](INDEX.md) - documentation map
- `[platform]-index.md` - platform documentation map (if exists)


## Situational References

Read these **when you reach that situation**, not upfront:

| When you're...          | Read...                       |
|-------------------------|-------------------------------|
| Finding platform docs   | `[platform]-index.md`         |
| Setting up / installing | `[platform]-installation.md`  |
| Writing code            | `[platform]-development.md`   |
| Writing tests           | `[platform]-testing.md`       |
| Writing documentation   | `DOCUMENTATION_GUIDELINES.md` |
| Validating docs         | `VALIDATION.md`               |
| Starting a task         | `CODING_GUIDELINES.md`        |
| Unsure about approach   | Ask the user                  |

**Don't know which doc?** Check [INDEX.md](INDEX.md) for section headers.


## Workflow Overview

Follow the complete workflow in [CODING_GUIDELINES.md](CODING_GUIDELINES.md). Summary:

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


**Last Updated:** 2026-01-08
