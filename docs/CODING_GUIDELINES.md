# Coding and Documentation Guidelines

## Core Principle

Enable a seasoned developer to reconstruct the project quickly without tribal knowledge.

**Document what a seasoned developer would want to know - skip trivial fixes.**

Document anything that would take measurable time for an experienced engineer to rediscover — configuration logic, architectural decisions, workflow setup — but skip details that are obvious or easily re-derived.

## When to Document

### ✅ Requires Documentation

- **Architectural/structural changes** - New modules, refactoring, async conversions
- **Technology/library decisions** - Choosing libraries, switching dependencies
- **Performance optimizations** - Refactoring for efficiency, caching strategies
- **Security vulnerabilities and fixes** - Any security-related changes
- **Complex logic bugs** - Hard to figure out or fix
- **Database/schema changes** - Any data structure modifications
- **New features or behavior changes** - Anything that changes user-facing behavior
- **Configuration changes** - New config options, changed defaults

### ❌ Does NOT Require Documentation

- **Typo fixes** - Error messages, comments, variable names
- **Simple bug fixes** - Off-by-one errors, null checks, obvious logic fixes
- **Code formatting** - Linting, whitespace, style adjustments
- **Trivial refactoring** - Renaming variables, extracting simple functions (no behavior change)

### Examples

| Change                                        | Document? | Why                            |
| --------------------------------------------- | --------- | ------------------------------ |
| Fix typo in error message                     | ❌ No      | Trivial                        |
| Fix off-by-one error in loop                  | ❌ No      | Simple bug                     |
| Fix logic bug that changes behavior (complex) | ✅ Yes     | Complex, affects understanding |
| Fix security vulnerability                    | ✅ Yes     | Important for security history |
| Refactor function to be more efficient        | ✅ Yes     | Performance decision           |
| Switching translation provider                | ✅ Yes     | Architectural decision         |
| Adding a new caching layer                    | ✅ Yes     | Structural change              |

## What Goes Where

**See [CONTENT_OWNERSHIP.md](CONTENT_OWNERSHIP.md) for detailed breakdown.**

**Quick summary:**

- **Documentation (docs/)** - Information to rebuild the project (architecture, installation, usage, features, fundamentals)
- **Code (docstrings, comments)** - Implementation details for developers working with the code

## Development Workflow

### 1. **Create Feature Branch**

```bash
git checkout -b feature/descriptive-name
```

###2. **Implement Code**

- Write the feature/fix implementation
- Follow existing code patterns and project conventions
- Keep changes focused and atomic

###3. **Write Tests**

**Test Coverage Requirements:**

- **Use common sense, risk-driven approach** - Not everything needs exhaustive tests
- **Consult "When to Document"** - If it requires documentation, it requires tests
- **Consult "Core Principle"** - Would a seasoned developer need tests to understand this?

**What Requires Tests:**

- ✅ New features - Core functionality must be tested
- ✅ Bug fixes (complex) - Test the fix and prevent regression
- ✅ Refactoring - Ensure behavior hasn't changed
- ✅ Public APIs - All public interfaces need tests
- ❌ Trivial changes - Typos, comments, simple formatting
- ❌ Documentation-only changes - No code tests needed

###4. **Run Tests**

```bash
poetry run pytest
poetry run pytest --cov=src --cov-report=html
```

Verify all tests pass and coverage is appropriate for the risk level.

###5. **Report to User for Review**

**LLM Behavior:** Inform the user that code and tests are ready:

```
✅ Code implemented: [brief description]
✅ Tests written: [test coverage summary]
✅ All tests passing: [test results]

Ready for your review and testing. Please verify functionality.
```

###6. **User Reviews and Tests**

- User manually tests the functionality
- User reviews code quality and approach
- User provides feedback or approval

###7. **Write Documentation** (After User Approval)

**Only after user confirms the implementation is correct:**

- Update relevant documentation (see "Where to Update" below)
- Add feature documentation if complex (see `docs/features/`)
- Include **summarized prompts** used during development
- Update changelog.md with changes
- Update "Last Updated" dates

###8. **Create Pull Request**

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

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

###9. **User Merges PR**

- User reviews PR on GitHub
- User merges when satisfied
- **User informs LLM:** "PR merged, continue"

###10. **Continue**

- LLM can proceed with next tasks
- Branch is merged and cleaned up

---

## Where to Update

| Change Type              | Update These Docs                                            |
| ------------------------ | ------------------------------------------------------------ |
| New feature              | `architecture.md` (component), `usage.md` (how to use), `changelog.md` (release notes), optionally `features/[name].md` (deep-dive) |
| Architecture change      | `architecture.md` (design section), `changelog.md` if breaking |
| Bug fix (complex)        | `architecture.md` (if design flaw), `changelog.md`           |
| Performance optimization | `architecture.md` (decision rationale)                       |
| New dependency           | `architecture.md` (tech stack + why), `installation.md` (setup) |
| Config option            | `usage.md` (configuration section), `architecture.md` (if affects design) |
| Breaking change          | `changelog.md` (migration guide), relevant doc with new behavior |
| Complex feature          | `features/[feature].md` (detailed explanation of how it works across modules) |
| New core concept         | `fundamentals/[concept].md` (explain the concept, why it matters, how it's used) |

## Pull Request Requirements

**All PRs must follow the "Complete Feature Development Process" above.**

**PRs must include:**

- ✅ Code changes (implemented and reviewed)
- ✅ Tests for new functionality (all passing)
- ✅ Updated documentation (if required by "When to Document" guidelines)
- ✅ Summarized prompts used during development (in PR description)
- ✅ Updated "Last Updated" dates

**PRs will be rejected if:**

- ❌ New features lack tests (unless trivial per "When to Document")
- ❌ Tests are not passing
- ❌ Significant changes lack documentation updates
- ❌ Architecture changes not explained in architecture.md
- ❌ Breaking changes not documented in changelog.md
- ❌ Code not reviewed by user before PR creation

---

**Last Updated:** 2025-11-06 **Maintained By:** Project Team
