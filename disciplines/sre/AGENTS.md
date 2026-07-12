---
id: DISC-SRE
title: Site Reliability Engineering Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - sre
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Site Reliability Engineering Agent Standard

## Purpose

Connects reliability objectives to design, delivery, and operations.

## Mandatory rules

### SRE-SLO-001

**Requirement:** Define service objectives or explicit operational expectations.

**Evidence:** SLO or operating target.

### SRE-BUDGET-002

**Requirement:** Use error budgets or equivalent risk signals for material services.

**Evidence:** Decision record.

### SRE-RUNBOOK-003

**Requirement:** Provide runbooks for likely incidents and recovery actions.

**Evidence:** Reviewed runbook.

### SRE-CAPACITY-004

**Requirement:** Assess resource limits, scaling, saturation, and dependency quotas.

**Evidence:** Capacity evidence.

### SRE-INCIDENT-005

**Requirement:** Feed incident learning into tests, automation, and design.

**Evidence:** Post-incident actions.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.
