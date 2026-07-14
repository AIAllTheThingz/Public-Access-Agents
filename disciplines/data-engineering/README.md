---
id: DISC-PKG-DATA
title: Data Engineering Discipline Package
version: 0.1.0
status: baseline
---
# Data Engineering Discipline Package

## Purpose

This package provides project-agnostic, language-neutral standards for **Data Engineering** work.

It exists to make data contracts, lineage, quality, privacy, reproducibility, recovery, and operational ownership explicit. The package converts broad expectations into explicit agent instructions, review questions, required evidence, and completion gates.

This package is a **baseline**, not a claim of universal completeness. The adopting repository remains responsible for selecting applicable obligations, declaring its environment, assigning accountable owners, and adding stricter project or organizational requirements.

## What this package controls

- data contracts and schemas
- lineage and metadata
- quality rules
- pipeline reliability
- privacy and governance
- replay and backfill
- data observability

## When to adopt this package

Adopt this discipline when one or more of the following are true:

- data is ingested, transformed, moved, aggregated, or published
- schemas or quality expectations change
- backfills or replay are possible
- sensitive or regulated data is processed

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
disciplines/data-engineering/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── standards/
│   ├── DATA_CONTRACT_STANDARD.md
│   ├── LINEAGE_METADATA_STANDARD.md
│   ├── QUALITY_STANDARD.md
│   ├── PIPELINE_RELIABILITY_STANDARD.md
│   ├── PRIVACY_GOVERNANCE_STANDARD.md
│   ├── REPLAY_BACKFILL_STANDARD.md
│   ├── OBSERVABILITY_STANDARD.md
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
| [`Data Contract Standard`](standards/DATA_CONTRACT_STANDARD.md) | Define producers, consumers, ownership, schema, semantics, quality, compatibility, freshness, retention, and support expectations. |
| [`Lineage and Metadata Standard`](standards/LINEAGE_METADATA_STANDARD.md) | Record sources, transformations, destinations, ownership, classifications, schedules, versions, and retention. |
| [`Data Quality Standard`](standards/QUALITY_STANDARD.md) | Define and test completeness, uniqueness, validity, timeliness, ranges, referential expectations, reconciliation, and alert thresholds. |
| [`Pipeline Reliability Standard`](standards/PIPELINE_RELIABILITY_STANDARD.md) | Define idempotency, checkpoints, retries, partial failure, late data, ordering, duplicate handling, recovery, and resource limits. |
| [`Data Privacy and Governance Standard`](standards/PRIVACY_GOVERNANCE_STANDARD.md) | Minimize sensitive data, enforce access and retention, document lawful or approved purposes, and protect nonproduction copies. |
| [`Replay and Backfill Standard`](standards/REPLAY_BACKFILL_STANDARD.md) | Plan scope, ordering, throttling, deduplication, reconciliation, observability, rollback, and downstream impact. |
| [`Data Observability Standard`](standards/OBSERVABILITY_STANDARD.md) | Measure freshness, volume, quality, lineage failures, processing latency, backlog, cost, and consumer impact. |
| [`Data Engineering Completion Evidence`](standards/COMPLETION_EVIDENCE.md) | Record contracts, lineage, quality results, replay tests, privacy review, operational metrics, assumptions, and residual risks. |

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

- data contract and ownership
- lineage documentation
- quality-test results
- replay or backfill evidence
- privacy and access review
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

- treating schema as the whole contract
- hiding data-quality failures
- running irreversible backfills
- copying production data casually
- ignoring downstream consumers

Other common mistakes include copying only selected controls without documenting omissions, declaring success without evidence, treating a scanner or checklist as proof by itself, and assuming the package removes the need for human accountability.

## Companion disciplines

This package commonly composes with:

- [`Database Engineering`](../database/)
- [`Privacy and Data Governance`](../privacy/)
- [`Integration Engineering`](../integration/)
- [`Observability`](../observability/)
- [`Site Reliability Engineering`](../sre/)
- [`Testing and Quality Engineering`](../testing/)

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

Adopting this package does not prove that data engineering work is complete. Completion requires implementation, verification, evidence, accountable review, and explicit disclosure of remaining limitations.
