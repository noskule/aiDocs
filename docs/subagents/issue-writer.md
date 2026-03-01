# issue-writer

Creates GitHub issues following project conventions.

## Purpose

Automates issue creation with correct type, labels, structure, project assignment, and estimation. Reads issue types and labels from the GitHub API so they stay in sync without manual documentation.

## Responsibilities

- Choose the correct issue type based on the work described
- Select labels by feature area (label the feature, not the data)
- Write issue body with required sections for the type
- Create the issue via GraphQL API with the correct `issueTypeId`
- Add to the project
- Set sprint status (default: Backlog), priority, and estimate
- Link as sub-issue to parent epic when applicable

## Workflow

1. **Discover** — read issue types and labels from the repo via GraphQL
2. **Draft** — write title (imperative verb) and body with required sections
3. **Create** — use `createIssue` mutation with `repositoryId`, `issueTypeId`, `labelIds`
4. **Project** — add to project, set sprint status, priority, estimate
5. **Link** — if part of an epic, use `addSubIssue` mutation

## API Reference

> **Project-specific:** Replace IDs below with your repository and project IDs.

### Discover issue types

```graphql
{ repository(owner: "<owner>", name: "<repo>") {
    issueTypes(first: 10) { nodes { id name description } }
}}
```

### Discover labels

```graphql
{ repository(owner: "<owner>", name: "<repo>") {
    labels(first: 30) { nodes { id name description } }
}}
```

### Create issue

```graphql
mutation {
  createIssue(input: {
    repositoryId: "<repo_id>",
    title: "...",
    issueTypeId: "...",
    labelIds: ["..."],
    body: "..."
  }) { issue { number url } }
}
```

### Add to project and set fields

```graphql
# Add to project
mutation { addProjectV2ItemById(input: {
  projectId: "<project_id>", contentId: "<issue_node_id>"
}) { item { id } } }

# Set field value (sprint status, priority, estimate)
mutation { updateProjectV2ItemFieldValue(input: {
  projectId: "<project_id>",
  itemId: "<item_id>",
  fieldId: "<field_id>",
  value: { singleSelectOptionId: "<option_id>" }  # or { number: N } for estimate
}) { projectV2Item { id } } }
```

### Discover project fields

```graphql
{ node(id: "<project_id>") {
    ... on ProjectV2 {
      fields(first: 30) {
        nodes {
          ... on ProjectV2Field { id name dataType }
          ... on ProjectV2SingleSelectField { id name options { id name } }
        }
      }
    }
}}
```

### Link sub-issue to epic

```graphql
mutation { addSubIssue(input: {
  issueId: "<epic_node_id>", subIssueId: "<child_node_id>"
}) { issue { number } subIssue { number } } }
```

## Required Sections per Type

| Type | Sections |
|------|----------|
| Feature | What It Does, Why It Matters, Implementation Plan, Acceptance Criteria |
| Bug | Observed Behavior, Expected Behavior, Steps to Reproduce |
| Epic | Overview, Phases (with sub-issue links), Dependencies |
| Spike | Question, Context, Timebox, Expected Output |
| Task | What, Why, Scope |

Add optional sections when relevant: Data Model Changes, Scientific Basis, Confounders, Context.

## Conventions

- **Title:** imperative verb + concise description
- **Labels:** one label (the core feature area), two only when genuinely spanning two features equally
- **Estimate:** Fibonacci (1, 2, 3, 5, 8) based on implementation complexity
- **Sprint status:** Backlog unless user specifies otherwise
- **Epic reference:** first line of body is `Part of #<epic>` when applicable
- **Dependencies:** noted as `Depends on: #<issue>` below the epic reference

## Setup

To use this agent in your project:

1. Copy this file to `docs/subagents/issue-writer.md`
2. Copy the agent wrapper to `.claude/agents/issue-writer.md`
3. Replace placeholder IDs with your repository and project IDs
4. Optionally cache field IDs in the reference doc to avoid repeated API lookups

## References

- [issue-tracker.md](../issue-tracker.md) — project conventions
- [DOCUMENTATION_GUIDELINES.md](../DOCUMENTATION_GUIDELINES.md) — information minimalism
