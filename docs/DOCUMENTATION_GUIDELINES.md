# Documentation Guidelines



## Information Minimalism

Use **Information Minimalism** as guide what to document. Use the following principle to decide if documentation is needed:

>  Document what a seasoned developer or llm would need to reconstruct the project - skip what they already know.

Additional reading ([INFORMATION_MINIMALISM.md](INFORMATION_MINIMALISM.md)) 

### Test

Before adding any documentation, ask these 3 questions in order:

#### 1. Would a skilled developer need this?

- **NO** → Don't document it
- **YES** → Continue to question 2

#### 2. Is it obvious from structure/code/naming?

- **YES** → Don't document it
- **NO** → Continue to question 3

#### 3. Does it duplicate existing content?

- **YES** → Reference instead, don't duplicate
- **NO** → Document it ✅



## Documentation Levels

**Code (docstrings, comments)**

- Implementation details, edge cases, and API behavior
- Rationale for non-obvious logic

**/docs folder**

- Repo-local developer operations (build, test, run, scripts, platform guides, releases)
- Contribution workflow and agent behavior
- Project management files under `docs/project/`

**Wiki**

- How the software works: fundamentals, architecture, features, behavior, domain concepts
- System-level documentation (not repo ops)



## Documenting in Code

Apply Information Minimalism. Document only what isn't obvious from reading the code.

### What to Document

| Type                   | When                                    | Example                                 |
| ---------------------- | --------------------------------------- | --------------------------------------- |
| **Class/module**       | Non-obvious purpose or responsibilities | `Manages BLE GATT connections...`       |
| **Public function**    | Complex signature or behavior           | `@param windowMillis Time window in ms` |
| **Inline "why"**       | Non-obvious decisions                   | `// Grace period to avoid UI flicker`   |
| **Domain knowledge**   | Values a dev wouldn't know              | `// RMSSD typically 20-200ms`           |
| **Quirks/workarounds** | Platform or device specific             | `// Coospo requires 500ms delay`        |


### Technical Debt

```
// TODO: Brief description of what's needed
// TODO(#123): With issue reference if tracked
```

### Skip

- What the code does (read the code)
- Obvious parameters (`@param id The ID`)
- Commented-out code (delete it)



## Documenting in /docs

### Index Maintenance

When adding/removing sections in any doc, update [INDEX.md](INDEX.md).

### Platform Index Maintenance

When adding/removing sections in platform files, update `[platform]-index.md`.

### File Naming Convention

**UPPERCASE** = Template/meta/reference files (describe structure, not content)

**lowercase** = Content files (actual project data)

### File Structure

See [INDEX.md](INDEX.md) for complete file list with contents.

## Documenting in Wiki

Wiki documents **what the software does** - behavior, concepts, architecture, device findings.

### Structure

| Section          | Content                      | Example                            |
| ---------------- | ---------------------------- | ---------------------------------- |
| **Fundamentals** | Domain concepts, terminology | HRV calculation, Doze mode         |
| **Architecture** | System design, data flow     | Multi-device architecture          |
| **Features**     | User-facing functionality    | Heart rate zones, template sharing |
| **Devices**      | Hardware-specific findings   | TicWatch sensors, Polar quirks     |
| **UI**           | Design concepts, patterns    | UI concept                         |

### File Naming

Use section prefix + descriptive name:

```
[section]-[subsection]-[topic].md

architecture-overview.md
features-heart_rate_zones.md
devices-wearos-ticwatch.md
devices-ble-polar.md
```

### When to Update Wiki

| Trigger                 | Action                      |
| ----------------------- | --------------------------- |
| New feature implemented | Add to Features section     |
| Architecture decision   | Add to Architecture section |
| Device/sensor discovery | Add to Devices section      |
| New domain concept      | Add to Fundamentals section |

### Sidebar Maintenance

`_Sidebar.md` is the wiki's index. Update when adding/removing pages.

(Parallel to `INDEX.md` for docs/)


## Periodic Validation

Run [VALIDATION.md](VALIDATION.md) checklist before major releases or quarterly.

Applies to both docs/ and wiki/. Not part of regular workflow - just a periodic quality check.


**Last Updated:** 2026-01-07