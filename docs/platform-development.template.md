# [Platform] Development Guide

Platform-specific development setup, commands, and patterns.


## Tech Stack

- **Platform:** [e.g., Android (Kotlin), iOS (Swift), Web (TypeScript)]
- **UI:** [e.g., Jetpack Compose, SwiftUI, React]
- **Architecture:** [e.g., MVVM, MVC, Clean Architecture]
- **Build System:** [e.g., Gradle, Xcode, npm]
- **Testing:** [e.g., JUnit, XCTest, Jest]


## Architecture

### Layer Separation

```
UI -> Presentation -> Domain -> Data -> Core
```

**Dependencies flow inward** - outer layers depend on inner layers.


## Build Commands

```bash
# Build
[build command]

# Install
[install command]
```

**Running tests?** See `[platform]-testing.md`


## Code Patterns

### Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Screen | `[Feature]Screen` | `SettingsScreen` |
| ViewModel | `[Feature]ViewModel` | `SettingsViewModel` |
| Repository | `[Domain]Repository` | `UserRepository` |


## File Organization

```
src/
├── ui/           # UI components
├── presentation/ # ViewModels
├── domain/       # Business logic
├── data/         # Repositories
└── core/         # Utilities
```


## Common Tasks

### Adding a New Screen

1. Create screen component
2. Create ViewModel
3. Add navigation route
4. Add tests
5. Update wiki if feature-related


## Troubleshooting

### Build Issues

1. Check error message
2. Clean build
3. Invalidate caches
4. Check dependencies


**Last Updated:** [date]
