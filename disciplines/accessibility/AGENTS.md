---
id: DISC-ACC
title: Accessibility Agent Standard
version: 0.1.0
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

Integrates accessibility into design, implementation, content, and testing.

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

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.

## References

- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/ARIA/apg/
