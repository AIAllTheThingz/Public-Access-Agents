---
id: TEMPLATE-CUSTOM-001
title: Template Customization Policy
version: 0.2.0
status: baseline
---

# Template Customization Policy

## Allowed customization

Adopting repositories may:

- replace placeholders with project facts
- add stricter requirements
- add project-specific sections
- remove genuinely optional sections
- add namespaced schema extensions
- add local decision vocabulary when documented and compatible
- add local examples and validation
- translate explanatory text while preserving semantic meaning

## Required preservation

Preserve:

- governance-required fields
- stable record identity
- scope and ownership
- decision state
- evidence and limitations
- review and approval distinction
- expiry and remediation for exceptions
- recovery and stop criteria for consequential work
- source template and version
- applicable schema contract

## Prohibited customization

Do not:

- remove controls merely because they are inconvenient
- convert mandatory evidence into optional prose
- embed secrets
- allow requester or implementer to self-approve where separation is required
- hide failed or not-run checks
- broaden authorization implicitly
- replace precise vocabulary with ambiguous states
- weaken parent instructions
- treat example values as defaults
- leave placeholders in adopted records

## Omission record

When removing a section, record:

- section removed
- why it is inapplicable
- reviewer
- impact
- revisit trigger

## Organization overlays

Organizations may maintain overlays that add:

- local owner roles
- required systems of record
- retention periods
- approval matrices
- local schema extensions
- additional validation

Overlays must remain separately versioned and must not rewrite the public template silently.
