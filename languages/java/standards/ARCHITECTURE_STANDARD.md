---
id: JAVA-ARCH-001
status: baseline
title: Java Architecture Standard
---

# Architecture Standard

## Requirements

- Keep boundaries explicit and dependencies directed toward stable abstractions.
- Separate domain logic from transport, persistence, environment, and tooling concerns.
- Prefer small cohesive units over hidden global state.
- Preserve public contracts unless change is explicitly required.
- Document material tradeoffs and decisions.

## Evidence

Identify the files and checks demonstrating these requirements. Exceptions must follow the repository exception process.
