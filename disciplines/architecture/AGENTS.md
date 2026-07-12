---
id: DISC-ARCH
title: Architecture and System Design Agent Standard
version: 0.2.0
status: baseline
applies_to:
  - architecture
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---

# Architecture and System Design Agent Standard

## Purpose

This file defines mandatory agent behavior for work governed by the **Architecture and System Design** discipline.

Its objective is to keep structural decisions explicit, reviewable, reversible, and aligned with required quality attributes.

> Make the smallest safe, reviewable, testable, and evidence-backed change that satisfies the requirement.

## Scope

This discipline applies to:

- system context and component boundaries
- dependencies and ownership
- quality attributes and trade-offs
- failure modes and recovery
- architecture decisions and evolution

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

- [`standards/SYSTEM_CONTEXT_STANDARD.md`](standards/SYSTEM_CONTEXT_STANDARD.md)
- [`standards/BOUNDARIES_DEPENDENCIES_STANDARD.md`](standards/BOUNDARIES_DEPENDENCIES_STANDARD.md)
- [`standards/QUALITY_ATTRIBUTES_STANDARD.md`](standards/QUALITY_ATTRIBUTES_STANDARD.md)
- [`standards/FAILURE_RESILIENCE_STANDARD.md`](standards/FAILURE_RESILIENCE_STANDARD.md)
- [`standards/ADR_STANDARD.md`](standards/ADR_STANDARD.md)
- [`standards/ARCHITECTURE_VALIDATION_STANDARD.md`](standards/ARCHITECTURE_VALIDATION_STANDARD.md)
- [`standards/EVOLUTION_COMPATIBILITY_STANDARD.md`](standards/EVOLUTION_COMPATIBILITY_STANDARD.md)
- [`standards/COMPLETION_EVIDENCE.md`](standards/COMPLETION_EVIDENCE.md)

The supporting standards extend this file. This `AGENTS.md` takes precedence if wording conflicts.

## Mandatory rules

### ARCH-BOUNDARY-001

**Requirement:** Define components, responsibilities, trust boundaries, dependencies, and ownership.

**Evidence:** Architecture diagram or ADR.

### ARCH-QUALITY-002

**Requirement:** State relevant quality attributes such as availability, security, maintainability, latency, scalability, and recoverability.

**Evidence:** Documented trade-offs and acceptance criteria.

### ARCH-COUPLING-003

**Requirement:** Prefer explicit interfaces and avoid hidden shared state or circular dependencies.

**Evidence:** Dependency review.

### ARCH-FAILURE-004

**Requirement:** Design for dependency failure, partial failure, retries, idempotency, and recovery where applicable.

**Evidence:** Failure-mode analysis.

### ARCH-ADR-005

**Requirement:** Record material, hard-to-reverse decisions as architecture decision records.

**Evidence:** Accepted ADR.

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
