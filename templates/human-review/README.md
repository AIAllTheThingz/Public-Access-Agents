---
id: TEMPLATE-PKG-HUMAN-REVIEW-001
title: Human Review Record Template Package
version: 0.2.0
status: baseline
---

# Human Review Record Template Package

## Purpose

Record accountable human review scope, evidence examined, findings, required changes, decision, authority, and limitations.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- governance requires human review
- AI-generated or high-risk work needs accountable assessment
- a reviewer decision must be traceable independently from comments

## This template does not replace

- automated validation
- change authorization unless the reviewer is also an authorized approver
- production-readiness approval
- evidence that was not actually examined

## Package contents

```text
templates/human-review/
├── HUMAN_REVIEW_TEMPLATE.md
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.md
```

- [`HUMAN_REVIEW_TEMPLATE.md`](HUMAN_REVIEW_TEMPLATE.md) is the stable template entry point.
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
| `{{REVIEW_ID}}` | Stable review identifier. |
| `{{WORK_ID}}` | Change, pull request, artifact, or task reviewed. |
| `{{REVIEWER}}` | Human reviewer identity or role. |
| `{{REVIEWER_AUTHORITY}}` | Authority or responsibility supporting the review. |
| `{{REVIEW_DATE}}` | Review date. |
| `{{REVIEW_SCOPE}}` | Files, systems, evidence, and decisions reviewed. |
| `{{EVIDENCE_EXAMINED}}` | Evidence actually examined. |
| `{{FINDINGS}}` | Findings and severity. |
| `{{REQUIRED_CHANGES}}` | Required corrections or `none`. |
| `{{DECISION}}` | Approved, approved-with-conditions, changes-required, or rejected. |
| `{{CONDITIONS}}` | Conditions attached to the decision. |
| `{{LIMITATIONS}}` | Items not reviewed or unresolved. |
| `{{FOLLOW_UP}}` | Owners and dates for follow-up. |

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

- reviewer is human and accountable
- scope and evidence examined are explicit
- decision vocabulary is clear
- conditions and limitations are recorded
- review is not misrepresented as authorization

## Common failure modes

- recording a name without what was reviewed
- using CI success as human review
- approving with unresolved critical findings
- hiding not-reviewed areas
- claiming authority the reviewer does not hold

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
- [AI_GENERATED_CODE_POLICY.md](../../governance/AI_GENERATED_CODE_POLICY.md)

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
