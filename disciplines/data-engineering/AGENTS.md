---
id: DISC-DATA
title: Data Engineering Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - data-engineering
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Data Engineering Agent Standard

## Purpose

Makes data lineage, quality, privacy, reproducibility, and recovery explicit.

## Mandatory rules

### DATA-CONTRACT-001

**Requirement:** Define schemas, ownership, quality expectations, and compatibility.

**Evidence:** Data contract.

### DATA-LINEAGE-002

**Requirement:** Record sources, transformations, destinations, and retention.

**Evidence:** Lineage documentation.

### DATA-QUALITY-003

**Requirement:** Validate completeness, uniqueness, timeliness, ranges, and referential expectations.

**Evidence:** Data-quality results.

### DATA-REPLAY-004

**Requirement:** Design idempotent or replay-safe processing where applicable.

**Evidence:** Replay test.

### DATA-PRIVACY-005

**Requirement:** Minimize sensitive data and enforce retention and access requirements.

**Evidence:** Privacy review.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.
