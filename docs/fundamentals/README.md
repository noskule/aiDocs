# Fundamentals Folder

**Purpose:** This folder contains documentation for core concepts, architectural patterns, and domain knowledge that underpin the entire project.

**Why this exists:** Understanding fundamental concepts is essential for making sense of features, architecture decisions, and code organization.

---

## What Goes in fundamentals/

**Fundamental documentation explains:**
- Core concepts and terminology (domain-specific knowledge)
- Design principles and patterns (guiding philosophies)
- Key abstractions (how we model the problem space)
- Architectural patterns (reusable solutions)
- Domain knowledge (business rules and context)

**Examples:**
- Manual types (Superadmin, Technician, User - what they are, why they matter)
- Language handling (how multilingual content is managed)
- Wiki structure (how documentation is organized)
- State management patterns (global vs local state)
- Authentication model (sessions, tokens, permissions)

---

## Organization Pattern

**Use individual files for each topic:**

```
fundamentals/
├── manual-types.md
├── language-handling.md
├── wiki-structure.md
├── state-management.md
└── authentication-model.md
```

**Each file should:**
- Explain the concept clearly (what it is)
- Explain the rationale (why it matters)
- Show how it's used (where it appears in the system)
- Link to related features and architecture

**Keep it focused:** One concept per file, <200 lines, <1000 words

---

## Relationship with Other Documentation

**fundamentals/ vs architecture.md:**
- architecture.md = System design, tech stack, component relationships
- fundamentals/ = Core concepts that inform architectural decisions

**fundamentals/ vs features/:**
- fundamentals/ = Core CONCEPTS (manual types, authentication model)
- features/ = What the software DOES (translation, export, auth workflow)

**Example:**
- `fundamentals/authentication-model.md` = What is a session? What is a token? Why this model?
- `features/authentication/` = How login works, API endpoints, configuration

**fundamentals/ vs CODING_GUIDELINES.md:**
- CODING_GUIDELINES.md = Process and workflow (when/how to document)
- fundamentals/ = Domain concepts and patterns (what to understand)

---

## Guidelines

**Keep it conceptual:**
- Focus on understanding, not implementation
- Explain "why" and "what," not detailed "how"
- Include diagrams or examples where helpful
- Link to features that use the concept

**Keep it LLM-friendly:**
- Target: <200 lines per file
- Target: <1000 words per file
- Use clear headings (max 3 levels: H1 → H2 → H3)
- Provide context and rationale
- Cross-reference related docs

**Focus on reconstruction:**
Document core concepts a seasoned developer would need to understand the system's design philosophy and make consistent decisions.

---

## When to Create a Fundamental

Create a fundamentals/ document when:
- A concept is used across multiple features or modules
- Understanding requires domain knowledge (not obvious from code)
- Design decisions are based on this concept
- New developers would benefit from explicit explanation
- The concept influences architecture or feature design

**Don't create fundamentals for:**
- Implementation details (put in code comments)
- Feature-specific workflows (put in features/)
- Process documentation (put in CODING_GUIDELINES.md)
- Project-specific data (put in architecture.md)

---

**Last Updated:** 2025-11-08