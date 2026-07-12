---
id: PROFILE-SERVERLESS
title: Serverless Function Project Profile
version: 0.1.0
status: baseline
applies_to:
  - serverless-function
depends_on:
  - GOV-CONTRACT
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Serverless Function Project Profile

## Required discipline overlays

- `disciplines/application-security/AGENTS.md`
- `disciplines/testing/AGENTS.md`
- `disciplines/integration/AGENTS.md`
- `disciplines/observability/AGENTS.md`
- `disciplines/ci-cd/AGENTS.md`
- `disciplines/supply-chain/AGENTS.md`

## Required project decisions

- Event validation
- Idempotency
- Timeout and retry behavior
- Least-privilege execution identity

## Completion gate

The project must satisfy applicable governance, language, platform, framework, and discipline standards. Document exclusions and exceptions.
