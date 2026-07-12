---
id: DISC-CICD
title: CI/CD Agent Standard
version: 0.2.0
status: baseline
applies_to:
  - ci-cd
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---

# CI/CD Agent Standard

## Purpose

This file defines mandatory agent behavior for work governed by the **CI/CD** discipline.

Its objective is to secure and stabilize automated build, test, artifact, approval, and deployment workflows.

> Make the smallest safe, reviewable, testable, and evidence-backed change that satisfies the requirement.

## Scope

This discipline applies to:

- workflow design and triggers
- permissions and secrets
- dependency pinning
- build and test gates
- artifact provenance
- deployment environments
- rollback and recovery

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

- [`standards/WORKFLOW_DESIGN_STANDARD.md`](standards/WORKFLOW_DESIGN_STANDARD.md)
- [`standards/PERMISSIONS_SECRETS_STANDARD.md`](standards/PERMISSIONS_SECRETS_STANDARD.md)
- [`standards/DEPENDENCY_PINNING_STANDARD.md`](standards/DEPENDENCY_PINNING_STANDARD.md)
- [`standards/BUILD_TEST_GATES_STANDARD.md`](standards/BUILD_TEST_GATES_STANDARD.md)
- [`standards/ARTIFACT_PROVENANCE_STANDARD.md`](standards/ARTIFACT_PROVENANCE_STANDARD.md)
- [`standards/DEPLOYMENT_ENVIRONMENT_STANDARD.md`](standards/DEPLOYMENT_ENVIRONMENT_STANDARD.md)
- [`standards/ROLLBACK_RECOVERY_STANDARD.md`](standards/ROLLBACK_RECOVERY_STANDARD.md)
- [`standards/COMPLETION_EVIDENCE.md`](standards/COMPLETION_EVIDENCE.md)

The supporting standards extend this file. This `AGENTS.md` takes precedence if wording conflicts.

## Mandatory rules

### CICD-PIN-001

**Requirement:** Pin third-party actions and tools to reviewed versions or immutable references where practical.

**Evidence:** Workflow review.

### CICD-PERM-002

**Requirement:** Grant minimum token and environment permissions.

**Evidence:** Permission review.

### CICD-SECRETS-003

**Requirement:** Use protected secret stores and prevent secret exposure to untrusted code.

**Evidence:** Secret-path review.

### CICD-GATES-004

**Requirement:** Require proportionate tests, security checks, and approvals before promotion.

**Evidence:** Pipeline evidence.

### CICD-ARTIFACT-005

**Requirement:** Preserve provenance, integrity, retention, and traceability for release artifacts.

**Evidence:** Artifact metadata.

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

- [GitHub Actions security hardening guidance](https://docs.github.com/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
