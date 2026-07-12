---
id: PROFILE-SECTOOL
title: Security Tool Project Profile
version: 0.1.0
status: baseline
applies_to:
  - security-tool
depends_on:
  - GOV-CONTRACT
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Security Tool Project Profile

## Required discipline overlays

- `disciplines/application-security/AGENTS.md`
- `disciplines/architecture/AGENTS.md`
- `disciplines/testing/AGENTS.md`
- `disciplines/privacy/AGENTS.md`
- `disciplines/observability/AGENTS.md`
- `disciplines/documentation/AGENTS.md`
- `disciplines/supply-chain/AGENTS.md`
- `disciplines/release-engineering/AGENTS.md`

## Required project decisions

- Safe handling of findings and evidence
- False-positive and false-negative limitations
- Privilege and data sensitivity
- Non-destructive defaults

## Completion gate

The project must satisfy applicable governance, language, platform, framework, and discipline standards. Document exclusions and exceptions.
