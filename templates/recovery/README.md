---
id: TEMPLATE-PKG-RECOVERY-001
title: Rollback and Recovery Plan Template Package
version: 0.2.0
status: baseline
---

# Rollback and Recovery Plan Template Package

## Purpose

Define failure scenarios, recovery objectives, rollback or restore methods, prerequisites, authority, validation, stop conditions, and evidence.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- a change can cause service, data, configuration, or infrastructure failure
- rollback is not a single command
- restore, failover, compensation, or recreation may be required

## This template does not replace

- tested backups
- incident response
- release authorization
- a general disaster-recovery program

## Package contents

```text
templates/recovery/
├── ROLLBACK_RECOVERY_TEMPLATE.md
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.md
```

- [`ROLLBACK_RECOVERY_TEMPLATE.md`](ROLLBACK_RECOVERY_TEMPLATE.md) is the stable template entry point.
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
| `{{PLAN_ID}}` | Stable recovery-plan identifier. |
| `{{SCOPE}}` | Systems, data, configurations, and environments covered. |
| `{{FAILURE_SCENARIOS}}` | Failures the plan addresses. |
| `{{RECOVERY_OBJECTIVES}}` | RTO, RPO, data-loss, and service objectives. |
| `{{PREREQUISITES}}` | Backups, snapshots, tools, access, and dependencies. |
| `{{TRIGGER_CRITERIA}}` | Conditions invoking recovery. |
| `{{AUTHORITY}}` | Who may initiate and stop recovery. |
| `{{ROLLBACK_STEPS}}` | Ordered rollback or reversal steps. |
| `{{RESTORE_STEPS}}` | Ordered restore, failover, compensation, or recreation steps. |
| `{{VALIDATION}}` | Functional, data, security, and operational validation. |
| `{{STOP_ESCALATE}}` | Conditions requiring halt or escalation. |
| `{{COMMUNICATION}}` | Stakeholders and incident communication. |
| `{{EVIDENCE}}` | Required logs, timestamps, artifacts, and decisions. |
| `{{TEST_HISTORY}}` | Most recent rehearsal and results. |

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

- failure scenarios match actual architecture
- recovery objectives are measurable
- prerequisites exist before the change
- authority and escalation are explicit
- the plan has been rehearsed at appropriate risk

## Common failure modes

- calling redeployment a rollback when data changed
- assuming backups restore
- omitting identity, network, or key dependencies
- having no authority to invoke the plan
- testing only the happy path

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
- [PRODUCTION_READINESS.md](../../governance/PRODUCTION_READINESS.md)
- [README.md](../../disciplines/sre/README.md)

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
