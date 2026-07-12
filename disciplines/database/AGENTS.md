---
id: DISC-DB
title: Database Engineering Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - database
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Database Engineering Agent Standard

## Purpose

Protects data integrity, security, performance, and recoverability.

## Mandatory rules

### DB-MIGRATION-001

**Requirement:** Use versioned, reviewable, forward and rollback-aware migrations.

**Evidence:** Migration test evidence.

### DB-QUERY-002

**Requirement:** Use parameterized queries and review plans for material queries.

**Evidence:** Query and plan review.

### DB-INTEGRITY-003

**Requirement:** Enforce constraints at the appropriate layer and test concurrency behavior.

**Evidence:** Constraint and concurrency tests.

### DB-ACCESS-004

**Requirement:** Apply least privilege and separate administrative from application access.

**Evidence:** Privilege review.

### DB-RECOVERY-005

**Requirement:** Define backup, restore, retention, and recovery expectations.

**Evidence:** Restore-test evidence.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.
