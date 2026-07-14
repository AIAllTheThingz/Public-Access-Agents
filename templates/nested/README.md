---
id: TEMPLATE-PKG-NESTED-001
title: Nested Agent Instructions Template Package
version: 0.2.0
status: baseline
---

# Nested Agent Instructions Template Package

## Purpose

Define stricter, scope-specific instructions for a directory whose responsibilities, risks, tooling, or validation differ from the repository root.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- a directory has a distinct language, framework, platform, virtualization, operating-system, networking, or responsibility boundary
- local work requires stricter validation or review
- generated, migration, infrastructure, security, data, or deployment files need specialized controls
- local owners and evidence differ from the repository root

## This template does not replace

- the root `AGENTS.md`
- parent governance or selected shared standards
- a waiver or exception record
- authorization for privileged or destructive actions

## Package contents

```text
templates/nested/
├── AGENTS_TEMPLATE.md
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.md
```

- [`AGENTS_TEMPLATE.md`](AGENTS_TEMPLATE.md) is the stable template entry point.
- [`REVIEW_CHECKLIST.md`](REVIEW_CHECKLIST.md) supports accountable review.
- [`examples/EXAMPLE.md`](examples/EXAMPLE.md) demonstrates a completed fictitious record.

## Required inputs

Before copying the template, identify:

- the document or record owner
- the decision, system, project, change, or artifact in scope
- authoritative project facts
- applicable governance and standards
- risk and authorization requirements
- evidence sources
- reviewers and approvers
- retention and review dates
- any schema or automation consumer

Do not populate unknown fields with plausible guesses. Record them as unresolved and stop where the missing fact affects authority, risk, or correctness.

## Placeholder inventory

Only the following placeholders are valid in this template:

| Placeholder | Required meaning |
|---|---|
| `{{SCOPE_NAME}}` | Human-readable name for the local scope. |
| `{{SCOPE_PATH}}` | Repository-relative directory covered by the instructions. |
| `{{SCOPE_RESPONSIBILITIES}}` | Files, behaviors, and ownership controlled here. |
| `{{LOCAL_OWNERS}}` | Accountable roles or teams for the scope. |
| `{{ADDITIONAL_REQUIREMENTS}}` | Requirements stricter or more specific than parent instructions. |
| `{{PROHIBITED_LOCAL_ACTIONS}}` | Actions forbidden in this scope. |
| `{{LOCAL_VALIDATION_COMMANDS}}` | Exact validation commands for this scope. |
| `{{LOCAL_EVIDENCE}}` | Evidence records or locations required for completion. |
| `{{ESCALATION_PATH}}` | Role or process used when local instructions conflict or are insufficient. |

Placeholders use the exact `{{UPPER_SNAKE_CASE}}` form. Replace every token before adoption.

For optional JSON fields, remove the property or array item when it is genuinely inapplicable. Do not replace typed JSON fields with quoted prose and then declare the schema unreasonable for noticing.

## Adoption workflow

1. Read the [template collection guide](../README.md).
2. Confirm this is the correct template type.
3. Copy the complete template file to the adopting repository.
4. Replace all placeholders using reviewed project facts.
5. Remove instructional notes that should not remain in the adopted record.
6. Remove genuinely inapplicable optional sections only with justification.
7. Preserve sections required by governance, schemas, or selected standards.
8. Link related architecture, risk, evidence, authorization, and review records.
9. Run repository and template validation.
10. Obtain accountable review.
11. Record the adopted document's owner and next review trigger.

## Completion criteria

The adopted record is complete only when:

- every placeholder is replaced
- scope and ownership are explicit
- required facts are traceable
- applicable evidence is linked
- decisions use defined vocabulary
- optional omissions are justified
- review and approval roles are not conflated
- no secret, credential, private key, or sensitive production evidence is embedded
- validation passes
- limitations and unresolved risk are visible

## Review focus

- scope boundaries are precise
- parent rules remain explicitly applicable
- local requirements only strengthen or specialize controls
- validation is local and executable
- ownership and escalation are named

## Common failure modes

- copying root instructions into every directory
- using nested instructions to bypass shared standards
- declaring a scope broader than the directory actually controls
- leaving local validation blank
- creating contradictory requirements without escalation

## Validation

From the standards repository root:

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
python tools/validate-templates/validate_templates.py
```

Copied JSON records should also be validated against the applicable versioned schema where one exists.

## Example boundary

The example is fictitious. It demonstrates structure and completion expectations only. It does not represent authorization, production readiness, a genuine artifact, an executed command, or accepted risk.

## Related guidance

- [README.md](../README.md)
- [ORGANIZATION_CONTRACT.md](../../governance/ORGANIZATION_CONTRACT.md)

## Maintenance

Changes to this package must:

- preserve the stable template path unless migration is approved
- update the README, checklist, example, and template together
- preserve placeholder names unless a migration is documented
- classify compatibility for downstream users
- run template and link validation
- state checks not run
- avoid silently turning optional fields into mandatory policy

## Completion boundary

Adopting this template does not prove the resulting decision, review, evidence, authorization, release, recovery, or instruction file is correct. Completion requires real facts, validation, evidence, and accountable human judgment.
