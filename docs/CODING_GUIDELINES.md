# Coding Guidelines

Scope: Applies to all code changes in this repository.


## Development Workflow

### 1. **Create Feature Branch**

```bash
git checkout -b feature/descriptive-name
```

### 2. **Implement Code**

### DO:
- Write the feature/fix implementation
- Read existing code before writing new code
- Follow existing patterns and conventions
- Flag problematic patterns in existing code to the user
- Keep changes focused and atomic

### DON'T:
- Commit directly to main/master
- Guess when you should ask

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
![img.png](img.png)


### 3. **Write Tests**

Test coverage is risk-driven. Use judgment—new behavior or complex changes should be tested. If a change requires documentation per `DOCUMENTATION_GUIDELINES.md`, it requires tests too.

**What Requires Tests:**

- New features - Core functionality must be tested
- Bug fixes (complex) - Test the fix and prevent regression
- Refactoring - Ensure behavior hasn't changed
- Public APIs - All public interfaces need tests
- Trivial changes - Typos, comments, simple formatting
- Documentation-only changes - No code tests needed

### 4. **Run Tests**

See `[platform]-testing.md` for test commands.

Verify all tests pass and coverage is appropriate for the risk level.

### 5. **Report to User for Review**

**LLM Behavior:** Inform user that code is ready with testing instructions:

```
- Code implemented: [brief description]
- Tests written: [coverage summary]
- Tests passing: [results]

Manual testing:
- [What to test - specific to changes made]
- [Expected behavior]

How to install/run: see [platform]-testing.md

Ready for your review and testing.

```

### 6. **User Manually Tests and Reviews**

- User tests the functionality (LLM provided what to test)
- User reviews code quality and approach
- User provides feedback or approval

### 7. **Capture Technical Discoveries**

Review the development session for reusable technical knowledge:

- Platform-specific findings (sensor types, API quirks, device behaviors)
- Workarounds for undocumented issues
- Integration details (how external systems actually work)

**If discoveries exist:** Add to wiki under appropriate section.

### 8. **Write Documentation**

Update documentation per `DOCUMENTATION_GUIDELINES.md`:

- Update changelog.md with changes
- Update wiki if feature-related
- Apply Information Minimalism test

### 9. **Create Pull Request**

**LLM Behavior:** Create PR using GitHub CLI:

```bash
gh pr create --title "Feature: descriptive title" --body "$(cat <<'EOF'
## Summary
- [What was implemented]
- [Key changes]

## Testing
- [Tests added]
- [Test results]

## Documentation
- [Docs updated]

## Prompts Used
- [Summarized prompts that led to this implementation]

-- Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

### 10. **User Merges PR**

- User reviews PR on GitHub
- User merges when satisfied
- **User informs LLM:** "PR merged, continue"

### 11. **Continue**

- LLM can proceed with next tasks
- Branch is merged and cleaned up


## Data Persistence

**Persistence changes:** Follow platform-specific data retention rules in `[platform]-development.md`.


**Last Updated:** 2026-01-07
