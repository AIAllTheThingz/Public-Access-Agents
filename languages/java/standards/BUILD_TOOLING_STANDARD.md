---
id: JAVA-S2-001
status: baseline
title: Java Build Tooling Standard
---

# Build Tooling Standard

## Requirements

- Use one primary build system per module: Maven or Gradle.
- Pin wrapper versions and verify wrapper integrity.
- Separate compile, test, integration-test, packaging, and publishing concerns.
- Use reproducible dependency resolution and dependency verification where supported.
- Test the packaged artifact, not only IDE execution.

## Review evidence

Document configuration, commands, tests, compatibility assumptions, and remaining risk.
