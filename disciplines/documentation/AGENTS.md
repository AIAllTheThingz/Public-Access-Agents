---
id: DISC-DOC
title: Documentation Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - documentation
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Documentation Agent Standard

## Purpose

Treats documentation as part of the deliverable and keeps it usable by non-authors.

## Mandatory rules

### DOC-AUDIENCE-001

**Requirement:** Identify intended readers and required prerequisites.

**Evidence:** Document header or introduction.

### DOC-OPERATE-002

**Requirement:** Document configuration, execution, failure handling, recovery, and support ownership.

**Evidence:** Operational documentation.

### DOC-DECISIONS-003

**Requirement:** Record non-obvious rationale and material trade-offs.

**Evidence:** Comments or ADRs.

### DOC-EXAMPLES-004

**Requirement:** Use safe, runnable, fictitious examples.

**Evidence:** Example validation.

### DOC-SYNC-005

**Requirement:** Update documentation in the same change as behavior.

**Evidence:** Diff review.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.
