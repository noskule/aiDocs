---
name: run-analysis
description: Runs structural health analysis after refactoring or completing a sprint.
argument-hint: ""
disable-model-invocation: true
---

Run the structural health analyzer against the codebase.

## Command

```bash
cd docs/tools/code-index && .venv/Scripts/python analyze.py --config ../../../aidocs.yaml
```

## After Running

1. Review the report at `docs/code-index/analysis.md`
2. Findings are informational — not all require action
3. Use `/review-analysis` to classify and prioritize findings

## Reference

See `docs/tools/JOBS.md` for full details.
