# Instructions for AI Coding Assistants

**Purpose:** Mandatory behavioral instructions for AI assistants working on this project.

**Applies to:** Claude Code, GitHub Copilot, ChatGPT, and all AI coding assistants.

---

## Your Mandatory Workflow

```
FOR EVERY SIGNIFICANT CHANGE:

1. Check existing solutions (search codebase, read docs)
2. Create branch: git checkout -b feature/descriptive-name
3. Write code (follow existing patterns)
4. Write tests (risk-driven - see CODING_GUIDELINES)
5. Run tests: poetry run pytest (all must pass)
6. Report to user: "✅ Code implemented, ✅ Tests written, ✅ All passing - Ready for review"
7. WAIT for user approval (DO NOT proceed automatically)
8. Write documentation (only after approval)
9. Create PR with summarized prompts
10. WAIT for user to merge
11. Continue only after user confirms merge

NEVER SKIP STEPS
NEVER COMMIT WITHOUT TESTS
NEVER PROCEED WITHOUT USER APPROVAL
```

**Complete workflow details:** [Development Workflow](docs/CODING_GUIDELINES.md#development-workflow)

---

## Critical LLM-Specific Behaviors

### 1. Always Check for Existing Solutions First

**Before implementing anything:**
```
REQUIRED:
1. Ask: "Does this already exist in the codebase?"
2. Search for similar patterns using Grep/Glob
3. Check documentation for existing approaches
4. Ask: "Is there a better way using what we already have?"

NEVER start implementation without completing these checks.
```

### 2. Report and Wait Pattern

**You MUST explicitly:**
- **After code/tests ready:** Report status and WAIT for user to review
- **After user approval:** Write documentation, then report again
- **After PR created:** WAIT for user to merge
- **After merge:** Only continue when user confirms

**Example report:**
```
✅ Code implemented: [brief description]
✅ Tests written: [coverage summary]
✅ All tests passing

Ready for your review and testing. Please verify functionality.
```

**DO NOT proceed to next steps automatically.**

### 3. Include Summarized Prompts in PRs

**Every PR description MUST include:**
```
## Prompts Used
- [Summarized conversation that led to this implementation]
- [Key decisions made during development]
- [Alternative approaches considered]
```

This helps humans understand the AI-assisted development process.

### 4. Test Before Reporting

```
MANDATORY SEQUENCE:
1. Write code
2. Write tests
3. Run tests: poetry run pytest
4. Verify ALL pass
5. Report to user
6. NEVER report "ready" if tests fail
```

---

## Critical Constraints - NEVER Do These

❌ **NEVER commit code without passing tests**
❌ **NEVER proceed to next step without user approval**
❌ **NEVER manually update version numbers** (controlled by git tags only)
❌ **NEVER duplicate documentation content** (reference single source of truth)
❌ **NEVER skip checking for existing solutions first**
❌ **NEVER create PR before user approves code/tests**
❌ **NEVER continue after PR creation until user confirms merge**

---

## What You MUST Consult

**For "When to document/test":**
- [Coding Guidelines - When to Document](docs/CODING_GUIDELINES.md#when-to-document)
- [Coding Guidelines - Core Principle](docs/CODING_GUIDELINES.md#core-principle)

**For "Where to update docs":**
- [Coding Guidelines - Where to Update](docs/CODING_GUIDELINES.md#where-to-update)

**For "How to write code":**
- [Coding Guidelines - Complete Rules](docs/CODING_GUIDELINES.md)
- [Architecture - System Design](docs/ARCHITECTURE.md)

**For "What exists in codebase":**
- [README - Documentation Structure](README.md#documentation-structure)
- [Architecture - Components](docs/ARCHITECTURE.md#core-components)

**For testing:**
- [Testing Quick Start](docs/testing/QUICK_START.md)

---

## Key Project-Specific Rules

### Git Versioning
- ❌ **NEVER manually update version numbers**
- ✅ Version controlled by git tags only: `git tag -a v1.0.0 -m "Release"`
- See: [Architecture - Git Versioning](docs/ARCHITECTURE.md#git-versioning-workflow)

### Translation Service
- Use OpenAI GPT (`gpt-3.5-turbo`) for translations
- Always use glossary: `EINSTELLUNGEN/GLOSSARY.md` in wiki
- See: [Architecture - Translation Strategy](docs/ARCHITECTURE.md#translation-strategy)

### Dependency Management
```bash
poetry install       # Install dependencies
poetry add <pkg>     # Add new dependency
poetry run pytest    # Run tests
poetry shell         # Activate environment
```

---

## Verification Checklist

**Before reporting "ready for review":**

✅ All tests pass: `poetry run pytest`
✅ Code follows existing patterns
✅ No duplication in documentation
✅ All cross-references valid
✅ Checked for existing solutions first

---

## Core Documents Reference

**You must consult these regularly:**

- [README](README.md) - Project overview and documentation structure
- [Coding Guidelines](docs/CODING_GUIDELINES.md) - When/where/how to document and test
- [Architecture](docs/ARCHITECTURE.md) - System design, tech stack, decisions
- [Installation Guide](docs/INSTALLATION.md) - Setup and configuration
- [Usage Guide](docs/USAGE.md) - How to use the tool
- [Testing Quick Start](docs/testing/QUICK_START.md) - How to run/write tests

---

## Summary

**Your role:** Assist development by writing code and tests, but ALWAYS:
1. Check existing solutions first
2. Report and wait for user approval
3. Follow the mandatory workflow (no shortcuts)
4. Reference docs instead of duplicating
5. Include summarized prompts in PRs

**Remember:** You are an assistant, not an autonomous agent. Wait for human approval at each critical step.

---

**Last Updated:** 2025-11-06
