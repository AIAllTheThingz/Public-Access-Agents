---
id: DISC-ACC
title: Accessibility Agent Standard
version: 0.2.0
status: baseline
applies_to:
  - accessibility
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---

# Accessibility Agent Standard

## Purpose

This file defines mandatory agent behavior for work governed by the **Accessibility** discipline.

Its objective is to integrate accessible design, implementation, content, and verification into user-facing work.

> Make the smallest safe, reviewable, testable, and evidence-backed change that satisfies the requirement.

## Scope

This discipline applies to:

- WCAG conformance
- semantic structure and ARIA
- keyboard and focus behavior
- forms and errors
- visual, motion, and media accessibility
- manual and automated testing
- remediation

## Instruction priority

When instructions conflict, apply them in this order:

1. explicit user requirements
2. the nearest more-specific `AGENTS.md`
3. this discipline `AGENTS.md`
4. the supporting standards in this package
5. repository conventions
6. general agent preferences

Do not resolve a material conflict silently. Follow the higher-priority instruction and report the conflict.

## Required supporting standards

Read every applicable supporting standard before implementation:

- [`standards/WCAG_CONFORMANCE_STANDARD.md`](standards/WCAG_CONFORMANCE_STANDARD.md)
- [`standards/SEMANTICS_ARIA_STANDARD.md`](standards/SEMANTICS_ARIA_STANDARD.md)
- [`standards/KEYBOARD_FOCUS_STANDARD.md`](standards/KEYBOARD_FOCUS_STANDARD.md)
- [`standards/CONTENT_FORMS_ERRORS_STANDARD.md`](standards/CONTENT_FORMS_ERRORS_STANDARD.md)
- [`standards/VISUAL_MOTION_MEDIA_STANDARD.md`](standards/VISUAL_MOTION_MEDIA_STANDARD.md)
- [`standards/TESTING_STANDARD.md`](standards/TESTING_STANDARD.md)
- [`standards/REMEDIATION_STANDARD.md`](standards/REMEDIATION_STANDARD.md)
- [`standards/COMPLETION_EVIDENCE.md`](standards/COMPLETION_EVIDENCE.md)

The supporting standards extend this file. This `AGENTS.md` takes precedence if wording conflicts.

## Mandatory rules

### ACC-WCAG-001

**Requirement:** Target WCAG 2.2 AA for web interfaces unless a stricter obligation applies.

**Evidence:** Automated and manual accessibility evidence.

### ACC-KEYBOARD-002

**Requirement:** Ensure all interactive behavior is keyboard operable with visible focus.

**Evidence:** Keyboard test.

### ACC-SEMANTICS-003

**Requirement:** Use native semantics first and ARIA only when necessary.

**Evidence:** Markup and screen-reader review.

### ACC-CONTENT-004

**Requirement:** Provide labels, names, instructions, errors, captions, and alternatives.

**Evidence:** Content review.

### ACC-MOTION-005

**Requirement:** Respect reduced-motion preferences and avoid harmful flashing.

**Evidence:** Visual behavior test.

## Non-negotiable behavior

- Inspect existing code, configuration, contracts, tests, documentation, ownership, and operational context before changing anything.
- Do not invent production values, identities, endpoints, schemas, credentials, infrastructure, legal obligations, or compatibility promises.
- Classify risk and identify trust boundaries, sensitive data, state changes, and reversibility.
- Default to safe, narrow, reversible behavior and stop when prerequisites or target identity are ambiguous.
- Do not weaken tests, security, privacy, accessibility, approvals, or evidence requirements to make work appear complete.
- Preserve public behavior unless change is explicitly authorized and migration or compatibility work is included.
- Keep examples fictitious and keep secrets and sensitive data out of source, tests, logs, errors, artifacts, and documentation.
- Record exact commands, results, limitations, assumptions, exceptions, and remaining risk.

## Required working method

1. Determine whether this discipline applies and document the reason.
2. Inspect the current implementation, contracts, evidence, and ownership.
3. Identify risk, trust boundaries, dependencies, failure modes, and affected users or operators.
4. Define acceptance criteria and required evidence before implementation.
5. Make the smallest coherent change.
6. Add or update tests, documentation, runbooks, contracts, diagrams, and evidence as applicable.
7. Run package-specific validation and review the final diff for unrelated or unsafe changes.
8. Report what changed, what was verified, what was not verified, and what risk remains.

## Completion gate

Do not report this discipline complete until:

- applicable mandatory rules are satisfied
- supporting standards were considered
- required evidence is recorded
- checks not run are identified
- limitations, assumptions, exceptions, and remaining risks are stated

## References

- [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
