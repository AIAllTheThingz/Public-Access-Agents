---
id: MATURITY-REVIEW-TEMPLATE-001
title: Component Maturity Review Template
version: 0.9.0
status: baseline
---

# Component Maturity Review

## Review identity

- Review ID: `{{REVIEW_ID}}`
- Component: `{{COMPONENT}}`
- Component version: `{{COMPONENT_VERSION}}`
- Repository commit: `{{REPOSITORY_COMMIT}}`
- Current maturity: `{{CURRENT_MATURITY}}`
- Proposed maturity: `{{PROPOSED_MATURITY}}`
- Owner: `{{OWNER}}`
- Reviewers: `{{REVIEWERS}}`
- Review date: `{{REVIEW_DATE}}`

## Scope and applicability

{{SCOPE_AND_APPLICABILITY}}

## Normative quality

{{NORMATIVE_QUALITY}}

## Adoption evidence

{{ADOPTION_EVIDENCE}}

Include at least one package-level adoption test and two representative adoptions, pilots, or independently reviewed composition exercises for baseline-to-stable promotion.

## Compatibility inventory

{{COMPATIBILITY_INVENTORY}}

Identify stable paths, rule identifiers, schema contracts, templates, tool behavior, generated output, and release impact.

## Validation evidence

{{VALIDATION_EVIDENCE}}

Record exact commands, environments, results, checks not run, and limitations.

## Source currency

- Authoritative sources reviewed: {{AUTHORITATIVE_SOURCES}}
- Last source review date: `{{SOURCE_REVIEW_DATE}}`
- Known provider or runtime lifecycle concerns: {{LIFECYCLE_CONCERNS}}

## Security and operational review

{{SECURITY_OPERATIONAL_REVIEW}}

## Open findings and conditions

{{OPEN_FINDINGS}}

## Decision

`{{DECISION}}`

Allowed values:

- approved
- approved-with-conditions
- deferred
- rejected

## Rationale

{{RATIONALE}}

## Conditions and owners

{{CONDITIONS}}

## Next review

- Next review date or trigger: `{{NEXT_REVIEW}}`
- Responsible owner: {{NEXT_REVIEW_OWNER}}

## Release linkage

- Target repository release: `{{TARGET_RELEASE}}`
- Release-note entry: {{RELEASE_NOTE_REFERENCE}}

A maturity decision applies only to the reviewed component version and repository revision. It does not certify adopting projects.
