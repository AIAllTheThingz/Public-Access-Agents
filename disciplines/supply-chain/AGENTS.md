---
id: DISC-SUPPLY
title: Software Supply Chain Agent Standard
version: 0.2.0
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

This file defines mandatory agent behavior for work governed by the **Software Supply Chain** discipline.

Its objective is to control dependency, build, provenance, vulnerability, licensing, and release-integrity risk.

> Make the smallest safe, reviewable, testable, and evidence-backed change that satisfies the requirement.

## Scope

This discipline applies to:

- dependency inventory
- dependency review
- lockfiles and reproducibility
- SBOM and provenance
- build environment security
- vulnerability and license handling
- release attestation

## Instruction priority

When instructions conflict, apply them in this order:

1. explicit user requirements
2. the nearest more-specific `AGENTS.md`
3. this discipline `AGENTS.md`
4. the supporting standards in this package
5. repository conventions
6. general agent preferences

Do not resolve a material conflict silently. Follow the higher-priority instruction and report the conflict.

## Required supporting standards

Read every applicable supporting standard before implementation:

- [`standards/DEPENDENCY_INVENTORY_STANDARD.md`](standards/DEPENDENCY_INVENTORY_STANDARD.md)
- [`standards/DEPENDENCY_REVIEW_STANDARD.md`](standards/DEPENDENCY_REVIEW_STANDARD.md)
- [`standards/LOCKFILE_REPRODUCIBILITY_STANDARD.md`](standards/LOCKFILE_REPRODUCIBILITY_STANDARD.md)
- [`standards/SBOM_PROVENANCE_STANDARD.md`](standards/SBOM_PROVENANCE_STANDARD.md)
- [`standards/BUILD_ENVIRONMENT_STANDARD.md`](standards/BUILD_ENVIRONMENT_STANDARD.md)
- [`standards/VULNERABILITY_LICENSE_STANDARD.md`](standards/VULNERABILITY_LICENSE_STANDARD.md)
- [`standards/RELEASE_ATTESTATION_STANDARD.md`](standards/RELEASE_ATTESTATION_STANDARD.md)
- [`standards/COMPLETION_EVIDENCE.md`](standards/COMPLETION_EVIDENCE.md)

The supporting standards extend this file. This `AGENTS.md` takes precedence if wording conflicts.

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

## Non-negotiable behavior

- Inspect existing code, configuration, contracts, tests, documentation, ownership, and operational context before changing anything.
- Do not invent production values, identities, endpoints, schemas, credentials, infrastructure, legal obligations, or compatibility promises.
- Classify risk and identify trust boundaries, sensitive data, state changes, and reversibility.
- Default to safe, narrow, reversible behavior and stop when prerequisites or target identity are ambiguous.
- Do not weaken tests, security, privacy, accessibility, approvals, or evidence requirements to make work appear complete.
- Preserve public behavior unless change is explicitly authorized and migration or compatibility work is included.
- Keep examples fictitious and keep secrets and sensitive data out of source, tests, logs, errors, artifacts, and documentation.
- Record exact commands, results, limitations, assumptions, exceptions, and remaining risk.

## Required working method

1. Determine whether this discipline applies and document the reason.
2. Inspect the current implementation, contracts, evidence, and ownership.
3. Identify risk, trust boundaries, dependencies, failure modes, and affected users or operators.
4. Define acceptance criteria and required evidence before implementation.
5. Make the smallest coherent change.
6. Add or update tests, documentation, runbooks, contracts, diagrams, and evidence as applicable.
7. Run package-specific validation and review the final diff for unrelated or unsafe changes.
8. Report what changed, what was verified, what was not verified, and what risk remains.

## Completion gate

Do not report this discipline complete until:

- applicable mandatory rules are satisfied
- supporting standards were considered
- required evidence is recorded
- checks not run are identified
- limitations, assumptions, exceptions, and remaining risks are stated

## References

- [SLSA](https://slsa.dev/)
- [OpenSSF Security Baseline](https://baseline.openssf.org/)
