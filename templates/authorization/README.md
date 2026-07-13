---
id: TEMPLATE-PKG-AUTHORIZATION-001
title: Change Authorization Record Template Package
version: 0.2.0
status: baseline
---

# Change Authorization Record Template Package

## Purpose

Record who may perform a consequential change, against which targets, during what window, with which controls, stop criteria, validation, and recovery expectations.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- a change is privileged, destructive, bulk, production-affecting, or otherwise consequential
- automation needs explicit target and action boundaries
- authorization must be separated from implementation and review

## This template does not replace

- risk classification
- technical review
- production-readiness review
- credentials or access grants

## Package contents

```text
templates/authorization/
├── CHANGE_AUTHORIZATION_TEMPLATE.md
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.md
```

- [`CHANGE_AUTHORIZATION_TEMPLATE.md`](CHANGE_AUTHORIZATION_TEMPLATE.md) is the stable template entry point.
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
| `{{AUTHORIZATION_ID}}` | Stable authorization identifier. |
| `{{REQUESTER}}` | Requester identity or role. |
| `{{IMPLEMENTER}}` | Authorized implementer identity or role. |
| `{{APPROVER}}` | Accountable human approver. |
| `{{APPROVAL_DATE}}` | Approval date. |
| `{{VALID_FROM}}` | Authorization start time. |
| `{{VALID_UNTIL}}` | Authorization end time. |
| `{{TARGET_SCOPE}}` | Exact systems, environments, records, or resources. |
| `{{ALLOWED_ACTIONS}}` | Explicit allowed actions. |
| `{{PROHIBITED_ACTIONS}}` | Explicit prohibited actions. |
| `{{PRECONDITIONS}}` | Conditions required before execution. |
| `{{STOP_CRITERIA}}` | Conditions requiring immediate halt. |
| `{{VALIDATION}}` | Required pre- and post-change validation. |
| `{{RECOVERY}}` | Rollback, restore, compensation, or escalation. |
| `{{EVIDENCE}}` | Required audit and completion evidence. |

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

- target scope and actions are exact
- time window is bounded
- approver has authority and is not the implementer where separation is required
- stop criteria are observable
- recovery and evidence are defined

## Common failure modes

- authorizing a broad class of future changes
- using credentials as proof of authorization
- omitting prohibited actions
- allowing the implementer to self-approve high-risk work
- leaving authorization open-ended

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
- [HUMAN_REVIEW_POLICY.md](../../governance/HUMAN_REVIEW_POLICY.md)
- [RISK_CLASSIFICATION.md](../../governance/RISK_CLASSIFICATION.md)

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
