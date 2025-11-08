# Documentation Guide

## Overview

A **documentation template** optimized for AI-assisted development:

- **LLM-Friendly:** Structured for AI coding assistants with dedicated behavioral instructions
- **Feature-First:** Organized by what software does, not code structure
- **AI-Documented:** Designed for human + LLM collaboration
- **Portable:** Copy entire `docs/` folder to any project

## File Naming Convention

**UPPERCASE** = Template/meta/reference files (describe structure, not content):
- `README.md` - Meta descriptions (what something IS FOR)
- `AGENTS.md`, `CODING_GUIDELINES.md` - Templates for all projects
- `CONTENT_OWNERSHIP.md` - Reference guide
- `VALIDATION.md` - Quality validation checklist
- `features/TEMPLATE.md` - Feature structure guide

**lowercase** = Content files (actual project data):
- `architecture.md`, `installation.md`, `usage.md`, `testing.md`
- `project/roadmap.md`, `project/tasks.md`, `project/worklog.md`, `project/changelog.md`
- `features/[name].md`, `fundamentals/[topic].md`

**Rule:** UPPERCASE = describes structure/process, lowercase = actual content

## Feature-Driven Approach

**Organize by features (what software does), not code structure (how it's built).**

- `features/` - Cross-cutting features, user-facing functionality, complete workflows
- `fundamentals/` - Core concepts, architectural patterns, domain knowledge

**Examples:**
- ✅ `features/translation-pipeline/` - How translation works across components
- ✅ `fundamentals/manual-types.md` - Concept of manual types
- ❌ `backend/translator.md` - Code-driven (avoid)

**For complex features:** See [features/TEMPLATE.md](features/TEMPLATE.md) for folder structure guide

**Note:** For projects with extensive testing needs, expand `testing.md` → `testing/` folder (strategy.md, coverage.md, e2e.md, etc.)



## Complete Structure

```
PROJECT_ROOT/
├── README.md                     # Project overview (manual, project-specific)
│
└── docs/
    ├── README.md                 # This file - documentation guide
    ├── AGENTS.md                 # LLM behavioral instructions
    ├── CODING_GUIDELINES.md      # Development and documentation rules
    ├── CONTENT_OWNERSHIP.md      # Detailed ownership reference
    ├── VALIDATION.md             # Quality validation checklist (run regularly)
    ├── architecture.md           # System design & tech stack
    ├── installation.md           # Setup and prerequisites
    ├── usage.md                  # Usage guide and key files
    ├── testing.md                # Testing guide
    │
    ├── features/                 # Feature-driven documentation
    │   ├── TEMPLATE.md           # Feature folder structure guide
    │   ├── [feature].md          # Simple feature (single file)
    │   └── [feature]/            # Complex feature (folder)
    │       ├── README.md         # Feature overview
    │       ├── implementation.md # How it's implemented
    │       └── examples.md       # Usage examples
    │
    ├── fundamentals/             # Core concepts
    │   └── [topic].md            # Fundamental topics
    │
    └── project/                  # Project management
        ├── README.md             # Meta: what this folder is FOR
        ├── roadmap.md            # Strategic planning (quarters/years)
        ├── tasks.md              # Approved work (ready to start)
        ├── worklog.md            # Daily execution (session logs)
        └── changelog.md          # Release history (shipped features)
```

## Content Ownership

**Principle:** Each piece of information lives in **exactly ONE location**. Reference, never duplicate.

**Detailed ownership table:** See [CONTENT_OWNERSHIP.md](CONTENT_OWNERSHIP.md)

---

## Using with GitHub

**docs/project tracks the complete workflow:**

**Workflow:** PLAN → APPROVE → EXECUTE → DELIVER → DOCUMENT

- `roadmap.md` - Strategic planning (quarterly goals, major initiatives)
- `tasks.md` - Approved work queue (concrete tasks ready to start)
- `worklog.md` - Daily execution (session logs, blockers, progress)
- `changelog.md` - Release history (shipped features after PR merge)

**Process:**
1. Plan → Add to roadmap.md
2. Approve → Discuss → Add to tasks.md
3. Execute → Work → Log in worklog.md
4. Deliver → PR → Merge
5. Document → Remove from tasks.md → Add to changelog.md

**Complements GitHub:** Issues for bugs, Projects for sprint planning, PRs for review

---

## Principles

1. **Single Source of Truth** - Each fact lives in ONE place
2. **Mandatory Documentation** - Features/architecture changes require doc updates
3. **Updated with Code** - Documentation in same commit, not afterthought
4. **Simple Structure** - Clear names, flat hierarchy, good cross-linking



## Quick Reference

- **Installation issues?** → [installation.md](installation.md#troubleshooting)
- **How to use?** → [usage.md](usage.md)
- **How does it work?** → [architecture.md](architecture.md)
- **Development rules?** → [CODING_GUIDELINES.md](CODING_GUIDELINES.md)
- **Testing?** → [testing.md](testing.md)

---

**Last Updated:** 2025-11-06
