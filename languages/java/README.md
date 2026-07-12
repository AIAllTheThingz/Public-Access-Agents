---
id: JAVA-PKG-001
status: baseline
title: Java Package
---

# Java Language Package

## Status

Baseline package suitable for project adoption and review.

## Contents

- `AGENTS.md`: mandatory agent behavior
- `standards/`: coding, architecture, documentation, testing, security, dependency, observability, evidence, and ecosystem-specific rules
- `templates/`: adoption templates
- `examples/`: composition guidance
- `MANIFEST.md`: package inventory and validation checklist

## Adoption

1. Copy this directory into the target repository or reference it through the organization's composition process.
2. Declare the exact supported runtime, toolchain, platforms, and compatibility constraints.
3. Remove standards that are provably inapplicable only through a documented tailoring decision.
4. Add stricter project-specific rules without weakening inherited controls.
5. Run the repository validator and link checker.
6. Review the resulting `AGENTS.md` with an accountable maintainer.

## Runtime policy

For new work, prefer a currently supported Java LTS release and declare the exact toolchain in the build. Existing repositories must preserve their declared compatibility unless migration is in scope.

## Validation baseline

- `./mvnw verify` or `./gradlew check`
- run configured static analysis
- test the packaged artifact
