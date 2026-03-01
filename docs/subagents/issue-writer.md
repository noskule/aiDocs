# issue-writer

Creates GitHub issues following [issue-tracker.md](../issue-tracker.md) conventions.

## Workflow

1. **Discover** — read issue types, labels, and project fields from the repo via GraphQL
2. **Draft** — write title and body with sections appropriate for the type
3. **Create** — `createIssue` mutation with `repositoryId`, `issueTypeId`, `labelIds`
4. **Project** — add to project, set sprint status, priority, estimate
5. **Link** — if part of an epic, `addSubIssue` mutation

## Setup

1. Copy this file and `.claude/agents/issue-writer.md` to your project
2. Add your repository ID, project ID, and field IDs below

## IDs

> Replace with your project-specific IDs. Discover them via `gh api graphql`.

```
Repository:    <repo_id>
Owner:         <owner>
Project:       <project_id>
```

### Project Fields

Cache field and option IDs here after first discovery to avoid repeated API lookups.
