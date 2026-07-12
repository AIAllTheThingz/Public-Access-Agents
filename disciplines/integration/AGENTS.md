---
id: DISC-INT
title: Integration Engineering Agent Standard
version: 0.2.0
status: baseline
applies_to:
  - integration
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---

# Integration Engineering Agent Standard

## Purpose

This file defines mandatory agent behavior for work governed by the **Integration Engineering** discipline.

Its objective is to control assumptions, contracts, data handling, ownership, and failure modes at system boundaries.

> Make the smallest safe, reviewable, testable, and evidence-backed change that satisfies the requirement.

## Scope

This discipline applies to:

- integration ownership and contracts
- transport and schema behavior
- delivery and resilience
- data mapping and validation
- security and trust
- testing and migration
- operations and support

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

- [`standards/CONTRACT_OWNERSHIP_STANDARD.md`](standards/CONTRACT_OWNERSHIP_STANDARD.md)
- [`standards/RESILIENCE_DELIVERY_STANDARD.md`](standards/RESILIENCE_DELIVERY_STANDARD.md)
- [`standards/DATA_MAPPING_VALIDATION_STANDARD.md`](standards/DATA_MAPPING_VALIDATION_STANDARD.md)
- [`standards/SECURITY_STANDARD.md`](standards/SECURITY_STANDARD.md)
- [`standards/TESTING_STANDARD.md`](standards/TESTING_STANDARD.md)
- [`standards/CHANGE_MIGRATION_STANDARD.md`](standards/CHANGE_MIGRATION_STANDARD.md)
- [`standards/OPERATIONS_STANDARD.md`](standards/OPERATIONS_STANDARD.md)
- [`standards/COMPLETION_EVIDENCE.md`](standards/COMPLETION_EVIDENCE.md)

The supporting standards extend this file. This `AGENTS.md` takes precedence if wording conflicts.

## Mandatory rules

### INT-CONTRACT-001

**Requirement:** Define ownership, schema, transport, authentication, timeouts, retries, and compatibility.

**Evidence:** Integration contract.

### INT-RESILIENCE-002

**Requirement:** Handle partial failure, duplicate delivery, reordering, and dependency outages.

**Evidence:** Failure-injection tests.

### INT-DATA-003

**Requirement:** Validate and minimize transferred data; classify sensitive fields.

**Evidence:** Data-flow review.

### INT-TEST-004

**Requirement:** Use contract or integration tests against representative behavior.

**Evidence:** Integration test evidence.

### INT-CHANGE-005

**Requirement:** Coordinate breaking changes and migration windows.

**Evidence:** Version and rollout plan.

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
