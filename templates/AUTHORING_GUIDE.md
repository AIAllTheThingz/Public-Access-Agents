---
id: TEMPLATE-AUTHOR-001
title: Template Authoring Guide
version: 0.2.0
status: baseline
---

# Template Authoring Guide

## Template package requirements

Every package must provide:

- stable template file
- package README
- review checklist
- completed fictitious example
- unique document identifiers
- documented placeholders
- completion criteria
- validation instructions
- related standards and schemas
- lifecycle expectations

## Writing requirements

Template language must be:

- explicit
- project-agnostic
- reviewable
- testable where possible
- clear about roles and states
- clear about optional versus required sections
- free of organization-specific secrets and policy assumptions
- honest about what the document does not prove

## Placeholder design

Good placeholders identify a specific fact:

- `{{RISK_OWNER}}`
- `{{ARTIFACT_DIGEST}}`
- `{{STOP_CRITERIA}}`

Bad placeholders invite arbitrary prose:

- `{{MISC}}`
- `{{OTHER}}`
- `{{DETAILS}}`
- `{{FILL_THIS_IN}}`

Use the same placeholder name for the same concept across packages when semantics are identical.

## Decision vocabulary

Controlled decision fields must list allowed values.

Examples:

- risk: low, moderate, high, critical
- validation: passed, failed, not-run
- review: approved, approved-with-conditions, changes-required, rejected
- readiness: ready, ready-with-conditions, not-ready, deferred

Do not create near-synonyms that force consumers to interpret mood.

## Examples

Examples must:

- contain no placeholders
- use fictitious values
- demonstrate meaningful completion
- include limitations
- avoid real systems, identities, endpoints, or incidents
- avoid claiming approval or readiness
- pass applicable schema validation

## Compatibility

Before changing a stable template:

1. identify consumers
2. classify path, placeholder, section, vocabulary, and schema impact
3. preserve compatibility where practical
4. provide migration guidance for breaking changes
5. update package documentation and example
6. run validation
7. record checks not run

## Anti-patterns

- empty headings with no instruction
- checklists with no decision or owner
- examples that are merely the template with different blanks
- hidden required fields
- ambiguous approval language
- screenshots as the only evidence
- templates that cannot be validated
- copying governance text without linking the authoritative policy
