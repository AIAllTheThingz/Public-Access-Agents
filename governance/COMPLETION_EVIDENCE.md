---
id: GOV-EVIDENCE
title: Completion Evidence
version: 0.1.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - none
---
# Completion Evidence

## Purpose

Defines evidence required before an agent may report work as complete.

## Requirements

### GOV-EVIDENCE-001

**Requirement:** Completion claims must distinguish implemented, validated, partially validated, and not validated work.

### GOV-EVIDENCE-002

**Requirement:** Evidence must include changed files, tests, static analysis, build results, security checks, and limitations as applicable.

### GOV-EVIDENCE-003

**Requirement:** A passing command is evidence only for the behavior it actually exercises.

### GOV-EVIDENCE-004

**Requirement:** Unavailable tools or environments must be reported rather than simulated.

### GOV-EVIDENCE-005

**Requirement:** High-risk work requires rollback and human-review evidence.

## Minimum evidence

- Machine-readable completion result where supported
- Command output or CI links
- Explicit list of unvalidated behavior

## Exceptions

Use the documented exception process.
