# Documentation

Development guidelines, skills, and agents (lives in repo).

**LLMs:** Start at [AGENTS.md](AGENTS.md)

**Navigation:** See [INDEX.md](INDEX.md) for full contents


## Project

**Name:** [Your Project Name]

**Description:** [Brief description of what your project does]

**Audience:** Developers and LLMs


## Data Flow: LLM File Reading Order

How files are loaded — mandatory reads first, then situational reads on demand:

```mermaid
flowchart TD
    START([Session Start]) --> M1

    subgraph startup ["Always Read (startup, in order)"]
        M1["1. AGENTS.md"] --> M2["2. INDEX.md"]
        M2 -.->|if exists| M3["3. [platform]-index.md"]
        M2 -.->|if exists| M4["4. Wiki index"]
    end

    M2 --> SIT{{"What situation?"}}

    SIT -->|"Writing code"| CODE["[platform]-architecture-rules.md<br>[platform]-development.md"]
    SIT -->|"Writing tests"| TEST["[platform]-testing.md"]
    SIT -->|"Writing docs"| DOCS["DOCUMENTATION_GUIDELINES.md"]
    SIT -->|"Setting up"| SETUP["[platform]-installation.md"]
    SIT -->|"Validating docs"| VDOC["/validate-docs skill"]
    SIT -->|"Creating agents"| AREADME["creating-agents.md"]
    SIT -->|"Running a job"| JOBS["tools/JOBS.md"]
    SIT -->|"Unsure"| USER(["Ask the user"])

    classDef always fill:#c8e6c9,stroke:#4caf50,color:#1b5e20
    classDef optional fill:#fff9c4,stroke:#fbc02d,color:#f57f17
    classDef conditional fill:#bbdefb,stroke:#1976d2,color:#0d47a1
    classDef decision fill:#fff,stroke:#616161,color:#212121

    class M1,M2 always
    class M3,M4 optional
    class CODE,TEST,DOCS,SETUP,VDOC,AREADME,JOBS conditional
    class SIT decision
```

Green = always read | Yellow = read if exists | Blue = read when situation occurs

Skills auto-trigger from `.claude/skills/` — see [AGENTS.md](AGENTS.md) Skills section.


## Wiki

**Location:** See [wiki.md](wiki.md) for setup and index file location

**File organization:**
- File naming: `[section]-[topic].md` (e.g., `architecture-overview.md`, `features-authentication.md`)
