# Wiki Documentation

The software documentation (user-facing features, architecture, domain concepts) may be maintained in a separate wiki repository.

## Location

```
../<project-name>.wiki/     # Wiki repository (sibling to main project)
```

**Index file:** `_Sidebar.md` - contains the wiki navigation structure and page listing.

The wiki is a Git repository cloned alongside the main project:
- **GitHub URL:** `https://github.com/<org>/<project>.wiki.git`
- **Local path:** `../<project-name>.wiki/` (relative to project root)

## Usage

```bash
# Clone wiki (if not already present)
git clone https://github.com/<org>/<project>.wiki.git ../<project-name>.wiki

# Navigate to wiki
cd ../<project-name>.wiki

# Edit and commit changes
git add . && git commit -m "docs: Update feature X"
git push
```

## Content Guidelines

See [DOCUMENTATION_GUIDELINES.md](DOCUMENTATION_GUIDELINES.md) for what belongs in the wiki vs /docs folder.

---

**Last Updated:** 2026-01-17
