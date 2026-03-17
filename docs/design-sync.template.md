# Design Sync — Bidirectional Design ↔ Code Sync

Standing instruction set for synchronizing Pencil design files (`.pen`) with UI code.

## File Map

<!-- Populate after discovery. One row per screen + one for tokens. -->

| Frame | Composable / View | File |
|---|---|---|
| `tokens.pen` (all variables) | Theme tokens (colors, typography, shapes) | `<!-- path to theme files -->` |
| `<!-- ScreenName -->` | `<!-- ScreenName() -->` | `<!-- path to screen file -->` |

All paths relative to `<!-- project source root -->`.

## Token Translation Table

### Colors — Light Theme

<!-- Extract from your theme file. Map every .pen variable to its code equivalent. -->

| `.pen` Variable | Code Token | Light Value |
|---|---|---|
| `$color.primary` | `<!-- platform theme token -->` | `<!-- hex -->` |
| `$color.onPrimary` | `<!-- platform theme token -->` | `<!-- hex -->` |

### Colors — Dark Theme

| `.pen` Variable | Code Token | Dark Value |
|---|---|---|
| `$color.primary` | `<!-- platform theme token -->` | `<!-- hex -->` |

### Shapes

| `.pen` Variable | Code Token | Value |
|---|---|---|
| `$shape.extraSmall` | `<!-- platform shape token -->` | `4dp` |
| `$shape.small` | `<!-- platform shape token -->` | `8dp` |
| `$shape.medium` | `<!-- platform shape token -->` | `12dp` |
| `$shape.large` | `<!-- platform shape token -->` | `16dp` |
| `$shape.extraLarge` | `<!-- platform shape token -->` | `28dp` |

### Typography

| `.pen` Variable | Code Token | Size / Weight |
|---|---|---|
| `$typography.displayLarge` | `<!-- platform type token -->` | `<!-- size / weight -->` |

## Component Mapping

<!-- One row per component parameter. Only include components actually used in the codebase. -->

| `.pen` Frame | Composable / View | Parameter Mapping |
|---|---|---|
| `Button.label` | `<!-- platform button -->` | Text content |
| `Card.children` | `<!-- platform card -->` | Card content slot |

## Sync Rules

### Design → Code

**Trigger:** `sync design→code <ScreenName>`

**Steps:**
1. Read the named frame from `design/screens.pen`
2. Read the corresponding source file
3. Update ONLY: layout structure, spacing, colors, typography, corner radius, component choice
4. NEVER touch: ViewModel/Controller calls, state management, navigation, event handlers, business logic
5. Preserve all existing function signatures and parameters

### Code → Design

**Trigger:** `sync code→design <ScreenName>`

**Steps:**
1. Read the source file
2. Read the current frame from `design/screens.pen`
3. Update the frame to reflect current UI hierarchy
4. Map each UI element to its component ref in `design/components.pen`
5. Update variable bindings to match hardcoded values if any

### Token Sync

**Trigger:** `sync tokens`

**Steps:**
1. Read theme source files
2. Update all variables in `design/tokens.pen` to match exactly
3. Report any discrepancies found

## Conflict Policy

| Category | Winner |
|---|---|
| Colors, spacing, typography | Design file wins |
| Component structure, logic | Code wins |
| Ambiguous | Ask before overwriting |

## Scope Boundary — Never Touch

- State management (ViewModel, StateFlow, LiveData, controllers)
- Navigation calls
- Event handlers (onClick, onValueChange, callbacks)
- Side effects (LaunchedEffect, SideEffect, lifecycle hooks)

## Minimum Sync Unit

Sync operates at frame/screen level, not whole-file.
A sync of one screen does not affect another, even if they share a source file.

## File Locations

```
design/
├── tokens.pen       # Color/typography/shape variables (JSON)
├── components.pen   # Component library (JSON)
└── screens.pen      # Screen frames matching current UI (JSON)

docs/
└── design-sync.md   # This file — sync rules and mappings
```

## Notes

- `.pen` files are JSON — treat as code, not binary assets
- Always use `$variable` references in `.pen`, never hardcoded hex values
- The `design/` folder commits alongside code changes in the same PR
- After writing a `.pen` file, reload it in Pencil to see changes
