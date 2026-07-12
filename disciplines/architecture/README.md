---
id: DISC-PKG-ARCH
title: Architecture and System Design Discipline Package
version: 0.1.0
status: baseline
---
# Architecture and System Design Discipline Package

## Purpose

This package provides project-agnostic, language-neutral standards for **Architecture and System Design** work.

It exists to keep structural decisions explicit, reviewable, reversible, and aligned with required quality attributes. The package converts broad expectations into explicit agent instructions, review questions, required evidence, and completion gates.

This package is a **baseline**, not a claim of universal completeness. The adopting repository remains responsible for selecting applicable obligations, declaring its environment, assigning accountable owners, and adding stricter project or organizational requirements.

## What this package controls

- system context and component boundaries
- dependencies and ownership
- quality attributes and trade-offs
- failure modes and recovery
- architecture decisions and evolution

## When to adopt this package

Adopt this discipline when one or more of the following are true:

- a new component, service, data store, or external dependency is introduced
- a public contract or trust boundary changes
- availability, scalability, latency, recoverability, or maintainability is material
- the decision is expensive or difficult to reverse

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
disciplines/architecture/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── standards/
│   ├── SYSTEM_CONTEXT_STANDARD.md
│   ├── BOUNDARIES_DEPENDENCIES_STANDARD.md
│   ├── QUALITY_ATTRIBUTES_STANDARD.md
│   ├── FAILURE_RESILIENCE_STANDARD.md
│   ├── ADR_STANDARD.md
│   ├── ARCHITECTURE_VALIDATION_STANDARD.md
│   ├── EVOLUTION_COMPATIBILITY_STANDARD.md
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
| [`System Context Standard`](standards/SYSTEM_CONTEXT_STANDARD.md) | Document users, systems, external dependencies, data flows, ownership, trust boundaries, deployment context, and operational responsibility. |
| [`Boundaries and Dependencies Standard`](standards/BOUNDARIES_DEPENDENCIES_STANDARD.md) | Assign cohesive responsibilities, explicit interfaces, dependency direction, failure ownership, and allowed coupling. Avoid hidden shared state and circular dependencies. |
| [`Quality Attributes Standard`](standards/QUALITY_ATTRIBUTES_STANDARD.md) | Translate availability, security, performance, scalability, maintainability, portability, accessibility, and recovery needs into measurable design constraints. |
| [`Failure and Resilience Standard`](standards/FAILURE_RESILIENCE_STANDARD.md) | Model dependency failure, partial failure, retries, timeouts, idempotency, degradation, recovery, and data consistency. |
| [`Architecture Decision Record Standard`](standards/ADR_STANDARD.md) | Record material decisions with context, options, trade-offs, consequences, status, owners, and reversal or migration considerations. |
| [`Architecture Validation Standard`](standards/ARCHITECTURE_VALIDATION_STANDARD.md) | Use diagrams, dependency checks, prototypes, load tests, failure tests, and review evidence to validate risky assumptions. |
| [`Evolution and Compatibility Standard`](standards/EVOLUTION_COMPATIBILITY_STANDARD.md) | Plan contract evolution, migration, coexistence, deprecation, rollback, and ownership when architecture changes cross boundaries. |
| [`Architecture Completion Evidence`](standards/COMPLETION_EVIDENCE.md) | Record diagrams, ADRs, quality-attribute decisions, failure analysis, validation results, assumptions, and unresolved risks. |

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

- system context and component diagrams
- accepted ADRs
- quality-attribute acceptance criteria
- failure-mode analysis
- validation of high-risk assumptions
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

- drawing diagrams without decisions
- inventing infrastructure details
- hiding coupling behind vague abstractions
- ignoring partial failure and recovery
- claiming scalability without evidence

Other common mistakes include copying only selected controls without documenting omissions, declaring success without evidence, treating a scanner or checklist as proof by itself, and assuming the package removes the need for human accountability.

## Companion disciplines

This package commonly composes with:

- [`Application Security`](../application-security/)
- [`Testing and Quality Engineering`](../testing/)
- [`Observability`](../observability/)
- [`Site Reliability Engineering`](../sre/)
- [`Database Engineering`](../database/)
- [`Integration Engineering`](../integration/)

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
