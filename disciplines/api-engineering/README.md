---
id: DISC-PKG-API
title: API Engineering Discipline Package
version: 0.1.0
status: baseline
---
# API Engineering Discipline Package

## Purpose

This package provides project-agnostic, language-neutral standards for **API Engineering** work.

It exists to define stable, secure, observable, evolvable, and operable interfaces. The package converts broad expectations into explicit agent instructions, review questions, required evidence, and completion gates.

This package is a **baseline**, not a claim of universal completeness. The adopting repository remains responsible for selecting applicable obligations, declaring its environment, assigning accountable owners, and adding stricter project or organizational requirements.

## What this package controls

- request and response contracts
- authentication and authorization
- validation and errors
- idempotency and retries
- pagination and limits
- versioning and compatibility
- API telemetry and testing

## When to adopt this package

Adopt this discipline when one or more of the following are true:

- HTTP, RPC, event, or programmatic interfaces are created or changed
- clients depend on a contract
- mutating operations require retry or idempotency semantics
- external exposure or compatibility risk exists

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
disciplines/api-engineering/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── standards/
│   ├── CONTRACT_STANDARD.md
│   ├── AUTH_SECURITY_STANDARD.md
│   ├── VERSION_COMPATIBILITY_STANDARD.md
│   ├── ERROR_IDEMPOTENCY_STANDARD.md
│   ├── PAGINATION_LIMITS_STANDARD.md
│   ├── OBSERVABILITY_STANDARD.md
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
| [`API Contract Standard`](standards/CONTRACT_STANDARD.md) | Define operations, schemas, examples, status and error models, authentication, authorization, limits, pagination, idempotency, and lifecycle. |
| [`API Authentication and Security Standard`](standards/AUTH_SECURITY_STANDARD.md) | Enforce identity and object-level authorization server-side, validate trust-boundary data, constrain resources, and prevent sensitive-data leakage. |
| [`API Versioning and Compatibility Standard`](standards/VERSION_COMPATIBILITY_STANDARD.md) | Define compatibility promises, additive change rules, deprecation, sunset, migration, and breaking-change approval. |
| [`Error and Idempotency Standard`](standards/ERROR_IDEMPOTENCY_STANDARD.md) | Use stable machine-readable errors, correlation identifiers, retry guidance, idempotency keys where needed, and explicit duplicate behavior. |
| [`Pagination and Limits Standard`](standards/PAGINATION_LIMITS_STANDARD.md) | Define bounded page sizes, ordering, cursors, quotas, rate limits, payload limits, timeout behavior, and resource-exhaustion controls. |
| [`API Observability Standard`](standards/OBSERVABILITY_STANDARD.md) | Measure availability, latency, errors, saturation, auth failures, and usage without logging secrets or sensitive payloads. |
| [`API Testing Standard`](standards/TESTING_STANDARD.md) | Validate contracts, examples, authorization, validation, pagination, retries, idempotency, compatibility, and dependency failures. |
| [`API Engineering Completion Evidence`](standards/COMPLETION_EVIDENCE.md) | Record contract changes, compatibility analysis, security tests, examples, telemetry, operational limits, and remaining client risks. |

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

- machine-readable API contract
- positive and negative authorization tests
- compatibility analysis
- idempotency and retry tests
- operational limits and telemetry evidence
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

- documenting only happy-path JSON
- using HTTP status codes without stable error bodies
- breaking clients silently
- treating retries as harmless
- exposing unbounded queries or payloads

Other common mistakes include copying only selected controls without documenting omissions, declaring success without evidence, treating a scanner or checklist as proof by itself, and assuming the package removes the need for human accountability.

## Companion disciplines

This package commonly composes with:

- [`Application Security`](../application-security/)
- [`Testing and Quality Engineering`](../testing/)
- [`Integration Engineering`](../integration/)
- [`Observability`](../observability/)
- [`Architecture and System Design`](../architecture/)
- [`Documentation`](../documentation/)

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

Adopting this package does not prove that api engineering work is complete. Completion requires implementation, verification, evidence, accountable review, and explicit disclosure of remaining limitations.
