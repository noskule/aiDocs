# Documentation Guidelines

## Core Principle

> Document what a seasoned developer or LLM would need to **reconstruct** the project on the same platform, or **translate** it to another platform — skip what they already know.

This serves two audiences equally:
- **Reconstruction:** A new developer joining the project
- **Translation:** An LLM porting functionality to another platform (e.g., Platform A → Platform B)

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

### Portability Markers

When documenting, flag platform-specific items:
```kotlin
// PLATFORM: [description] — may not apply on other platforms
// PLATFORM: Platform A BLE stack requires explicit disconnect before reconnect

// INTENT: [description] — must work identically on any platform  
// INTENT: Heart rate zones must update within 1 second of sensor data
```

This helps during porting: INTENT items are requirements, PLATFORM items need evaluation.

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

#### Architecture vs Implementation Separation

Wiki documentation should clearly separate **architecture** (platform-agnostic design) from **implementation** (platform-specific code). This enables:
- Clear understanding of what's required vs. how it's done
- Easier porting to new platforms
- Better AI assistant comprehension

**Structure Pattern:**

```markdown
## Overview
Platform-agnostic explanation of what this feature does and why.

## Architecture
Design decisions, state machines, algorithms, data flow.
Use INTENT markers for requirements that must work identically everywhere.

### [Specific Concept]
**INTENT:** [What must happen, regardless of platform]
[Explanation of the concept/algorithm/pattern]

## Platform A Implementation
**PLATFORM:** [How it's implemented on Platform A]
- Specific classes, APIs, patterns used
- Platform-specific quirks and workarounds

## Platform B Implementation
*To be documented when Platform B development begins.*
```

**Example Page Structure:**

```markdown
# Device Connection Management

## Overview
Users connect heart rate devices and expect automatic reconnection.

## Architecture

### Connection States
**INTENT:** Clear state machine for connection lifecycle.
[Diagram showing: Disconnected → Connecting → Connected]

### Auto-Reconnect Rules
**INTENT:** Respect user's connection choices across restarts.
1. On app start: connect to devices marked "enabled"
2. On user disconnect: mark as "disabled", no auto-reconnect

## Platform A Implementation

### Key Components
| Component | Responsibility |
|-----------|---------------|
| `DeviceManager` | Facade coordinating sources |
| `BleDeviceSource` | BLE connection |

### PLATFORM: BLE Specifics
- Platform-specific BLE scanning API
- Connection priority settings for power management
```

**Key Rules:**
1. Architecture sections should be understandable without knowing any specific platform
2. Implementation sections reference actual code, classes, and APIs
3. Use INTENT for cross-platform requirements
4. Use PLATFORM for platform-specific details

## Examples

### Good: Intent + Rationale
```kotlin
/**
 * Manages heart rate session state.
 * 
 * INTENT: Emits Loading → Success/Error states. UI binds directly to these.
 * Sessions must survive configuration changes (rotation, theme switch).
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
// are zeros. Other tested devices (Polar H10, Garmin HRM) work
// immediately. May not apply on other platforms.
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

Run [VALIDATION.md](VALIDATION.md) checklist before major releases or quarterly.
Applies to both docs/ and wiki/.

---

**Last Updated:** 2026-01-14