---
id: PROFILE-AI-AGENT
title: AI Agent Application Project Profile
version: 0.1.0
status: baseline
applies_to:
  - ai-agent-application
depends_on:
  - GOV-CONTRACT
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# AI Agent Application Project Profile

## Required discipline overlays

- `disciplines/application-security/AGENTS.md`
- `disciplines/architecture/AGENTS.md`
- `disciplines/testing/AGENTS.md`
- `disciplines/api-engineering/AGENTS.md`
- `disciplines/privacy/AGENTS.md`
- `disciplines/observability/AGENTS.md`
- `disciplines/supply-chain/AGENTS.md`

## Required project decisions

- Tool authorization and allowlists
- Prompt and retrieved-content trust boundaries
- Human approval for consequential actions
- Traceable decisions, outputs, and tool calls
- Evaluation for unsafe or incorrect behavior

## Completion gate

The project must satisfy applicable governance, language, platform, framework, and discipline standards. Document exclusions and exceptions.
