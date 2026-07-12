---
id: BASH-ARCH-001
status: baseline
title: Bash Architecture Standard
---

# Architecture Standard

- Keep orchestration separate from reusable functions and environment configuration.
- Prefer configuration files or explicit parameters over hidden environment assumptions.
- Keep external-command adapters isolated so they can be validated and tested.
- Split overly large scripts into cohesive libraries only when sourcing and deployment remain clear.
- Document execution order, state transitions, and recovery behavior.
