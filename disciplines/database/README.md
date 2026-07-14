---
id: DISC-PKG-DB
title: Database Engineering Discipline Package
version: 0.1.0
status: baseline
---
# Database Engineering Discipline Package

## Purpose

This package provides project-agnostic, language-neutral standards for **Database Engineering** work.

It exists to protect data integrity, security, performance, compatibility, and recoverability. The package converts broad expectations into explicit agent instructions, review questions, required evidence, and completion gates.

This package is a **baseline**, not a claim of universal completeness. The adopting repository remains responsible for selecting applicable obligations, declaring its environment, assigning accountable owners, and adding stricter project or organizational requirements.

## What this package controls

- schema and data modeling
- migrations and compatibility
- queries and performance
- transactions and concurrency
- access control
- backup and recovery
- database testing

## When to adopt this package

Adopt this discipline when one or more of the following are true:

- schemas, indexes, constraints, stored code, or queries change
- data migration or backfill occurs
- transactional integrity or concurrency matters
- backup, restore, retention, or access control is affected

Do not omit the package merely because its controls add work. Omit it only when the discipline is genuinely inapplicable and the tailoring decision is documented.

## What this package does not replace

This package does not replace:

- accountable human review
- organization policy, law, regulation, contractual obligations, or professional judgment
- project-specific architecture, risk, data classification, support, or deployment decisions
- language, framework, platform, virtualization, operating-system, networking, and project-profile standards
- product, security, privacy, accessibility, legal, or operational specialists where their review is required

## Package structure

```text
disciplines/database/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── standards/
│   ├── SCHEMA_MODELING_STANDARD.md
│   ├── MIGRATION_STANDARD.md
│   ├── QUERY_PERFORMANCE_STANDARD.md
│   ├── TRANSACTION_INTEGRITY_STANDARD.md
│   ├── SECURITY_ACCESS_STANDARD.md
│   ├── BACKUP_RECOVERY_STANDARD.md
│   ├── TESTING_STANDARD.md
│   └── COMPLETION_EVIDENCE.md
├── templates/
│   ├── ADOPTION_CHECKLIST.md
│   ├── REVIEW_CHECKLIST.md
│   └── EVIDENCE_RECORD_TEMPLATE.md
└── examples/
    └── ADOPTION_EXAMPLE.md
```

## Normative entry point

Start with [`AGENTS.md`](AGENTS.md). It contains the mandatory agent rules, preserves the discipline's stable rule identifiers, defines instruction precedence, and points to the supporting standards.

[`MANIFEST.md`](MANIFEST.md) defines the package inventory and acceptance checks.

## Supporting standards

| Standard | Purpose |
|---|---|
| [`Schema and Modeling Standard`](standards/SCHEMA_MODELING_STANDARD.md) | Define keys, constraints, relationships, types, nullability, ownership, lifecycle, and domain invariants at the appropriate layer. |
| [`Database Migration Standard`](standards/MIGRATION_STANDARD.md) | Use versioned, reviewable, bounded, observable, forward-compatible migrations with rollback or roll-forward plans. |
| [`Query and Performance Standard`](standards/QUERY_PERFORMANCE_STANDARD.md) | Use parameterized queries, bounded result sets, reviewed plans, appropriate indexes, and evidence for material query changes. |
| [`Transaction and Integrity Standard`](standards/TRANSACTION_INTEGRITY_STANDARD.md) | Define isolation, locking, consistency, idempotency, concurrency, retry, and failure behavior. |
| [`Database Security and Access Standard`](standards/SECURITY_ACCESS_STANDARD.md) | Separate administrative and application identities, apply least privilege, protect credentials, encrypt appropriately, and audit privileged access. |
| [`Backup and Recovery Standard`](standards/BACKUP_RECOVERY_STANDARD.md) | Define backup scope, retention, encryption, restore objectives, recovery sequencing, verification, and ownership. |
| [`Database Testing Standard`](standards/TESTING_STANDARD.md) | Test migrations, constraints, concurrency, rollback or roll-forward, representative data volumes, query plans, and restore procedures. |
| [`Database Completion Evidence`](standards/COMPLETION_EVIDENCE.md) | Record migration results, query plans, integrity tests, access review, backup or restore evidence, limitations, and residual risks. |

## Adoption workflow

1. Read the repository root `AGENTS.md` and governance standards.
2. Confirm that this discipline applies to the project or change.
3. Copy or compose the complete package, not just the README.
4. Preserve the package `AGENTS.md` and stable rule identifiers.
5. Declare project-specific scope, owners, environments, constraints, and required evidence.
6. Select companion language, framework, platform, virtualization, operating-system, networking, profile, and discipline packages.
7. Add stricter nested `AGENTS.md` files where directories require more specific controls.
8. Complete the adoption checklist and review checklist.
9. Run the repository validator and relative-link checker.
10. Obtain accountable review before promoting the tailored package for normal use.

## Project tailoring checklist

Before adoption, the project must answer:

- What work, components, data, environments, and users are in scope?
- Who owns implementation, review, approval, operations, exceptions, and follow-up?
- What risk classification applies?
- What trust boundaries, external dependencies, and sensitive data are involved?
- Which requirements are mandatory, conditionally applicable, or provably inapplicable?
- What tools, tests, review methods, environments, and evidence are required?
- What compatibility, migration, rollback, recovery, and support constraints exist?
- What laws, regulations, contracts, organization policies, or external standards apply?
- Where will evidence, decisions, exceptions, and residual risk be recorded?
- What would prevent the work from being reported complete?

## Required evidence

Typical completion evidence includes:

- reviewed schema and migration
- query-plan evidence
- constraint and concurrency tests
- least-privilege review
- restore or recovery evidence
- exact validation commands and results
- checks not run and the reason
- affected environments and representative test conditions
- accepted exceptions and expiration or review dates
- known limitations, unresolved risks, owners, and follow-up actions

Evidence must distinguish **planned**, **implemented**, **tested**, **reviewed**, and **operationally verified**. These are not interchangeable states, despite humanity's recurring attempts to treat them as synonyms.

## Validation

Validate the standards repository itself with:

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
```

The adopting project must also define discipline-specific validation commands and review procedures. This package intentionally does not invent tool names, environments, credentials, endpoints, data sets, or production targets.

## Common failure modes

- using application checks instead of database constraints
- running unbounded migrations
- assuming rollback is always possible
- testing only empty databases
- granting broad shared credentials

Other common mistakes include copying only selected controls without documenting omissions, declaring success without evidence, treating a scanner or checklist as proof by itself, and assuming the package removes the need for human accountability.

## Companion disciplines

This package commonly composes with:

- [`Architecture and System Design`](../architecture/)
- [`Application Security`](../application-security/)
- [`Data Engineering`](../data-engineering/)
- [`Privacy and Data Governance`](../privacy/)
- [`Testing and Quality Engineering`](../testing/)
- [`Site Reliability Engineering`](../sre/)

Companion disciplines supplement this package. They do not replace its applicable rules.

## Templates and example

- [`ADOPTION_CHECKLIST.md`](templates/ADOPTION_CHECKLIST.md) helps tailor the package to a repository.
- [`REVIEW_CHECKLIST.md`](templates/REVIEW_CHECKLIST.md) supports change and package review.
- [`EVIDENCE_RECORD_TEMPLATE.md`](templates/EVIDENCE_RECORD_TEMPLATE.md) provides a repeatable evidence structure.
- [`ADOPTION_EXAMPLE.md`](examples/ADOPTION_EXAMPLE.md) shows how to compose this discipline with governance and other standards.

Templates are starting points. Replace placeholders with reviewed project facts and never insert production secrets or sensitive identifiers.

## Maturity and maintenance

Status: **baseline**

A baseline package is usable for adoption and review but should be expected to evolve. Changes must:

- preserve stable identifiers unless a documented breaking change is approved
- update the README, manifest, templates, and examples when package behavior changes
- keep requirements specific, testable, risk-proportionate, and evidence-based
- avoid duplicating shared governance when a reference is sufficient
- run repository validation and link checking
- state compatibility, migration, and deprecation impact

## Completion statement

Adopting this package does not prove that database engineering work is complete. Completion requires implementation, verification, evidence, accountable review, and explicit disclosure of remaining limitations.
