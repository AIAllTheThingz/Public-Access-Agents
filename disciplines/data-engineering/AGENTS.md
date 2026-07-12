---
id: DISC-DATA
title: Data Engineering Agent Standard
version: 0.2.0
status: baseline
applies_to:
  - data-engineering
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---

# Data Engineering Agent Standard

## Purpose

This file defines mandatory agent behavior for work governed by the **Data Engineering** discipline.

Its objective is to make data contracts, lineage, quality, privacy, reproducibility, recovery, and operational ownership explicit.

> Make the smallest safe, reviewable, testable, and evidence-backed change that satisfies the requirement.

## Scope

This discipline applies to:

- data contracts and schemas
- lineage and metadata
- quality rules
- pipeline reliability
- privacy and governance
- replay and backfill
- data observability

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

- [`standards/DATA_CONTRACT_STANDARD.md`](standards/DATA_CONTRACT_STANDARD.md)
- [`standards/LINEAGE_METADATA_STANDARD.md`](standards/LINEAGE_METADATA_STANDARD.md)
- [`standards/QUALITY_STANDARD.md`](standards/QUALITY_STANDARD.md)
- [`standards/PIPELINE_RELIABILITY_STANDARD.md`](standards/PIPELINE_RELIABILITY_STANDARD.md)
- [`standards/PRIVACY_GOVERNANCE_STANDARD.md`](standards/PRIVACY_GOVERNANCE_STANDARD.md)
- [`standards/REPLAY_BACKFILL_STANDARD.md`](standards/REPLAY_BACKFILL_STANDARD.md)
- [`standards/OBSERVABILITY_STANDARD.md`](standards/OBSERVABILITY_STANDARD.md)
- [`standards/COMPLETION_EVIDENCE.md`](standards/COMPLETION_EVIDENCE.md)

The supporting standards extend this file. This `AGENTS.md` takes precedence if wording conflicts.

## Mandatory rules

### DATA-CONTRACT-001

**Requirement:** Define schemas, ownership, quality expectations, and compatibility.

**Evidence:** Data contract.

### DATA-LINEAGE-002

**Requirement:** Record sources, transformations, destinations, and retention.

**Evidence:** Lineage documentation.

### DATA-QUALITY-003

**Requirement:** Validate completeness, uniqueness, timeliness, ranges, and referential expectations.

**Evidence:** Data-quality results.

### DATA-REPLAY-004

**Requirement:** Design idempotent or replay-safe processing where applicable.

**Evidence:** Replay test.

### DATA-PRIVACY-005

**Requirement:** Minimize sensitive data and enforce retention and access requirements.

**Evidence:** Privacy review.

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
