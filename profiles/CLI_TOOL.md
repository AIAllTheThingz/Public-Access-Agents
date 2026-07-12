---
id: PROFILE-CLI
title: Command-Line Tool Project Profile
version: 0.1.0
status: baseline
applies_to:
  - command-line-tool
depends_on:
  - GOV-CONTRACT
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Command-Line Tool Project Profile

## Required discipline overlays

- `disciplines/application-security/AGENTS.md`
- `disciplines/testing/AGENTS.md`
- `disciplines/documentation/AGENTS.md`
- `disciplines/supply-chain/AGENTS.md`
- `disciplines/release-engineering/AGENTS.md`

## Required project decisions

- Safe defaults
- Explicit confirmation for destructive actions
- Machine-readable and human-readable output
- Exit-code contract

## Completion gate

The project must satisfy applicable governance, language, platform, framework, and discipline standards. Document exclusions and exceptions.
