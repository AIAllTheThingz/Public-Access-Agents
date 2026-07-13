---
id: TEMPLATE-AGENT-001
title: Template Library Agent Instructions
version: 0.2.0
status: baseline
---

# Template Library Agent Instructions

## Purpose

These instructions govern changes to the reusable template library, its examples, validation tooling, and root documentation.

Templates are public interfaces. Stable paths, placeholder names, section meaning, schemas, and examples may be consumed by humans or automation.

## Scope

These instructions apply to:

- `templates/`
- `tools/validate-templates/`
- root catalog and manifest sections describing templates
- permanent CI steps that validate templates

## Precedence

1. Applicable legal, contractual, safety, and security obligations
2. Explicit authorized requirements
3. Root repository `AGENTS.md`
4. Governance standards
5. These template instructions
6. More-specific package instructions
7. Repository conventions

Local template changes may strengthen requirements. They may not weaken governance, evidence, authorization, or review controls.

## Required behavior

- Preserve stable template paths unless migration is approved.
- Treat placeholder names as compatibility-sensitive interfaces.
- Use only `{{UPPER_SNAKE_CASE}}` placeholders.
- Document every placeholder in the package README.
- Keep examples completed and placeholder-free.
- Keep public examples fictitious and free of secrets or sensitive evidence.
- Distinguish requester, implementer, reviewer, approver, operator, and risk owner.
- Distinguish implementation, validation, review, authorization, approval, operational verification, and closure.
- Do not use templates to imply compliance or production readiness.
- Keep JSON templates parseable and document required type conversion.
- Align JSON examples with versioned schemas.
- Update template, README, checklist, and example together.
- Run repository, link, schema, and template validation.
- State compatibility and migration impact.
- Record checks not run.

## Required working method

1. Inspect the current template package, consumers, schemas, governance references, and validator.
2. Identify the record or decision the template controls.
3. Classify compatibility impact.
4. Make the smallest coherent package change.
5. Update placeholders and their documentation together.
6. Update the completed example.
7. Update review and completion criteria.
8. Run all validators.
9. Review for secret-like values, ambiguous authority, and unresolved placeholders.
10. Obtain accountable review.

## Prohibited behavior

- Do not add real credentials, tokens, keys, endpoints, incidents, or personal data.
- Do not leave examples with unresolved placeholders.
- Do not add vague placeholders such as `{{MISC}}` or `{{DETAILS}}`.
- Do not silently rename placeholders.
- Do not turn optional fields into mandatory governance without review.
- Do not let a template authorize its own use.
- Do not conflate review with approval.
- Do not suppress validation failures.
- Do not claim that structural completion proves semantic correctness.

## Completion gate

Template work is incomplete until:

- stable paths exist
- package README is useful
- placeholders are valid and documented
- examples are complete
- checklist matches the template
- compatibility is assessed
- validation passes
- no sensitive value is present
- limitations and checks not run are disclosed
