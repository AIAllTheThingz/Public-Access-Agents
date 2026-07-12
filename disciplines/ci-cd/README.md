---
id: DISC-PKG-CICD
title: CI/CD Discipline Package
version: 0.1.0
status: baseline
---
# CI/CD Discipline Package

## Purpose

This package provides project-agnostic, language-neutral standards for **CI/CD** work.

It exists to secure and stabilize automated build, test, artifact, approval, and deployment workflows. The package converts broad expectations into explicit agent instructions, review questions, required evidence, and completion gates.

This package is a **baseline**, not a claim of universal completeness. The adopting repository remains responsible for selecting applicable obligations, declaring its environment, assigning accountable owners, and adding stricter project or organizational requirements.

## What this package controls

- workflow design and triggers
- permissions and secrets
- dependency pinning
- build and test gates
- artifact provenance
- deployment environments
- rollback and recovery

## When to adopt this package

Adopt this discipline when one or more of the following are true:

- automated workflows build, test, scan, package, release, deploy, or modify infrastructure
- third-party actions or tools execute
- secrets, environments, approvals, or production promotion are involved

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
disciplines/ci-cd/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── standards/
│   ├── WORKFLOW_DESIGN_STANDARD.md
│   ├── PERMISSIONS_SECRETS_STANDARD.md
│   ├── DEPENDENCY_PINNING_STANDARD.md
│   ├── BUILD_TEST_GATES_STANDARD.md
│   ├── ARTIFACT_PROVENANCE_STANDARD.md
│   ├── DEPLOYMENT_ENVIRONMENT_STANDARD.md
│   ├── ROLLBACK_RECOVERY_STANDARD.md
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
| [`Workflow Design Standard`](standards/WORKFLOW_DESIGN_STANDARD.md) | Define triggers, trust boundaries, concurrency, cancellation, retries, timeouts, reusable workflow contracts, and failure behavior. |
| [`Permissions and Secrets Standard`](standards/PERMISSIONS_SECRETS_STANDARD.md) | Use minimum token, environment, runner, cloud, and repository permissions; protect secrets from untrusted code and logs. |
| [`CI/CD Dependency Pinning Standard`](standards/DEPENDENCY_PINNING_STANDARD.md) | Pin actions, images, tools, and reusable workflows to reviewed versions or immutable references with controlled updates. |
| [`Build and Test Gates Standard`](standards/BUILD_TEST_GATES_STANDARD.md) | Require risk-proportionate formatting, build, tests, security checks, approvals, and evidence before promotion. |
| [`Artifact and Provenance Standard`](standards/ARTIFACT_PROVENANCE_STANDARD.md) | Create immutable, identifiable artifacts with checksums, metadata, SBOM or provenance where applicable, retention, and traceability. |
| [`Deployment and Environment Standard`](standards/DEPLOYMENT_ENVIRONMENT_STANDARD.md) | Separate environments, protect approvals, prevent untrusted promotion, use environment-specific configuration, and verify deployment state. |
| [`Pipeline Rollback and Recovery Standard`](standards/ROLLBACK_RECOVERY_STANDARD.md) | Define rollback or roll-forward, failed-deployment containment, partial-success handling, cleanup, audit evidence, and operator intervention. |
| [`CI/CD Completion Evidence`](standards/COMPLETION_EVIDENCE.md) | Record workflow changes, permissions, pins, gates, artifact identity, deployment tests, recovery behavior, limitations, and residual risks. |

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

- workflow and trust-boundary review
- least-permission evidence
- pinned dependency review
- successful required gates
- artifact and deployment traceability
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

- granting write-all permissions
- running secrets in untrusted pull requests
- using floating action tags
- rebuilding different artifacts per environment
- treating a green pipeline as production readiness

Other common mistakes include copying only selected controls without documenting omissions, declaring success without evidence, treating a scanner or checklist as proof by itself, and assuming the package removes the need for human accountability.

## Companion disciplines

This package commonly composes with:

- [`Software Supply Chain`](../supply-chain/)
- [`Testing and Quality Engineering`](../testing/)
- [`Release Engineering`](../release-engineering/)
- [`Application Security`](../application-security/)
- [`Site Reliability Engineering`](../sre/)
- [`Observability`](../observability/)

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
