---
id: PROFILE-WORKER
title: Worker Service Project Profile
version: 0.1.0
status: baseline
applies_to:
  - worker-service
depends_on:
  - GOV-CONTRACT
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Worker Service Project Profile

## Required discipline overlays

- `disciplines/architecture/AGENTS.md`
- `disciplines/testing/AGENTS.md`
- `disciplines/integration/AGENTS.md`
- `disciplines/observability/AGENTS.md`
- `disciplines/sre/AGENTS.md`
- `disciplines/ci-cd/AGENTS.md`
- `disciplines/supply-chain/AGENTS.md`
- `disciplines/release-engineering/AGENTS.md`

## Required project decisions

- Idempotency and replay behavior
- Concurrency and cancellation
- Dependency failure handling
- Health and operational ownership

## Completion gate

The project must satisfy applicable governance, language, platform, framework, and discipline standards. Document exclusions and exceptions.
