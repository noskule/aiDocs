# Feature Documentation Template

## When to Use a Feature Folder

**Simple feature:** Single `.md` file in `features/`
**Complex feature:** Folder in `features/` with multiple files

## Feature Folder Contents

For complex features, use a folder structure with multiple files:

**Core files:**
- `README.md` - Feature overview and purpose
- `workflow.md` - Step-by-step process (how it works end-to-end)

**Interface files:**
- `api.md` - API/programmatic interface
- `ui.md` - User interface (if applicable)
- `cli.md` - Command-line interface (if applicable)

**Implementation files:**
- `implementation.md` - Technical implementation details
- `architecture.md` - Feature-specific architectural decisions
- `data.md` - Data structures, formats, schemas

**Usage files:**
- `examples.md` - Usage examples and common patterns
- `configuration.md` - How to configure the feature
- `integration.md` - How to integrate with other systems

**Support files:**
- `troubleshooting.md` - Common issues and solutions
- `testing.md` - How to test this feature
- `security.md` - Security considerations (if applicable)

## Example Structure

```
features/translation-pipeline/
├── README.md           # What is translation pipeline?
├── workflow.md         # Source → Glossary → Translate → Output
├── api.md              # TranslationService API
├── configuration.md    # Engines, languages, glossary setup
├── troubleshooting.md  # API failures, rate limits
└── examples.md         # Common translation patterns
```

## Principle

Files represent **what users/developers need to know**, not how code is organized.

---

**Last Updated:** 2025-11-08
