---
id: DISC-SUPPLY
title: Software Supply Chain Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - supply-chain
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Software Supply Chain Agent Standard

## Purpose

Controls dependency, build, provenance, and release risk.

## Mandatory rules

### SUPPLY-INVENTORY-001

**Requirement:** Maintain direct and transitive dependency visibility.

**Evidence:** Lockfiles, manifests, or SBOM.

### SUPPLY-REVIEW-002

**Requirement:** Verify source, license, maintenance, vulnerabilities, and necessity before adding dependencies.

**Evidence:** Dependency review.

### SUPPLY-PIN-003

**Requirement:** Use reproducible resolution and controlled updates.

**Evidence:** Lockfile and update policy.

### SUPPLY-BUILD-004

**Requirement:** Protect build environments and separate trusted release workflows from untrusted contributions.

**Evidence:** Build review.

### SUPPLY-PROVENANCE-005

**Requirement:** Generate and retain provenance or equivalent traceability for releases.

**Evidence:** Release evidence.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.

## References

- https://slsa.dev/
- https://baseline.openssf.org/
