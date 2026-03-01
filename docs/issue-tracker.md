# Issue Tracker

Project management using GitHub Issues and Projects v2.

## Conventions

Issue types, labels, and project fields are discoverable from GitHub directly. The agent reads them via the GraphQL API. These are the workflow rules that aren't obvious from the UI:

1. **Use issue types** (Bug, Feature, Task, etc.) for classification — not labels
2. **Use labels** for the feature area the issue touches
3. **Label the feature, not the data.** Most issues need one label. A backup feature that backs up training data is `backup` — not `backup` + `training`
4. **Use the sub-issue feature** to link children to epics — not just tasklist checkboxes
5. **Add every issue to the project**
6. **Set sprint status** to Backlog unless otherwise stated
7. **Always estimate** using Fibonacci story points

### Estimate Scale

| Points | Complexity |
|--------|-----------|
| 1 | Trivial — config change, copy fix |
| 2 | Small — single file, data already available |
| 3 | Medium — new component, aggregation logic |
| 5 | Large — DB migration, new data capture, multi-file |
| 8 | XL — architectural change, cross-cutting concern |

## Issue Structure

The `issue-writer` agent handles section structure per type. These are the required sections:

| Type | Required Sections |
|------|------------------|
| Feature | What It Does, Why It Matters, Implementation Plan, Acceptance Criteria |
| Bug | Observed Behavior, Expected Behavior, Steps to Reproduce |
| Epic | Overview, Phases (with sub-issue links), Dependencies |
| Spike | Question, Context, Timebox, Expected Output |
| Task | What, Why, Scope |

Optional sections added when relevant: Data Model Changes, Scientific Basis, Confounders.

### Title Format

Imperative verb + concise description. "Add threshold trend chart", not "threshold chart feature".

## Wiki Mapping

When closing an issue that adds significant functionality, update the corresponding wiki page. Issue labels map to wiki sections — check the wiki sidebar for the relevant page.
