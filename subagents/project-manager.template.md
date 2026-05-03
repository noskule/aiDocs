# project-manager

Issue and project board management agent. Creates and manages issues following [issue-tracker.md](../issue-tracker.md) conventions.

Adapt this template for your issue tracker (GitHub Issues, Linear, Jira, etc.).

## Workflow

1. **Discover** — read issue types, labels, and project fields from the tracker API
2. **Draft** — write title and body with sections appropriate for the type
3. **Create** — create issue via API
4. **Project** — add to project board, set status, priority, estimate
5. **Link** — if part of an epic, link as sub-issue

## Setup

1. Copy this file (remove `.template` suffix) and `.claude/agents/project-manager.md` to your project
2. Add your tracker-specific IDs below

## IDs

> Replace with your project-specific IDs. Discover them via your tracker's API.

```
Repository:    <repo_id>
Owner:         <owner>
Project:       <project_id>
```

### Project Fields

Cache field and option IDs here after first discovery to avoid repeated API lookups.
