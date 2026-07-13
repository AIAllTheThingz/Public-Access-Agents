---
id: TEMPLATE-EX-PRODUCTION-READINESS-001
title: Production Readiness Review Example
version: 0.2.0
status: baseline
---

# Production Readiness Review Example

- Review ID: `PRR-EXAMPLE-0042`
- System or change: Fictitious report worker
- Target environment: production
- Owners: application owner, platform owner, operations owner
- Risk assessment: `CHG-EXAMPLE-0042`
- Architecture reference: `ADR-0042`

## Security and privacy readiness

Workload identity, least privilege, threat-model review, and redaction tests are complete.

## Reliability, capacity, and quota readiness

Load test and queue-capacity review passed for expected volume.

## Observability readiness

Owned logs, queue-depth metrics, health alerts, and dashboards are configured.

## Recovery readiness

Previous artifact rollback and message replay were rehearsed in staging.

## Operations and support

Runbook, on-call route, escalation, and maintenance ownership are documented.

## Release and rollout

Canary worker, fifteen-minute observation, then phased worker rollout.

## Open risks and exceptions

One moderate exception for a non-production-only dependency. It does not apply to production.

## Decision

`ready-with-conditions`

## Authorized approvers

Operations owner and production change authority.

## Boundary

This example is not a real production approval.
