# test-runner

Runs tests by category after code changes.

## Commands

<!-- Replace with your project's test commands -->
| Category | Command |
|----------|---------|
| (all) | `./gradlew test` |
| unit | `./gradlew test -PtestCategory=unit` |
| integration | `./gradlew test -PtestCategory=integration` |

## Steps

1. Determine category from arguments (if provided)
2. Run the matching command
3. Report: tests run, passed, failed, time
4. On failure: list failed test names and suggest re-run command
