---
id: DISC-DB
title: Database Engineering Agent Standard
version: 0.2.0
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

This file defines mandatory agent behavior for work governed by the **Database Engineering** discipline.

Its objective is to protect data integrity, security, performance, compatibility, and recoverability.

> Make the smallest safe, reviewable, testable, and evidence-backed change that satisfies the requirement.

## Scope

This discipline applies to:

- schema and data modeling
- migrations and compatibility
- queries and performance
- transactions and concurrency
- access control
- backup and recovery
- database testing

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

- [`standards/SCHEMA_MODELING_STANDARD.md`](standards/SCHEMA_MODELING_STANDARD.md)
- [`standards/MIGRATION_STANDARD.md`](standards/MIGRATION_STANDARD.md)
- [`standards/QUERY_PERFORMANCE_STANDARD.md`](standards/QUERY_PERFORMANCE_STANDARD.md)
- [`standards/TRANSACTION_INTEGRITY_STANDARD.md`](standards/TRANSACTION_INTEGRITY_STANDARD.md)
- [`standards/SECURITY_ACCESS_STANDARD.md`](standards/SECURITY_ACCESS_STANDARD.md)
- [`standards/BACKUP_RECOVERY_STANDARD.md`](standards/BACKUP_RECOVERY_STANDARD.md)
- [`standards/TESTING_STANDARD.md`](standards/TESTING_STANDARD.md)
- [`standards/COMPLETION_EVIDENCE.md`](standards/COMPLETION_EVIDENCE.md)

The supporting standards extend this file. This `AGENTS.md` takes precedence if wording conflicts.

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
