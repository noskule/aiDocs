# Documentation

Development guidelines and templates (lives in repo).

**LLMs:** Start at [AGENTS.md](AGENTS.md)

**Navigation:** See [INDEX.md](INDEX.md) for full contents


## Project

**Name:** [Your Project Name]

**Description:** [Brief description of what your project does]

**Audience:** Developers and LLMs


## Wiki

**Location:** [GitHub Wiki](../../wiki)

**Access:**
```bash
# Clone wiki for local editing (GitHub)
gh repo clone [org]/[repo].wiki

# Or via git
git clone https://github.com/[org]/[repo].wiki.git
```

**Index file:** `_Sidebar.md` (GitHub Wiki) or platform-specific

**File organization:**
- File naming: `[section]-[topic].md` (e.g., `architecture-overview.md`, `features-authentication.md`)
- Sidebar uses H2 (`##`) for sections, links for pages

**Alternative locations:**
- GitHub Wiki: `../../wiki` or `https://github.com/[org]/[repo]/wiki`
- Confluence: `https://[company].atlassian.net/wiki/spaces/[space]`
- Notion: `https://notion.so/[workspace]/[page]`