---
id: GOV-PROD
title: Production Readiness
version: 0.1.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - none
---
# Production Readiness

## Purpose

Defines minimum operational evidence before production use.

## Requirements

### GOV-PROD-001

**Requirement:** Document deployment, configuration, secrets, observability, support ownership, rollback, and recovery.

### GOV-PROD-002

**Requirement:** Validate failure modes, dependency outages, resource limits, and data migration behavior as applicable.

### GOV-PROD-003

**Requirement:** Define service-level objectives or operational expectations where applicable.

### GOV-PROD-004

**Requirement:** Do not equate successful build or unit tests with production readiness.

## Minimum evidence

- Deployment and rollback plan
- Monitoring and alerting plan
- Recovery evidence
- Operational owner

## Exceptions

Use the documented exception process.
