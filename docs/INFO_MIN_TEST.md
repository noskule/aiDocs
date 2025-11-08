# The Information Minimalism Test

**A 3-question framework to decide what to document**

Inspired by "no part is the best part" - the best documentation is often no documentation.

---

## The Test

Before adding any documentation, ask these 3 questions in order:

### 1. Would a skilled developer need this?

- **NO** → Don't document it
- **YES** → Continue to question 2

### 2. Is it obvious from structure/code/naming?

- **YES** → Don't document it
- **NO** → Continue to question 3

### 3. Does it duplicate existing content?

- **YES** → Reference instead, don't duplicate
- **NO** → Document it ✅

---

## Examples

| Documentation Candidate | Q1: Need? | Q2: Obvious? | Q3: Duplicate? | Decision |
|------------------------|-----------|--------------|----------------|----------|
| Quick Reference section linking to files | NO | - | - | ❌ Don't document |
| Why JWT over sessions | YES | NO | NO | ✅ Document |
| How to run `pytest` | NO | - | - | ❌ Don't document |
| Custom timing model rationale | YES | NO | NO | ✅ Document |
| Installation prerequisites | YES | NO | NO | ✅ Document |
| Git commit command syntax | NO | - | - | ❌ Don't document |
| Architecture decision (Arc42) | YES | NO | NO | ✅ Document |
| File naming pattern already in README | YES | - | YES | 🔗 Reference |

---

## When to Document

**Document:**
- Project-specific decisions and rationale
- Non-obvious architectural choices
- Configuration that affects behavior
- Design patterns unique to your project
- Trade-offs and alternatives considered
- Tribal knowledge a skilled developer would need

**Don't document:**
- Obvious things (standard commands, basic syntax)
- Information already in structure/naming
- Details any experienced engineer would know
- Duplicate content (reference instead)

---

## Underlying Principle

> "Document what a seasoned developer would need to reconstruct the project - skip what they already know."

This test operationalizes **Information Minimalism**: each piece of documentation must earn its place by adding unique, non-obvious value.

---

## Benefits

✅ **Prevents bloat** - Stops redundant content at the source
✅ **Saves time** - Less documentation to write and maintain
✅ **Improves clarity** - Signal-to-noise ratio stays high
✅ **LLM-friendly** - Simple yes/no decision tree
✅ **Actionable** - Clear framework, not vague "be minimal"

---

## Real-World Usage

This test was created for the [aiDocs](../README.md) LLM-optimized documentation template and has been used to:
- Remove Quick Reference sections (duplicated structure diagrams)
- Eliminate verbose installation steps (obvious to skilled developers)
- Condense validation checklists (removed explanatory prose)
- Reduce file sizes by 50%+ while improving clarity

---

## Integration

**For projects:**
- Add this test to your CODING_GUIDELINES or CONTRIBUTING guide
- Use during code reviews: "Does this pass the 3-question test?"
- Apply to existing docs during refactoring

**For AI assistants:**
- Reference this test when writing documentation
- Apply during validation passes
- Use as decision framework for what to generate

---

## Credits

**Created by:** Human-AI collaboration (2025)
- Conceptualized and refined through iterative development
- Formalized during creation of the aiDocs template
- Inspired by the "no part is the best part" engineering principle

**Authors:**
- Benjamin Behringer - Original concept and practical refinement
- Claude (Anthropic) - Framework formalization and documentation

Part of the **aiDocs** LLM-optimized documentation template:
- [Full Template](../README.md)
- [Documentation Standards](README.md#documentation-standards)
- [Coding Guidelines](CODING_GUIDELINES.md#information-minimalism-test)

---

**Version:** 1.0
**Last Updated:** 2025-11-08
**License:** Public Domain (CC0) - use freely
