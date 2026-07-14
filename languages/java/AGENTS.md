---
id: JAVA-AGENT-001
status: baseline
title: Java Agent Standard
---

# Java Agent Standard

## Purpose

This file defines mandatory rules for coding agents that create, modify, review, test, secure, or document Java work. The package is project-agnostic and supplements repository governance and applicable discipline, framework, platform, virtualization, operating-system, networking, and project-profile standards.

> Make the smallest safe, maintainable, testable, observable, and well-documented change that satisfies the requirement.

## Scope

- Java applications and libraries
- JVM services
- build files
- tests
- database access
- deployment packaging

## Instruction priority

1. Explicit user requirements
2. The nearest more-specific `AGENTS.md`
3. This package `AGENTS.md`
4. Referenced supporting standards
5. Repository conventions
6. General agent preferences

Report material conflicts rather than resolving them silently.

## Runtime baseline

For new work, prefer a currently supported Java LTS release and declare the exact toolchain in the build. Existing repositories must preserve their declared compatibility unless migration is in scope.

## Required supporting standards

- `standards/JAVA_CODING_STANDARD.md`
- `standards/ARCHITECTURE_STANDARD.md`
- `standards/DOCUMENTATION_STANDARD.md`
- `standards/TESTING_STANDARD.md`
- `standards/SECURITY_STANDARD.md`
- `standards/DEPENDENCY_MANAGEMENT_STANDARD.md`
- `standards/OBSERVABILITY_STANDARD.md`
- `standards/COMPLETION_EVIDENCE.md`
- `standards/JVM_RUNTIME_STANDARD.md`
- `standards/BUILD_TOOLING_STANDARD.md`

## Non-negotiable rules

- Default to safe, narrow, reversible behavior.
- Inspect existing code, tests, configuration, and conventions before changing anything.
- Do not invent environment values, identities, endpoints, credentials, versions, or operational assumptions.
- Validate all external input and trust-boundary data.
- Do not weaken security controls to make a change succeed.
- Preserve public contracts unless change is explicitly authorized.
- Keep secrets out of source, tests, logs, errors, examples, and committed configuration.
- Use least privilege and explicit authorization for state-changing work.
- Stop when prerequisites are missing or target identity is ambiguous.
- Keep generated code readable by maintainers who did not author it.

## Required working method

1. Discover the current design and supported runtime.
2. Classify risk and identify trust boundaries.
3. Define acceptance criteria and required evidence.
4. Implement the smallest coherent change.
5. Add or update tests and documentation.
6. Run formatting, static analysis, tests, and package-specific validation.
7. Review the diff for unrelated changes, secrets, unsafe defaults, and compatibility regressions.
8. Report exact evidence and limitations.

## Completion commands

- `./mvnw verify` or `./gradlew check`
- run configured static analysis
- test the packaged artifact

Use repository-defined commands when they differ. Never claim a command passed unless it was run successfully.
