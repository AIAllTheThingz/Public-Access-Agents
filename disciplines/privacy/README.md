---
id: DISC-PKG-PRIV
title: Privacy and Data Governance Discipline Package
version: 0.1.0
status: baseline
---
# Privacy and Data Governance Discipline Package

## Purpose

This package provides project-agnostic, language-neutral standards for **Privacy and Data Governance** work.

It exists to require deliberate, minimal, transparent, and auditable handling of personal, sensitive, and regulated data. The package converts broad expectations into explicit agent instructions, review questions, required evidence, and completion gates.

This package is a **baseline**, not a claim of universal completeness. The adopting repository remains responsible for selecting applicable obligations, declaring its environment, assigning accountable owners, and adding stricter project or organizational requirements.

## What this package controls

- data inventory and classification
- purpose and minimization
- consent and rights
- access and sharing
- retention and deletion
- logging and analytics
- privacy testing

## When to adopt this package

Adopt this discipline when one or more of the following are true:

- personal, sensitive, confidential, or regulated data is collected or processed
- telemetry, analytics, support artifacts, exports, or sharing are involved
- retention, deletion, correction, or access rights apply

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
disciplines/privacy/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── standards/
│   ├── DATA_INVENTORY_CLASSIFICATION_STANDARD.md
│   ├── MINIMIZATION_PURPOSE_STANDARD.md
│   ├── CONSENT_RIGHTS_STANDARD.md
│   ├── ACCESS_SHARING_STANDARD.md
│   ├── RETENTION_DELETION_STANDARD.md
│   ├── LOGGING_ANALYTICS_STANDARD.md
│   ├── PRIVACY_TESTING_STANDARD.md
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
| [`Data Inventory and Classification Standard`](standards/DATA_INVENTORY_CLASSIFICATION_STANDARD.md) | Identify data elements, purposes, owners, classifications, locations, recipients, transfers, retention, and protection requirements. |
| [`Purpose and Minimization Standard`](standards/MINIMIZATION_PURPOSE_STANDARD.md) | Collect, process, expose, and retain only data necessary for an approved purpose; prevent secondary use without review. |
| [`Consent and Data Rights Standard`](standards/CONSENT_RIGHTS_STANDARD.md) | Define notices, choices, consent where applicable, access, correction, export, deletion, objection, and verification behavior. |
| [`Access and Sharing Standard`](standards/ACCESS_SHARING_STANDARD.md) | Apply least privilege, purpose-bound access, auditable sharing, recipient review, transfer controls, and revocation. |
| [`Retention and Deletion Standard`](standards/RETENTION_DELETION_STANDARD.md) | Define retention triggers, holds, deletion propagation, backups, caches, archives, and verification of lifecycle actions. |
| [`Logging and Analytics Privacy Standard`](standards/LOGGING_ANALYTICS_STANDARD.md) | Exclude or redact sensitive data, minimize identifiers, constrain analytics, and review support and debugging artifacts. |
| [`Privacy Testing Standard`](standards/PRIVACY_TESTING_STANDARD.md) | Test data flows, minimization, access, rights, retention, deletion, exports, logs, and failure behavior with synthetic data. |
| [`Privacy Completion Evidence`](standards/COMPLETION_EVIDENCE.md) | Record inventory, purpose, minimization, access, lifecycle tests, notices, residual risks, approvals, and exceptions. |

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

- data inventory and flow
- purpose and minimization review
- access and sharing controls
- retention and deletion tests
- privacy limitations and approvals
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

- collecting data because it might be useful
- logging full payloads
- treating encryption as complete privacy
- ignoring backups and derived data during deletion
- using production personal data in tests

Other common mistakes include copying only selected controls without documenting omissions, declaring success without evidence, treating a scanner or checklist as proof by itself, and assuming the package removes the need for human accountability.

## Companion disciplines

This package commonly composes with:

- [`Application Security`](../application-security/)
- [`Data Engineering`](../data-engineering/)
- [`Database Engineering`](../database/)
- [`Documentation`](../documentation/)
- [`Observability`](../observability/)
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

Adopting this package does not prove that privacy and data governance work is complete. Completion requires implementation, verification, evidence, accountable review, and explicit disclosure of remaining limitations.
