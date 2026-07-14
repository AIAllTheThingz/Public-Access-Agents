---
id: DISC-PKG-APPSEC
title: Application Security Discipline Package
version: 0.1.0
status: baseline
---
# Application Security Discipline Package

## Purpose

This package provides project-agnostic, language-neutral standards for **Application Security** work.

It exists to turn security requirements into concrete design, implementation, verification, and vulnerability-management work. The package converts broad expectations into explicit agent instructions, review questions, required evidence, and completion gates.

This package is a **baseline**, not a claim of universal completeness. The adopting repository remains responsible for selecting applicable obligations, declaring its environment, assigning accountable owners, and adding stricter project or organizational requirements.

## What this package controls

- authentication and authorization
- input validation and output encoding
- secret and key handling
- secure error behavior
- abuse resistance
- security testing and vulnerability remediation

## When to adopt this package

Adopt this discipline when one or more of the following are true:

- the system accepts untrusted input
- protected operations or sensitive data exist
- the change crosses a trust boundary
- dependencies, cryptography, identity, or authorization are involved

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
disciplines/application-security/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── standards/
│   ├── THREAT_MODELING_STANDARD.md
│   ├── AUTHENTICATION_AUTHORIZATION_STANDARD.md
│   ├── INPUT_OUTPUT_SECURITY_STANDARD.md
│   ├── SECRETS_CRYPTOGRAPHY_STANDARD.md
│   ├── SECURITY_TESTING_STANDARD.md
│   ├── VULNERABILITY_MANAGEMENT_STANDARD.md
│   ├── SECURE_OPERATIONS_STANDARD.md
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
| [`Threat Modeling Standard`](standards/THREAT_MODELING_STANDARD.md) | Define assets, actors, trust boundaries, abuse cases, attack paths, assumptions, and mitigations before material security-sensitive implementation. |
| [`Authentication and Authorization Standard`](standards/AUTHENTICATION_AUTHORIZATION_STANDARD.md) | Define identity, session, credential, authorization, ownership, and negative-access behavior. Enforce authorization at the protected operation and object. |
| [`Input and Output Security Standard`](standards/INPUT_OUTPUT_SECURITY_STANDARD.md) | Validate untrusted input at trust boundaries; use parameterized APIs, safe encoding, bounded parsing, and explicit file, path, command, query, and template handling. |
| [`Secrets and Cryptography Standard`](standards/SECRETS_CRYPTOGRAPHY_STANDARD.md) | Keep secrets out of source and telemetry, use approved secret stores, avoid custom cryptography, define rotation and failure behavior, and document trust anchors. |
| [`Security Testing Standard`](standards/SECURITY_TESTING_STANDARD.md) | Require negative authorization, boundary, abuse, injection, parser, configuration, and dependency-security tests proportionate to risk. |
| [`Vulnerability Management Standard`](standards/VULNERABILITY_MANAGEMENT_STANDARD.md) | Define intake, triage, severity, remediation, verification, disclosure, exception, and dependency-update behavior. |
| [`Secure Operations Standard`](standards/SECURE_OPERATIONS_STANDARD.md) | Define secure defaults, logging boundaries, rate limits, resource controls, break-glass behavior, and operational security ownership. |
| [`Application Security Completion Evidence`](standards/COMPLETION_EVIDENCE.md) | Record threat-model changes, control implementation, tests, scans, residual risk, accepted exceptions, and unverified assumptions. |

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

- threat model or security review
- positive and negative authorization tests
- input and abuse-case tests
- dependency and secret-scan results
- documented residual risks and exceptions
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

- treating authentication as authorization
- relying on client-side checks
- logging secrets or sensitive payloads
- using generic validation without boundary tests
- declaring security complete from a scanner alone

Other common mistakes include copying only selected controls without documenting omissions, declaring success without evidence, treating a scanner or checklist as proof by itself, and assuming the package removes the need for human accountability.

## Companion disciplines

This package commonly composes with:

- [`Architecture and System Design`](../architecture/)
- [`Testing and Quality Engineering`](../testing/)
- [`Privacy and Data Governance`](../privacy/)
- [`Software Supply Chain`](../supply-chain/)
- [`CI/CD`](../ci-cd/)
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

Adopting this package does not prove that application security work is complete. Completion requires implementation, verification, evidence, accountable review, and explicit disclosure of remaining limitations.
