---
id: DISC-REL
title: Release Engineering Agent Standard
version: 0.2.0
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

This file defines mandatory agent behavior for work governed by the **Release Engineering** discipline.

Its objective is to make versions, releases, promotion, rollout, rollback, artifacts, and support handoff repeatable and traceable.

> Make the smallest safe, reviewable, testable, and evidence-backed change that satisfies the requirement.

## Scope

This discipline applies to:

- versioning and compatibility
- release planning
- artifact promotion
- release notes
- deployment and rollout
- rollback and roll-forward
- signing and attestation

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

- [`standards/VERSIONING_COMPATIBILITY_STANDARD.md`](standards/VERSIONING_COMPATIBILITY_STANDARD.md)
- [`standards/RELEASE_PLANNING_STANDARD.md`](standards/RELEASE_PLANNING_STANDARD.md)
- [`standards/ARTIFACT_PROMOTION_STANDARD.md`](standards/ARTIFACT_PROMOTION_STANDARD.md)
- [`standards/RELEASE_NOTES_STANDARD.md`](standards/RELEASE_NOTES_STANDARD.md)
- [`standards/DEPLOYMENT_ROLLOUT_STANDARD.md`](standards/DEPLOYMENT_ROLLOUT_STANDARD.md)
- [`standards/ROLLBACK_ROLLFORWARD_STANDARD.md`](standards/ROLLBACK_ROLLFORWARD_STANDARD.md)
- [`standards/SIGNING_ATTESTATION_STANDARD.md`](standards/SIGNING_ATTESTATION_STANDARD.md)
- [`standards/COMPLETION_EVIDENCE.md`](standards/COMPLETION_EVIDENCE.md)

The supporting standards extend this file. This `AGENTS.md` takes precedence if wording conflicts.

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
