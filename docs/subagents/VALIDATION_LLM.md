# VALIDATION_LLM

Tests whether documentation actually works for LLMs by introducing a fresh agent to the project and verifying its understanding.


## Purpose

Integration test for the documentation system. While VALIDATION_DOCS checks structural correctness (links, indexes, orphans), this agent tests **effectiveness** — can an LLM navigate the docs and come out with correct project understanding?


## Responsibilities

- Introduce a fresh LLM to the project via the standard entry point (AGENTS.md)
- Generate project-specific knowledge questions
- Evaluate LLM responses against expected answers
- Identify navigation gaps where the LLM gets lost
- Report documentation blind spots


## When to Invoke

- After major documentation restructuring
- When setting up aiDocs in a new project
- Onboarding verification (does the docs structure work?)
- When user requests LLM readiness check


## Validation Process

### Step 1: Prepare Ground Truth

Before testing, build expected answers from the documentation:

```
1. Read [platform]-development.md → extract tech stack, architecture
2. Read [platform]-testing.md → extract test commands, structure
3. Read CODING_GUIDELINES.md → extract workflow steps
4. Read DOCUMENTATION_GUIDELINES.md → extract documentation rules
5. Read subagents/index.md → extract available agents
6. Read wiki index (if exists) → extract domain concepts
```

Compile a question-answer set from this content.


### Step 2: Define Knowledge Questions

Generate questions across these categories:

**Navigation (can it find things?):**
- "What's the tech stack?"
- "Where are test commands documented?"
- "What sub-agents are available?"

**Workflow (does it understand the process?):**
- "What steps do you follow when starting a new task?"
- "When should you ask the user before proceeding?"
- "How do you create a pull request?"

**Documentation (does it know the rules?):**
- "Where do you document a new feature?"
- "What's the information minimalism test?"
- "When should you use INTENT vs PLATFORM markers?"

**Domain (does it understand the project?):**
- Project-specific questions derived from wiki/feature docs
- Architecture questions from development docs
- Questions about constraints and rationale found in code


### Step 3: Run the Test

```
1. Spawn a fresh agent (Task tool) with ONLY the instruction:
   "Read docs/AGENTS.md and follow its instructions.
    Then answer the following questions: [questions]"
2. The agent must navigate docs naturally — no hints
3. Collect all answers
```


### Step 4: Evaluate Responses

For each answer, classify:

| Result | Meaning |
|--------|---------|
| **Correct** | LLM found the right information and answered accurately |
| **Partial** | LLM found some info but missed key details |
| **Wrong** | LLM gave incorrect information |
| **Not Found** | LLM couldn't locate the information |

**Not Found** and **Wrong** indicate documentation gaps.
**Partial** may indicate information is scattered or unclear.


### Step 5: Diagnose Gaps

For each failed question, trace the navigation path:

```
1. What was the expected path? (AGENTS.md → situational ref → target doc)
2. Where did the LLM deviate?
3. Why? (missing link, unclear reference, wrong index entry, ambiguous wording)
4. What fix would close the gap?
```


## Output Format

```markdown
## LLM Knowledge Test Report

**Date:** YYYY-MM-DD
**Questions tested:** N

### Results Summary
- Correct: N/N
- Partial: N/N
- Wrong: N/N
- Not Found: N/N

### Failed Questions

#### Q: [question]
- **Expected:** [correct answer + source file]
- **LLM answered:** [what the LLM said]
- **Classification:** Wrong | Not Found | Partial
- **Root cause:** [why the LLM failed]
- **Fix:** [suggested documentation change]

### Navigation Gaps
- [List of missing links, unclear references, dead ends]

### Recommendations
- [Prioritized list of documentation improvements]
```


## Post-Validation

Ask user:
1. Fix navigation gaps now?
2. Save report to `docs/project/validation-llm-report.md`?
3. Re-run after fixes to verify improvement?


## Key Files

| File | Purpose |
|------|---------|
| `docs/AGENTS.md` | Entry point being tested |
| `docs/INDEX.md` | Navigation map |
| `docs/[platform]-*.md` | Platform docs (test targets) |
| `docs/subagents/index.md` | Agent registry |


**Last Updated:** 2026-02-08
