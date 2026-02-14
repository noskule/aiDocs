# Coding Guidelines

Scope: Applies to all code changes in this repository.


## Development Workflow

### 1. **Create Feature Branch**

```bash
git checkout -b feature/descriptive-name
```

### 2. **Implement Code**

- Flag problematic patterns in existing code to the user
- Keep changes focused and atomic
- Never commit directly to main/master

**Ask before proceeding when:**
- Architecture decision or multiple valid approaches
- Requirements unclear or ambiguous
- Breaking changes, new dependencies, or API changes
- Unsure about expected behavior



### 3. **Write Tests**

Test coverage is risk-driven. If a change requires documentation per `DOCUMENTATION_GUIDELINES.md`, it requires tests too.

**Requires tests:** new features, complex bug fixes, refactoring, public API changes.
**Skip tests:** trivial changes (typos, comments, formatting), documentation-only changes.

### 4. **Run Tests**

See `[platform]-testing.md` for test commands.

Verify all tests pass and coverage is appropriate for the risk level.

### 5. **Report to User for Review**

**LLM Behavior:** Inform user with: what was implemented, test results, what to manually test and expected behavior, link to `[platform]-testing.md`.

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

## Data Persistence

**Persistence changes:** Follow platform-specific data retention rules in `[platform]-development.md`.


**Last Updated:** 2026-02-14
