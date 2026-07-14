---
id: DISC-PKG-ACC
title: Accessibility Discipline Package
version: 0.1.0
status: baseline
---
# Accessibility Discipline Package

## Purpose

This package provides project-agnostic, language-neutral standards for **Accessibility** work.

It exists to integrate accessible design, implementation, content, and verification into user-facing work. The package converts broad expectations into explicit agent instructions, review questions, required evidence, and completion gates.

This package is a **baseline**, not a claim of universal completeness. The adopting repository remains responsible for selecting applicable obligations, declaring its environment, assigning accountable owners, and adding stricter project or organizational requirements.

## What this package controls

- WCAG conformance
- semantic structure and ARIA
- keyboard and focus behavior
- forms and errors
- visual, motion, and media accessibility
- manual and automated testing
- remediation

## When to adopt this package

Adopt this discipline when one or more of the following are true:

- users interact with visual, audio, mobile, desktop, document, or web interfaces
- content, controls, navigation, forms, media, or notifications change
- public or employee-facing experiences are delivered

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
disciplines/accessibility/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── standards/
│   ├── WCAG_CONFORMANCE_STANDARD.md
│   ├── SEMANTICS_ARIA_STANDARD.md
│   ├── KEYBOARD_FOCUS_STANDARD.md
│   ├── CONTENT_FORMS_ERRORS_STANDARD.md
│   ├── VISUAL_MOTION_MEDIA_STANDARD.md
│   ├── TESTING_STANDARD.md
│   ├── REMEDIATION_STANDARD.md
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
| [`WCAG Conformance Standard`](standards/WCAG_CONFORMANCE_STANDARD.md) | Target the repository's declared accessibility level, normally WCAG 2.2 AA for web interfaces, and map applicable success criteria to evidence. |
| [`Semantics and ARIA Standard`](standards/SEMANTICS_ARIA_STANDARD.md) | Prefer native semantics, use ARIA only when necessary, preserve names, roles, states, relationships, and reading order. |
| [`Keyboard and Focus Standard`](standards/KEYBOARD_FOCUS_STANDARD.md) | Make all interaction keyboard operable with logical order, visible focus, predictable movement, and managed focus for dynamic interfaces. |
| [`Content, Forms, and Errors Standard`](standards/CONTENT_FORMS_ERRORS_STANDARD.md) | Provide clear labels, instructions, validation, status messages, alternatives, readable language, and recoverable errors. |
| [`Visual, Motion, and Media Standard`](standards/VISUAL_MOTION_MEDIA_STANDARD.md) | Address contrast, reflow, zoom, color independence, reduced motion, flashing, captions, transcripts, and audio descriptions as applicable. |
| [`Accessibility Testing Standard`](standards/TESTING_STANDARD.md) | Combine automated checks with keyboard, zoom, screen-reader, visual, and representative assistive-technology testing. |
| [`Accessibility Remediation Standard`](standards/REMEDIATION_STANDARD.md) | Prioritize blockers, record user impact, avoid regressions, provide workarounds where appropriate, and verify fixes manually. |
| [`Accessibility Completion Evidence`](standards/COMPLETION_EVIDENCE.md) | Record criteria assessed, automated and manual results, assistive technologies, known limitations, exceptions, and remediation ownership. |

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

- applicable conformance criteria
- automated accessibility results
- keyboard and focus test
- screen-reader or assistive-technology evidence
- documented limitations and remediation
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

- relying only on automated scanners
- adding ARIA instead of fixing semantics
- testing mouse interaction only
- using color as the sole signal
- claiming conformance without defined scope

Other common mistakes include copying only selected controls without documenting omissions, declaring success without evidence, treating a scanner or checklist as proof by itself, and assuming the package removes the need for human accountability.

## Companion disciplines

This package commonly composes with:

- [`Testing and Quality Engineering`](../testing/)
- [`Documentation`](../documentation/)
- [`Architecture and System Design`](../architecture/)
- [`Privacy and Data Governance`](../privacy/)
- [`Application Security`](../application-security/)

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

Adopting this package does not prove that accessibility work is complete. Completion requires implementation, verification, evidence, accountable review, and explicit disclosure of remaining limitations.
