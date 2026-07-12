---
id: DISC-PKG-DOC
title: Documentation Discipline Package
version: 0.1.0
status: baseline
---
# Documentation Discipline Package

## Purpose

This package provides project-agnostic, language-neutral standards for **Documentation** work.

It exists to treat documentation as part of the deliverable and keep it accurate, discoverable, testable, and usable by non-authors. The package converts broad expectations into explicit agent instructions, review questions, required evidence, and completion gates.

This package is a **baseline**, not a claim of universal completeness. The adopting repository remains responsible for selecting applicable obligations, declaring its environment, assigning accountable owners, and adding stricter project or organizational requirements.

## What this package controls

- information architecture
- code and API documentation
- operations and runbooks
- user and administrator guides
- decision records
- examples
- review and maintenance

## When to adopt this package

Adopt this discipline when one or more of the following are true:

- software, configuration, behavior, operations, interfaces, deployment, or support processes change
- non-authors need to understand, use, maintain, or recover the system
- material design decisions require a durable record

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
disciplines/documentation/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── standards/
│   ├── INFORMATION_ARCHITECTURE_STANDARD.md
│   ├── CODE_API_DOCUMENTATION_STANDARD.md
│   ├── OPERATIONS_RUNBOOK_STANDARD.md
│   ├── USER_GUIDE_STANDARD.md
│   ├── DECISION_RECORD_STANDARD.md
│   ├── EXAMPLE_STANDARD.md
│   ├── REVIEW_MAINTENANCE_STANDARD.md
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
| [`Information Architecture Standard`](standards/INFORMATION_ARCHITECTURE_STANDARD.md) | Organize documentation by audience and task, provide clear entry points, navigation, ownership, prerequisites, and lifecycle. |
| [`Code and API Documentation Standard`](standards/CODE_API_DOCUMENTATION_STANDARD.md) | Document public contracts, behavior, errors, side effects, security expectations, examples, compatibility, and deprecation. |
| [`Operations and Runbook Standard`](standards/OPERATIONS_RUNBOOK_STANDARD.md) | Document configuration, deployment, diagnostics, common failures, recovery, rollback, access, escalation, and ownership. |
| [`User and Administrator Guide Standard`](standards/USER_GUIDE_STANDARD.md) | Use task-oriented steps, prerequisites, expected outcomes, safe examples, troubleshooting, accessibility, and version context. |
| [`Decision Record Standard`](standards/DECISION_RECORD_STANDARD.md) | Record non-obvious decisions, options, rationale, consequences, status, owners, and supersession. |
| [`Documentation Example Standard`](standards/EXAMPLE_STANDARD.md) | Use fictitious, safe, minimal, runnable examples; validate commands and avoid secrets or internal production identifiers. |
| [`Documentation Review and Maintenance Standard`](standards/REVIEW_MAINTENANCE_STANDARD.md) | Update documentation with behavior, assign owners, review stale material, validate links and examples, and retire obsolete guidance. |
| [`Documentation Completion Evidence`](standards/COMPLETION_EVIDENCE.md) | Record audiences, files updated, example and link validation, reviewer feedback, known gaps, ownership, and maintenance expectations. |

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

- audience and task coverage
- updated operational and user documentation
- validated examples and links
- decision records where needed
- documented ownership and known gaps
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

- writing only for the original author
- copying commands that were not tested
- mixing concepts, procedures, and reference material randomly
- leaving stale screenshots or version claims
- documenting behavior after the change ships

Other common mistakes include copying only selected controls without documenting omissions, declaring success without evidence, treating a scanner or checklist as proof by itself, and assuming the package removes the need for human accountability.

## Companion disciplines

This package commonly composes with:

- [`Architecture and System Design`](../architecture/)
- [`Testing and Quality Engineering`](../testing/)
- [`Site Reliability Engineering`](../sre/)
- [`API Engineering`](../api-engineering/)
- [`Release Engineering`](../release-engineering/)
- [`Accessibility`](../accessibility/)

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

Adopting this package does not prove that documentation work is complete. Completion requires implementation, verification, evidence, accountable review, and explicit disclosure of remaining limitations.
