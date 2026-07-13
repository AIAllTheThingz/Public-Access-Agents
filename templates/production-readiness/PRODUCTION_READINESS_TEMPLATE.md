---
id: TEMPLATE-PRODUCTION-READINESS-001
title: Production Readiness Review Template
version: 0.2.0
status: baseline
template_type: production-readiness
---

# Production Readiness Review Template

- Review ID: `{{REVIEW_ID}}`
- System or change: {{SYSTEM}}
- Target environment: {{TARGET_ENVIRONMENT}}
- Owners: {{OWNERS}}
- Risk assessment: {{RISK_REFERENCE}}
- Architecture reference: {{ARCHITECTURE_REFERENCE}}

## Security and privacy readiness

{{SECURITY_PRIVACY}}

## Reliability, capacity, and quota readiness

{{RELIABILITY_CAPACITY}}

## Observability readiness

{{OBSERVABILITY}}

## Recovery readiness

{{RECOVERY}}

Include tested rollback, restore, failover, recreation, and escalation evidence as applicable.

## Operations and support

{{OPERATIONS_SUPPORT}}

## Release and rollout

{{RELEASE_ROLLOUT}}

## Open risks and exceptions

{{OPEN_RISKS}}

## Decision

`{{DECISION}}`

Allowed decision vocabulary:

- ready
- ready-with-conditions
- not-ready
- deferred

## Authorized approvers

{{APPROVERS}}

Production readiness is separate from implementation completion and deployment success.
