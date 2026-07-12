---
id: DISC-OBS
title: Observability Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - observability
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Observability Agent Standard

## Purpose

Requires telemetry that supports diagnosis without becoming a data leak.

## Mandatory rules

### OBS-SIGNALS-001

**Requirement:** Define logs, metrics, traces, and events appropriate to the system.

**Evidence:** Telemetry plan.

### OBS-CONTEXT-002

**Requirement:** Include correlation and operation context without sensitive data.

**Evidence:** Sample telemetry.

### OBS-HEALTH-003

**Requirement:** Separate liveness, readiness, dependency, and business-health signals.

**Evidence:** Health-check tests.

### OBS-ALERTS-004

**Requirement:** Alert on actionable symptoms with ownership and runbook links.

**Evidence:** Alert review.

### OBS-COST-005

**Requirement:** Control cardinality, retention, sampling, and telemetry volume.

**Evidence:** Cost and cardinality review.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.

## References

- https://opentelemetry.io/docs/
