---
id: TEMPLATE-EX-RISK-001
title: Change Risk Assessment Example
version: 0.2.0
status: baseline
---

# Change Risk Assessment Example

- Change ID: `CHG-EXAMPLE-0042`
- Summary: Replace a read-only reporting dependency.
- Classification: `moderate`
- Risk owner: application owner
- Rollback required: `yes`

## Rationale

The change affects internal reports and one scheduled job but does not modify source systems.

## Risk factors

| Factor | Assessment |
|---|---|
| Data sensitivity | Internal asset metadata |
| Privilege | Read-only service identity |
| External exposure | None |
| Blast radius | One reporting workflow |
| Reversibility | Configuration rollback |
| Availability impact | Reports may be delayed |
| Safety impact | None identified |
| Dependency and supply-chain risk | New supported client library |

## Required controls

Peer review, integration test, staged deployment, rollback configuration, and report comparison.

## Residual risk

A provider-specific edge case may alter optional fields.

## Reassessment triggers

Write capability, public exposure, sensitive data, or multi-system rollout.
