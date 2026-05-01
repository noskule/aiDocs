# documentation

Action checklist for writing or updating documentation.

**Trigger:** When creating or updating docs, wiki pages, or code comments.

## Before Writing

Run the 3-question Information Minimalism test (full framework: [`INFORMATION_MINIMALISM.md`](../INFORMATION_MINIMALISM.md)):
1. Would a skilled developer need this? (No → don't write it)
2. Is it obvious from code, naming, or structure? (Yes → don't write it)
3. Does it duplicate existing content? (Yes → reference instead)

## Determine Placement

| Content type | Location |
|-------------|----------|
| Intent, rationale, edge cases | Code comments / docstrings |
| Developer operations, platform guides | `docs/` |
| How software functions, domain concepts | Wiki |

For detailed conventions per level, see [`DOCUMENTATION_GUIDELINES.md`](../DOCUMENTATION_GUIDELINES.md).

## When Writing New Docs

1. Apply the 3-question test
2. Determine correct location using placement rules above
3. Write the content
4. Update the relevant index (INDEX.md, [platform]-index.md, or wiki index)
5. Add `**Last Updated:** YYYY-MM-DD` at the bottom

## When Updating Existing Docs

1. Read existing content first
2. Make targeted changes — don't rewrite surrounding text
3. Update the Last Updated date
4. Check if index entries still match
