---
id: DISC-ARCH
title: Architecture and System Design Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - architecture
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Architecture and System Design Agent Standard

## Purpose

Keeps structural decisions explicit, reviewable, reversible, and aligned with quality attributes.

## Mandatory rules

### ARCH-BOUNDARY-001

**Requirement:** Define components, responsibilities, trust boundaries, dependencies, and ownership.

**Evidence:** Architecture diagram or ADR.

### ARCH-QUALITY-002

**Requirement:** State relevant quality attributes such as availability, security, maintainability, latency, scalability, and recoverability.

**Evidence:** Documented trade-offs and acceptance criteria.

### ARCH-COUPLING-003

**Requirement:** Prefer explicit interfaces and avoid hidden shared state or circular dependencies.

**Evidence:** Dependency review.

### ARCH-FAILURE-004

**Requirement:** Design for dependency failure, partial failure, retries, idempotency, and recovery where applicable.

**Evidence:** Failure-mode analysis.

### ARCH-ADR-005

**Requirement:** Record material, hard-to-reverse decisions as architecture decision records.

**Evidence:** Accepted ADR.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.
