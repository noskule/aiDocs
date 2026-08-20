# Contributing

This repo **is** the aiDocs standard: everything under `docs/` and `.claude/` is content shipped to consuming projects (see [AGENTS.md](AGENTS.md) for the content-vs-instructions separation).

## Workflow

1. Open an issue describing the gap (templates in `.github/ISSUE_TEMPLATE/`, conventions in [docs/issue-tracker.template.md](docs/issue-tracker.template.md))
2. Make the change on a branch, open a PR — the PR template carries the checklist

## Rules for doc changes

- Apply the [Information Minimalism test](docs/INFORMATION_MINIMALISM.md) before adding content
- Follow the file naming rule in [DOCUMENTATION_GUIDELINES.md](docs/DOCUMENTATION_GUIDELINES.md)
- Update [docs/INDEX.md](docs/INDEX.md) when adding or removing files
- Lint locally: `npx markdownlint-cli2 "**/*.md"` (config: `.markdownlint.yaml`) and `python docs/tools/check-docs.py` — CI runs both on every doc-touching PR
