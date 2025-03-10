0.4.2 - 2023-05-10
==================
Update - Allow the gradlew to not be present in current directory, but use the -p argument to specify the path

0.3.0 - 2021-01-08
==================
- Update - `gradle-spotless` now executes `spotlessCheck` and `spotlessApply` rather than `spotlessJavaCheck` and `spotlessJavaApply`. Now supports projects using Java Kotlin, Scala, etc.

0.2.1 - 2020-02-10
==================
- Bug - Adjusted use of shell in python subprocess execution by using tuple expansion on command execution

0.2.0 - 2020-02-05
==================
- Safety checks on gradle and gradlew installations before execution
- Refactoring common code snippets to utilities
- Default disable output from gradle commands
- '-o, --output' argument added to enable gradle output
- Colored print statements using ANSI escape sequences
- Human readable escape statements on missing gradle or gradle wrapper

0.1.0 - 2020-01-23
==================
- Initial Release
