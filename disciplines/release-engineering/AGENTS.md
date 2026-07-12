---
id: DISC-REL
title: Release Engineering Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - release-engineering
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Release Engineering Agent Standard

## Purpose

Makes releases repeatable, traceable, reversible, and supportable.

## Mandatory rules

### REL-VERSION-001

**Requirement:** Use a defined versioning and compatibility policy.

**Evidence:** Version decision.

### REL-NOTES-002

**Requirement:** Produce release notes describing changes, risks, migrations, and known limitations.

**Evidence:** Release notes.

### REL-PROMOTE-003

**Requirement:** Promote immutable artifacts rather than rebuilding per environment.

**Evidence:** Artifact identifiers.

### REL-ROLLBACK-004

**Requirement:** Define rollback or roll-forward procedures and constraints.

**Evidence:** Rollback evidence.

### REL-SIGN-005

**Requirement:** Sign or attest release artifacts where risk warrants.

**Evidence:** Signature or attestation evidence.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.
