---
id: PROFILE-DATA-PIPELINE
title: Data Pipeline Project Profile
version: 0.1.0
status: baseline
applies_to:
  - data-pipeline
depends_on:
  - GOV-CONTRACT
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Data Pipeline Project Profile

## Required discipline overlays

- `disciplines/architecture/AGENTS.md`
- `disciplines/testing/AGENTS.md`
- `disciplines/integration/AGENTS.md`
- `disciplines/database/AGENTS.md`
- `disciplines/data-engineering/AGENTS.md`
- `disciplines/privacy/AGENTS.md`
- `disciplines/observability/AGENTS.md`
- `disciplines/sre/AGENTS.md`

## Required project decisions

- Data contracts and lineage
- Replay and backfill behavior
- Quality gates
- Retention and sensitive-data handling

## Completion gate

The project must satisfy applicable governance, language, platform, framework, and discipline standards. Document exclusions and exceptions.
