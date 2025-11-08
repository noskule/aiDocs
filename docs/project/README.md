# Project Management Folder

**Purpose:** This folder tracks the complete project workflow from planning to delivery.

**Why this exists:** Fills the gap between GitHub's features (Issues, PRs, Projects) and day-to-day development workflow.

---

## Workflow Overview

```
PLAN ’ APPROVE ’ EXECUTE ’ DELIVER ’ DOCUMENT

roadmap.md ’ tasks.md ’ worklog.md ’ (PR/merge) ’ changelog.md
```

## Files in This Folder

### `roadmap.md` - Strategic Planning
**Purpose:** Long-term vision and quarterly goals

**Contains:**
- Strategic initiatives
- Quarterly goals
- Major features (not yet approved)
- Future vision

**Update when:** Planning major features or setting quarterly goals

---

### `tasks.md` - Approved Work Queue
**Purpose:** Concrete, approved tasks ready to start

**Contains:**
- Features approved for development
- Bugs approved for fixing
- Enhancements ready to implement
- Current work in progress

**Update when:**
- User approves a task
- Work starts (move to "In Progress")
- PR is merged (remove and add to changelog.md)

---

### `worklog.md` - Daily Execution
**Purpose:** Track daily progress, blockers, and decisions

**Contains:**
- Current status
- Session-by-session logs
- Technical blockers
- Decisions made during development
- Progress updates

**Update when:**
- Starting/ending a work session
- Encountering blockers
- Making technical decisions
- Multi-day features in progress

**Why this matters:** Tracks progress between commits and PRs, especially for interrupted work or multi-day features.

---

### `changelog.md` - Release History
**Purpose:** Record of shipped features and releases

**Contains:**
- Version history
- Features shipped
- Breaking changes
- Migration guides

**Update when:**
- PR is merged
- Feature is delivered
- Version is released

---

## Relationship with GitHub

**GitHub Issues:** Bug reports, feature requests (from users/stakeholders)
**GitHub Projects:** Sprint planning, kanban boards (team coordination)
**GitHub PRs:** Code review, merge process (quality gate)

**docs/project:** Complete workflow documentation (planning ’ execution ’ delivery)

**Key difference:** GitHub tools are event-driven (issue opened, PR merged). docs/project is process-driven (plan ’ approve ’ execute ’ deliver ’ document).

---

## Examples

**Scenario 1: Planning a new feature**
1. Discuss idea with team ’ Add to `roadmap.md` under Q2 2025
2. Break down into tasks ’ User approves ’ Add to `tasks.md`
3. Start work ’ Log daily progress in `worklog.md`
4. Create PR ’ Merge ’ Remove from `tasks.md` ’ Add to `changelog.md`

**Scenario 2: Multi-day feature with interruption**
1. Working on feature ’ Logging in `worklog.md`
2. Urgent bug comes in ’ Note interruption in `worklog.md`
3. Resume feature ’ Check `worklog.md` for context
4. Complete feature ’ Create PR ’ Update `changelog.md`

**Scenario 3: Tracking decisions**
1. During development, decide to use Context API instead of Redux
2. Log decision and rationale in `worklog.md`
3. When PR is created, decision context is preserved
4. Future developers can see why decision was made

---

**Last Updated:** 2025-11-08
