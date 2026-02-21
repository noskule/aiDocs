---
name: generate-index
description: Regenerates the code-index after public API changes (add/remove/rename classes or functions).
argument-hint: ""
disable-model-invocation: true
---

Regenerate the AST-based code index. Run this after modifying public APIs.

## Command

```bash
cd docs/tools/code-index && .venv/Scripts/python generate.py --config ../../../aidocs.yaml
```

## After Running

1. Review the changes in `docs/code-index/`
2. Commit the updated index files with your code change

## Reference

See `docs/tools/JOBS.md` for full details.
