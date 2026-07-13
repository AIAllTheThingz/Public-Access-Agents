---
id: TEMPLATE-PKG-COMPLETION-001
title: Completion Report Template Package
version: 0.2.0
status: baseline
---

# Completion Report Template Package

## Purpose

Report implemented scope, changed files, risk, validation, evidence, limitations, operational impact, recovery, and accountable review.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- closing an implementation or documentation change
- summarizing evidence for review
- distinguishing implemented, validated, partially validated, and not completed work
- recording checks not run and residual risk

## This template does not replace

- raw test output
- production-readiness approval
- risk classification
- change authorization

## Package contents

```text
templates/completion/
├── COMPLETION_REPORT_TEMPLATE.md
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.md
```

- [`COMPLETION_REPORT_TEMPLATE.md`](COMPLETION_REPORT_TEMPLATE.md) is the stable template entry point.
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
| `{{WORK_ID}}` | Issue, pull request, change, or task identifier. |
| `{{COMPLETION_STATUS}}` | Implemented, validated, partially validated, or not completed. |
| `{{SCOPE}}` | Authorized and completed scope. |
| `{{CHANGE_SUMMARY}}` | What changed and why. |
| `{{FILES_CHANGED}}` | Files or artifacts changed. |
| `{{RISK_CLASSIFICATION}}` | Risk level and assessment reference. |
| `{{SECURITY_IMPACT}}` | Security and privacy impact. |
| `{{COMPATIBILITY_IMPACT}}` | Compatibility and migration impact. |
| `{{VALIDATION_ROWS}}` | Command, result, environment, and evidence rows. |
| `{{VALIDATION_NOT_PERFORMED}}` | Checks not run with reasons. |
| `{{OPERATIONAL_IMPACT}}` | Deployment, operations, monitoring, and support impact. |
| `{{ROLLBACK_RECOVERY}}` | Rollback, restore, or recovery plan and evidence. |
| `{{LIMITATIONS}}` | Known limitations and remaining risks. |
| `{{ARTIFACT_IDENTIFIERS}}` | Commits, digests, tags, or release identifiers. |
| `{{HUMAN_REVIEW}}` | Reviewers, decisions, and dates. |

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

- scope matches authorization
- validation rows contain exact commands and evidence
- not-run checks are explicit
- artifact identifiers are immutable where possible
- limitations and residual risk are honest

## Common failure modes

- claiming complete when only implementation finished
- reporting a command without its result or environment
- omitting failed or not-run checks
- confusing deployment success with operational verification
- using reviewer names as proof of approval without a decision record

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
- [COMPLETION_EVIDENCE.md](../../governance/COMPLETION_EVIDENCE.md)
- [completion-result.schema.json](../../schemas/completion-result.schema.json)

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
