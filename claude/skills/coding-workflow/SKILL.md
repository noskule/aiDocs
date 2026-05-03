---
name: coding-workflow
description: Development workflow for implementing features and making code changes. 10-step process from feature branch to merged PR.
user-invocable: false
---

# coding-workflow

Development workflow for all code changes. Follow these steps in order.

## Step Tracking

When this workflow triggers, create a task for each of the 10 steps below using your task system. Not all steps apply to every task — mark inapplicable steps as completed immediately (e.g., skip tests for docs-only changes). Before advancing to a new step, check that prior steps are either completed or explicitly marked not applicable. If a step was skipped without acknowledgment, ask the user before proceeding.

## 1. Create Feature Branch

```bash
git checkout -b feature/descriptive-name
```

Never commit directly to main/master.

## 2. Implement Code

- Flag problematic patterns in existing code to the user
- Keep changes focused and atomic
- Read `[platform]-architecture-rules.md` before writing code (if exists)

**Ask before proceeding when:**
- Architecture decision or multiple valid approaches
- Requirements unclear or ambiguous
- Breaking changes, new dependencies, or API changes
- Unsure about expected behavior

## 3. Write Tests

Test coverage is risk-driven. If a change requires documentation, it requires tests too.

**Requires tests:** new features, complex bug fixes, refactoring, public API changes.
**Skip tests:** trivial changes (typos, comments, formatting), documentation-only changes.

See `[platform]-testing.md` for test commands and patterns.

## 4. Run Tests

Verify all tests pass and coverage is appropriate for the risk level.

## 5. Report to User for Review

Inform user with:
- What was implemented
- Test results
- What to manually test and expected behavior

## 6. User Manually Tests and Reviews

Wait for user feedback or approval before proceeding.

## 7. Capture Technical Discoveries

Review the session for reusable knowledge:
- Platform-specific findings (API quirks, device behaviors)
- Workarounds for undocumented issues
- Integration details (how external systems actually work)

**If discoveries exist:** Add to wiki under appropriate section.

## 8. Write Documentation

- Update changelog with changes
- Update wiki if feature-related
- Apply Information Minimalism test
- See `docs/DOCUMENTATION_GUIDELINES.md` for reference

## 9. Create Pull Request

Create PR with summary, testing details, and documentation changes.

## 10. User Merges PR

- User reviews and merges
- **User informs LLM:** "PR merged, continue"

## Data Persistence

Follow platform-specific data retention rules in `[platform]-development.md`.
