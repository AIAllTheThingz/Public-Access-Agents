---
id: GOV-RISK
title: Risk Classification
version: 0.1.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - none
---
# Risk Classification

## Purpose

Scales review, testing, and completion evidence to the potential impact of a change.

## Requirements

### GOV-RISK-001

**Requirement:** Classify each change as low, moderate, high, or critical before implementation.

### GOV-RISK-002

**Requirement:** Consider data sensitivity, privilege, blast radius, reversibility, external exposure, availability, and safety.

### GOV-RISK-003

**Requirement:** High and critical changes require threat analysis, rollback planning, independent review, and explicit approval.

### GOV-RISK-004

**Requirement:** Uncertain risk defaults to the higher plausible classification.

## Minimum evidence

- Recorded risk level and rationale
- Required reviewers
- Required validation and rollback evidence

## Exceptions

Use the documented exception process.
