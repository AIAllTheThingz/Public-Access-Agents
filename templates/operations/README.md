---
id: TEMPLATE-PKG-OPERATIONS-001
title: Operational Runbook Template Package
version: 0.2.0
status: baseline
---

# Operational Runbook Template Package

## Purpose

Provide an operator-safe procedure for observing, diagnosing, changing, recovering, and escalating a supported system.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- operators need repeatable service procedures
- a system has alerts, scheduled maintenance, recovery, or manual interventions
- support responsibilities cross teams or time zones

## This template does not replace

- architecture documentation
- change authorization
- incident command policy
- automation that should replace unsafe repetitive manual work

## Package contents

```text
templates/operations/
├── RUNBOOK_TEMPLATE.md
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.md
```

- [`RUNBOOK_TEMPLATE.md`](RUNBOOK_TEMPLATE.md) is the stable template entry point.
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
| `{{RUNBOOK_ID}}` | Stable runbook identifier. |
| `{{SYSTEM}}` | Supported system or capability. |
| `{{PURPOSE}}` | Operational outcome and boundaries. |
| `{{OWNERS}}` | Primary and secondary owners. |
| `{{SUPPORT_HOURS}}` | Support window and escalation expectations. |
| `{{PREREQUISITES}}` | Access, tools, safety checks, and dependencies. |
| `{{HEALTH_SIGNALS}}` | Dashboards, alerts, logs, and expected state. |
| `{{DIAGNOSTIC_STEPS}}` | Ordered read-only diagnostic steps. |
| `{{CHANGE_PROCEDURES}}` | Authorized state-changing procedures. |
| `{{RECOVERY_PROCEDURES}}` | Rollback, restore, restart, failover, or escalation. |
| `{{STOP_CRITERIA}}` | Conditions requiring halt. |
| `{{ESCALATION}}` | Contacts, roles, severity, and handoff. |
| `{{EVIDENCE}}` | Logs and records required for completion. |
| `{{VALIDATION}}` | How operators verify the desired state. |
| `{{REVIEW_DATE}}` | Next review date. |

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

- diagnostics precede state-changing actions
- commands identify target and expected output
- privileged actions reference authorization
- stop and escalation criteria are explicit
- runbook ownership and review date are current

## Common failure modes

- embedding credentials
- using screenshots without commands or expected results
- placing destructive steps before diagnosis
- assuming every environment is identical
- leaving stale contacts and commands unreviewed

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
- [README.md](../../disciplines/sre/README.md)
- [README.md](../../disciplines/observability/README.md)

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
