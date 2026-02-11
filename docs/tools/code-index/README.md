# code-index

Generates a compact two-level markdown index from source ASTs for LLM codebase orientation.

An LLM reads `index.md` to orient itself, then drills into only the relevant package file — avoiding the need to read entire source files just to discover what exists.

## How It Works

1. **Parse** source files using tree-sitter AST extraction
2. **Group** declarations by package with configurable depth-based merging
3. **Generate** three levels of markdown: root index, module index, per-package detail

## Output Structure

```
docs/code-index/
├── index.md              # Root: lists all modules with counts
├── <module>/
│   ├── index.md          # Module: one-line summary per declaration
│   └── <package>.md      # Package: full signatures + members
```

## Setup

```bash
cd docs/tools/code-index
python -m venv .venv
.venv/Scripts/activate   # Windows
# source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

Requires Python 3.10+.

## Usage

### With config file (recommended)

```bash
python docs/tools/code-index/generate.py --config aidocs.yaml
```

Create an `aidocs.yaml` at your project root. See `aidocs.yaml.template` for the format.

### With CLI args (single module)

```bash
python docs/tools/code-index/generate.py \
  --src app/src/main/java \
  --lang kotlin \
  --module app \
  --prefix com.example.myapp \
  --out docs/code-index
```

## Configuration

`aidocs.yaml` fields:

| Field | Description | Default |
|-------|-------------|---------|
| `language` | Source language | `kotlin` |
| `modules[].name` | Module identifier | required |
| `modules[].source_dirs` | Source directories (relative to config) | required |
| `modules[].prefix` | Package prefix to strip | required |
| `output_dir` | Output directory | `docs/code-index` |
| `merge_threshold` | Package depth for merging | `2` |

### Merge threshold

Controls how deep packages are grouped. With `merge_threshold: 2`:
- `data.db.converters` and `data.db.dao` merge into `data/db.md`
- `core.hrv` stays as `core/hrv.md` (depth 2, not merged)

## Architecture

```
generate.py          # CLI entry point + orchestration
languages/
  base.py            # Declaration dataclass + LanguageAdapter ABC
  kotlin.py          # Kotlin tree-sitter extraction
grouping.py          # Package grouping + merge logic
generator.py         # Markdown rendering
```

### Adding a new language

1. Create `languages/<lang>.py` implementing `LanguageAdapter`
2. Register it in `generate.py:get_adapter()`
3. The adapter must return `Declaration` objects from `parse_file()`

## What Gets Indexed

- Top-level classes, interfaces, objects, functions, properties
- Class body: public members (functions, properties, nested types)
- Architecture-relevant annotations (e.g., `@Composable`, `@Inject`, `@Entity`)
- KDoc first-sentence summaries

## What Gets Skipped

- Private/internal members
- Override functions
- Function bodies and initializers
- `@Preview` composables
- Default parameter values
