# architecture-rules

Enforces architecture principles when implementing features or writing new code. Prevents code duplication and layer violations.

**Trigger:** Automatically before writing new code or implementing features.

## Before Writing Code

1. **Read** `docs/[platform]-architecture-rules.md`
2. **Search before implementing** — check the Reuse Rules tables for existing utilities. If the function you need exists, use it.
3. **Verify layer boundaries** — ensure imports respect the documented dependency direction
4. **Check extension points** — if adding a new type, metric, or protocol, use the documented extension mechanism
5. **Check anti-patterns** — review the anti-patterns table to avoid common mistakes
6. **Use constants** — never hard-code values that belong in a constants class

## After Completing Your Task

Scan all modified files for architecture violations against `docs/[platform]-architecture-rules.md`:

For each file, check:
- Layer boundary violations (wrong imports across layers)
- Hard-coded values that should use a constants class
- Duplicated logic that exists in the Reuse Rules table
- Anti-patterns from the anti-patterns table

Output a concise violation report. Group by severity:
- **Must fix** — active violations that cause bugs or inconsistency
- **Should fix** — technical debt worth addressing
- **Note** — minor style issues

If no violations found, report "No violations detected."
