---
id: DISC-PKG-REL
title: Release Engineering Discipline Package
version: 0.1.0
status: baseline
---
# Release Engineering Discipline Package

## Purpose

This package provides project-agnostic, language-neutral standards for **Release Engineering** work.

It exists to make versions, releases, promotion, rollout, rollback, artifacts, and support handoff repeatable and traceable. The package converts broad expectations into explicit agent instructions, review questions, required evidence, and completion gates.

This package is a **baseline**, not a claim of universal completeness. The adopting repository remains responsible for selecting applicable obligations, declaring its environment, assigning accountable owners, and adding stricter project or organizational requirements.

## What this package controls

- versioning and compatibility
- release planning
- artifact promotion
- release notes
- deployment and rollout
- rollback and roll-forward
- signing and attestation

## When to adopt this package

Adopt this discipline when one or more of the following are true:

- software or infrastructure is versioned, packaged, promoted, deployed, published, or handed to operations
- breaking changes, migrations, or coordinated rollout exist
- release artifacts require integrity or provenance

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
disciplines/release-engineering/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── standards/
│   ├── VERSIONING_COMPATIBILITY_STANDARD.md
│   ├── RELEASE_PLANNING_STANDARD.md
│   ├── ARTIFACT_PROMOTION_STANDARD.md
│   ├── RELEASE_NOTES_STANDARD.md
│   ├── DEPLOYMENT_ROLLOUT_STANDARD.md
│   ├── ROLLBACK_ROLLFORWARD_STANDARD.md
│   ├── SIGNING_ATTESTATION_STANDARD.md
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
| [`Versioning and Compatibility Standard`](standards/VERSIONING_COMPATIBILITY_STANDARD.md) | Define versioning, supported versions, compatibility promises, deprecation, migration, and breaking-change approval. |
| [`Release Planning Standard`](standards/RELEASE_PLANNING_STANDARD.md) | Define scope, owners, dependencies, approvals, risk, windows, communications, validation, migration, and support readiness. |
| [`Artifact Promotion Standard`](standards/ARTIFACT_PROMOTION_STANDARD.md) | Promote immutable verified artifacts across environments; do not rebuild release content per environment. |
| [`Release Notes Standard`](standards/RELEASE_NOTES_STANDARD.md) | Describe changes, compatibility, risks, migrations, configuration, known limitations, security impact, and operator or user actions. |
| [`Deployment and Rollout Standard`](standards/DEPLOYMENT_ROLLOUT_STANDARD.md) | Use staged or progressive rollout where appropriate, define health gates, pause criteria, observability, and approval. |
| [`Rollback and Roll-Forward Standard`](standards/ROLLBACK_ROLLFORWARD_STANDARD.md) | Define rollback feasibility, data and schema constraints, roll-forward paths, restoration, verification, and decision ownership. |
| [`Signing and Attestation Standard`](standards/SIGNING_ATTESTATION_STANDARD.md) | Sign or attest artifacts where risk warrants, protect signing identities, verify signatures, and retain provenance. |
| [`Release Engineering Completion Evidence`](standards/COMPLETION_EVIDENCE.md) | Record version, artifact identity, approvals, tests, release notes, rollout, rollback, signatures, limitations, and residual risks. |

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

- version and compatibility decision
- release plan and approvals
- immutable artifact identity
- release notes and migration guidance
- rollout and rollback evidence
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

- rebuilding per environment
- using version numbers without compatibility policy
- publishing release notes after deployment
- assuming rollback is safe after schema changes
- signing artifacts without protecting signing keys

Other common mistakes include copying only selected controls without documenting omissions, declaring success without evidence, treating a scanner or checklist as proof by itself, and assuming the package removes the need for human accountability.

## Companion disciplines

This package commonly composes with:

- [`CI/CD`](../ci-cd/)
- [`Software Supply Chain`](../supply-chain/)
- [`Site Reliability Engineering`](../sre/)
- [`Documentation`](../documentation/)
- [`Testing and Quality Engineering`](../testing/)
- [`Architecture and System Design`](../architecture/)

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

Adopting this package does not prove that release engineering work is complete. Completion requires implementation, verification, evidence, accountable review, and explicit disclosure of remaining limitations.
