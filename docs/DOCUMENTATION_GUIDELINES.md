# Documentation Guidelines

## Core Principle

> Document what a seasoned developer or LLM would need to **reconstruct** the project on the same platform, or **translate** it to another platform — skip what they already know.

This serves two audiences equally:
- **Reconstruction:** A new developer joining the project
- **Translation:** An LLM porting functionality to another platform

Both need the same information: intent, constraints, and rationale — not mechanics.

## Information Minimalism

### The Test

Before adding documentation, ask in order:

1. **Would a skilled developer need this to reconstruct or port the feature?**
    - NO → Don't document
    - YES → Continue

2. **Is it obvious from code, naming, or structure?**
    - YES → Don't document
    - NO → Continue

3. **Does it duplicate existing content?**
    - YES → Reference instead
    - NO → Document it ✅

### What to Document

| Type | When | Example |
|------|------|---------|
| **Behavioral intent** | Expected outcome matters | `// Session survives rotation — user expects no data loss` |
| **Constraint rationale** | A limit/threshold exists | `// 500ms debounce — faster causes UI jank on low-end devices` |
| **Domain knowledge** | Values a dev wouldn't know | `// RMSSD typically 20-200ms for healthy adults` |
| **Non-obvious "why"** | Decision isn't self-evident | `// Room over DataStore: need relational queries for history` |
| **Quirks/workarounds** | Platform or device-specific | `// PLATFORM: Coospo BLE requires 500ms post-connect delay` |
| **Complex behavior** | Signature doesn't tell the story | `@param windowMillis Sliding window; resets on new session` |

### What to Skip

- What the code does (read the code)
- Obvious parameters (`@param id The ID`)
- Standard patterns the platform expects (ViewModel lifecycle, Composable structure)
- Commented-out code (delete it)

### Platform-Specific Marker

Use one marker for platform-specific quirks that need evaluation when porting:

```kotlin
// PLATFORM: Coospo BLE requires 500ms post-connect delay before notifications work
```

Everything *without* this marker is implicitly cross-platform intent. No separate INTENT marker needed — if it's not platform-specific, it's a requirement.

## Documentation Levels

| Location | Contains | Examples |
|----------|----------|----------|
| **Code** (docstrings, comments) | Intent, rationale, edge cases, API behavior | Function docs, inline "why" comments |
| **/docs folder** | Developer operations, platform guides, contribution workflow | Build, test, run, release, agent behavior |
| **Wiki** | How software functions (user perspective), architecture, domain concepts | Features, behavior, system design |

### Code Documentation

Apply Information Minimalism. Document only what isn't obvious from reading the code.

**Technical Debt:**
```kotlin
// TODO: Brief description of what's needed
// TODO(#123): With issue reference if tracked
```

### /docs Folder

Documents platform-specific setup, development, and testing.

**File Naming:**
- **UPPERCASE** — Template/meta/reference files (describe structure)
- **lowercase** — Content files (actual project data)

**Before writing:** Check `[platform]-index.md` to avoid duplication
**After writing:** Update the index

### Wiki

Documents how software **functions** (user perspective), not how code **works** (implementation).

**File Naming:** Section prefix + descriptive name
```
architecture-overview.md
features-heart_rate_zones.md
devices-ble-polar.md
```

**Before writing:** Check wiki index to avoid duplication
**After writing:** Update the sidebar

#### Structure: Behavior First, Then Platform

Wiki pages separate **what the feature does** (platform-agnostic) from **how it's implemented** (platform-specific). The structure itself conveys intent — no inline markers needed.

```markdown
# Feature Name

## What It Does
Platform-agnostic description of behavior. Any implementation on any
platform must achieve this. This section IS the cross-platform requirement.

## Why It Matters
Rationale, constraints, domain knowledge. Explains decisions that aren't
obvious from the behavior description.

## Android Implementation
How it's built on Android: classes, APIs, patterns, quirks.
Use `// PLATFORM:` comments for code-level quirks.

## iOS Implementation
*Placeholder until iOS development begins.*
```

**Example:**

```markdown
# Device Connection Management

## What It Does
Users pair heart rate devices once. The app remembers paired devices and
reconnects automatically on launch. Manual disconnect prevents auto-reconnect
until user explicitly reconnects.

Connection states: Disconnected → Connecting → Connected → Disconnected

## Why It Matters
- Auto-reconnect saves time for daily workouts
- Respecting manual disconnect prevents unwanted battery drain
- Clear states let UI show accurate feedback

## Android Implementation

### Key Components
| Component | Responsibility |
|-----------|---------------|
| `DeviceManager` | Coordinates BLE and WearOS sources |
| `BleDeviceSource` | Android BLE scanning and GATT connections |

### Quirks
- BLE scanning requires location permission (Android platform requirement)
- Some devices (Coospo) need post-connect delay before notifications work

## iOS Implementation
*To be documented when iOS development begins.*
```

**Key principle:** If someone reads only "What It Does" and "Why It Matters", they have everything needed to implement the feature on any platform. The platform sections are reference for existing implementations.

## Examples

### Good: Behavior + Rationale
```kotlin
/**
 * Manages heart rate session state.
 *
 * Emits Loading → Success/Error states. UI binds directly to these.
 * Sessions survive configuration changes (rotation, theme switch).
 *
 * Uses 500ms debounce on sensor readings — faster updates cause visible
 * UI jank on mid-range devices (tested on Pixel 4a, Galaxy A52).
 */
class HeartRateViewModel(...) : ViewModel()
```

### Good: Platform Workaround
```kotlin
// PLATFORM: Coospo H808S requires 500ms delay after BLE connect
// before enabling notifications. Without this, first 2-3 readings
// are zeros. Other tested devices (Polar H10, Garmin HRM) work immediately.
delay(500)
```

### Good: Domain Knowledge
```kotlin
// RMSSD (Root Mean Square of Successive Differences) measures
// heart rate variability. Typical range: 20-200ms for healthy adults.
// Values outside this range may indicate sensor noise or artifacts.
// Reference: Shaffer & Ginsberg, 2017
```

### Bad: Obvious
```kotlin
// Get the heart rate (DON'T — obvious from name)
fun getHeartRate(): Int

// Loop through the list (DON'T — read the code)
for (item in items) { ... }

// The user ID (DON'T — obvious parameter)
@param userId The user ID
```

### Bad: Mechanics Without Why
```kotlin
// Delays for 500 milliseconds (DON'T — says what, not why)
delay(500)
```

## Periodic Validation

Invoke the [validation](subagents/validation.md) agent before major releases or quarterly.
Applies to both docs/ and wiki/.

---

**Last Updated:** 2026-02-06
