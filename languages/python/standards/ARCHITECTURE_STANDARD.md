---
id: PY-ARCH-001
status: baseline
title: Python Architecture Standard
---

# Architecture Standard

## Requirements

- Keep boundaries explicit and dependencies directed toward stable abstractions.
- Separate domain logic from transport, persistence, environment, and tooling concerns.
- Prefer small cohesive units over hidden global state.
- Preserve public contracts unless change is explicitly required.
- Document material tradeoffs and decisions.

## Evidence

Completion evidence must identify the files and checks that demonstrate these requirements. Exceptions must follow the repository exception process and must not be implied by omission.
