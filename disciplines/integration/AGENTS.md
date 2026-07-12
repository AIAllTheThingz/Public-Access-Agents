---
id: DISC-INT
title: Integration Engineering Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - integration
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Integration Engineering Agent Standard

## Purpose

Controls assumptions and failure modes at system boundaries.

## Mandatory rules

### INT-CONTRACT-001

**Requirement:** Define ownership, schema, transport, authentication, timeouts, retries, and compatibility.

**Evidence:** Integration contract.

### INT-RESILIENCE-002

**Requirement:** Handle partial failure, duplicate delivery, reordering, and dependency outages.

**Evidence:** Failure-injection tests.

### INT-DATA-003

**Requirement:** Validate and minimize transferred data; classify sensitive fields.

**Evidence:** Data-flow review.

### INT-TEST-004

**Requirement:** Use contract or integration tests against representative behavior.

**Evidence:** Integration test evidence.

### INT-CHANGE-005

**Requirement:** Coordinate breaking changes and migration windows.

**Evidence:** Version and rollout plan.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.
