---
id: DISC-PKG-INT
title: Integration Engineering Discipline Package
version: 0.1.0
status: baseline
---
# Integration Engineering Discipline Package

## Purpose

This package provides project-agnostic, language-neutral standards for **Integration Engineering** work.

It exists to control assumptions, contracts, data handling, ownership, and failure modes at system boundaries. The package converts broad expectations into explicit agent instructions, review questions, required evidence, and completion gates.

This package is a **baseline**, not a claim of universal completeness. The adopting repository remains responsible for selecting applicable obligations, declaring its environment, assigning accountable owners, and adding stricter project or organizational requirements.

## What this package controls

- integration ownership and contracts
- transport and schema behavior
- delivery and resilience
- data mapping and validation
- security and trust
- testing and migration
- operations and support

## When to adopt this package

Adopt this discipline when one or more of the following are true:

- two systems exchange data or commands
- a vendor or external service is introduced
- message delivery, retries, duplication, or ordering matter
- a breaking schema or protocol change is planned

Do not omit the package merely because its controls add work. Omit it only when the discipline is genuinely inapplicable and the tailoring decision is documented.

## What this package does not replace

This package does not replace:

- accountable human review
- organization policy, law, regulation, contractual obligations, or professional judgment
- project-specific architecture, risk, data classification, support, or deployment decisions
- language, framework, platform, and project-profile standards
- product, security, privacy, accessibility, legal, or operational specialists where their review is required

## Package structure

```text
disciplines/integration/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── standards/
│   ├── CONTRACT_OWNERSHIP_STANDARD.md
│   ├── RESILIENCE_DELIVERY_STANDARD.md
│   ├── DATA_MAPPING_VALIDATION_STANDARD.md
│   ├── SECURITY_STANDARD.md
│   ├── TESTING_STANDARD.md
│   ├── CHANGE_MIGRATION_STANDARD.md
│   ├── OPERATIONS_STANDARD.md
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
| [`Integration Contract and Ownership Standard`](standards/CONTRACT_OWNERSHIP_STANDARD.md) | Define producer, consumer, owners, schema, transport, authentication, authorization, SLAs, support paths, and compatibility. |
| [`Resilience and Delivery Standard`](standards/RESILIENCE_DELIVERY_STANDARD.md) | Define timeouts, retries, backoff, idempotency, ordering, duplicate handling, dead letters, partial failure, and outage behavior. |
| [`Data Mapping and Validation Standard`](standards/DATA_MAPPING_VALIDATION_STANDARD.md) | Validate source and destination semantics, field mapping, units, formats, null behavior, classification, minimization, and reconciliation. |
| [`Integration Security Standard`](standards/SECURITY_STANDARD.md) | Protect credentials and channels, validate endpoints and certificates, apply least privilege, and constrain untrusted content. |
| [`Integration Testing Standard`](standards/TESTING_STANDARD.md) | Use contract, component, representative-environment, failure-injection, migration, and reconciliation tests. |
| [`Integration Change and Migration Standard`](standards/CHANGE_MIGRATION_STANDARD.md) | Plan version coexistence, sequencing, backfill, cutover, rollback, consumer readiness, and retirement. |
| [`Integration Operations Standard`](standards/OPERATIONS_STANDARD.md) | Define monitoring, alerting, replay, quarantine, reconciliation, incident ownership, runbooks, and support diagnostics. |
| [`Integration Completion Evidence`](standards/COMPLETION_EVIDENCE.md) | Record contracts, mapping, security review, failure tests, migration plans, operational readiness, assumptions, and residual risks. |

## Adoption workflow

1. Read the repository root `AGENTS.md` and governance standards.
2. Confirm that this discipline applies to the project or change.
3. Copy or compose the complete package, not just the README.
4. Preserve the package `AGENTS.md` and stable rule identifiers.
5. Declare project-specific scope, owners, environments, constraints, and required evidence.
6. Select companion language, platform, framework, profile, and discipline packages.
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

- owned integration contract
- data mapping and classification
- failure and duplicate-delivery tests
- migration and rollback plan
- monitoring and reconciliation evidence
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

- assuming exactly-once delivery
- leaving ownership ambiguous
- coupling to undocumented vendor behavior
- retrying non-idempotent operations blindly
- omitting reconciliation and recovery

Other common mistakes include copying only selected controls without documenting omissions, declaring success without evidence, treating a scanner or checklist as proof by itself, and assuming the package removes the need for human accountability.

## Companion disciplines

This package commonly composes with:

- [`API Engineering`](../api-engineering/)
- [`Application Security`](../application-security/)
- [`Data Engineering`](../data-engineering/)
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

Adopting this package does not prove that {data["title"].lower()} work is complete. Completion requires implementation, verification, evidence, accountable review, and explicit disclosure of remaining limitations.
