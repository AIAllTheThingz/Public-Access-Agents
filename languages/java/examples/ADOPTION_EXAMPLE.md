---
id: JAVA-EX-001
status: baseline
title: Java Adoption Example
---

# Java Adoption Example

A project should compose standards rather than duplicate them.

```text
project/
├── AGENTS.md
├── standards/
│   └── project-specific.md
├── src/
├── tests/
└── docs/
```

The project `AGENTS.md` should reference this package, declare the exact JDK and build tool, add applicable overlays, define project commands, and preserve inherited security and evidence requirements.

Example completion evidence:

```text
Changed: src/, tests/, docs/
Validation: ./mvnw verify or ./gradlew check
Security impact: reviewed trust boundaries and secret handling
Compatibility: preserved declared runtime baseline
Limitations: list checks not run and why
```
