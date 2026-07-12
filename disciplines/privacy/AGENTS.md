---
id: DISC-PRIV
title: Privacy and Data Governance Agent Standard
version: 0.2.0
status: baseline
applies_to:
  - privacy
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---

# Privacy and Data Governance Agent Standard

## Purpose

This file defines mandatory agent behavior for work governed by the **Privacy and Data Governance** discipline.

Its objective is to require deliberate, minimal, transparent, and auditable handling of personal, sensitive, and regulated data.

> Make the smallest safe, reviewable, testable, and evidence-backed change that satisfies the requirement.

## Scope

This discipline applies to:

- data inventory and classification
- purpose and minimization
- consent and rights
- access and sharing
- retention and deletion
- logging and analytics
- privacy testing

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

- [`standards/DATA_INVENTORY_CLASSIFICATION_STANDARD.md`](standards/DATA_INVENTORY_CLASSIFICATION_STANDARD.md)
- [`standards/MINIMIZATION_PURPOSE_STANDARD.md`](standards/MINIMIZATION_PURPOSE_STANDARD.md)
- [`standards/CONSENT_RIGHTS_STANDARD.md`](standards/CONSENT_RIGHTS_STANDARD.md)
- [`standards/ACCESS_SHARING_STANDARD.md`](standards/ACCESS_SHARING_STANDARD.md)
- [`standards/RETENTION_DELETION_STANDARD.md`](standards/RETENTION_DELETION_STANDARD.md)
- [`standards/LOGGING_ANALYTICS_STANDARD.md`](standards/LOGGING_ANALYTICS_STANDARD.md)
- [`standards/PRIVACY_TESTING_STANDARD.md`](standards/PRIVACY_TESTING_STANDARD.md)
- [`standards/COMPLETION_EVIDENCE.md`](standards/COMPLETION_EVIDENCE.md)

The supporting standards extend this file. This `AGENTS.md` takes precedence if wording conflicts.

## Mandatory rules

### PRIV-INVENTORY-001

**Requirement:** Identify collected data, purpose, owner, classification, location, recipients, and retention.

**Evidence:** Data inventory.

### PRIV-MINIMIZE-002

**Requirement:** Collect and retain only data necessary for the stated purpose.

**Evidence:** Minimization review.

### PRIV-ACCESS-003

**Requirement:** Enforce least privilege and auditable access.

**Evidence:** Access-control evidence.

### PRIV-LOGS-004

**Requirement:** Exclude or redact sensitive data from logs, analytics, errors, and support artifacts.

**Evidence:** Log review.

### PRIV-LIFECYCLE-005

**Requirement:** Define deletion, correction, export, and retention behavior as applicable.

**Evidence:** Lifecycle test evidence.

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
