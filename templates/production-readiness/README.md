---
id: TEMPLATE-PKG-PRODUCTION-READINESS-001
title: Production Readiness Review Template Package
version: 0.2.0
status: baseline
---

# Production Readiness Review Template Package

## Purpose

Evaluate whether a system or change is operationally ready for production, including ownership, security, data, reliability, observability, recovery, capacity, support, and approval.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- introducing a new production service or material capability
- performing a high-risk production change
- promoting a system from implementation completion to operational acceptance

## This template does not replace

- implementation completion
- risk assessment
- change authorization
- ongoing operational ownership

## Package contents

```text
templates/production-readiness/
├── PRODUCTION_READINESS_TEMPLATE.md
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.md
```

- [`PRODUCTION_READINESS_TEMPLATE.md`](PRODUCTION_READINESS_TEMPLATE.md) is the stable template entry point.
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
| `{{REVIEW_ID}}` | Stable readiness review identifier. |
| `{{SYSTEM}}` | System or change under review. |
| `{{TARGET_ENVIRONMENT}}` | Production environment or class. |
| `{{OWNERS}}` | Application, platform, security, data, and operations owners. |
| `{{RISK_REFERENCE}}` | Risk assessment reference. |
| `{{ARCHITECTURE_REFERENCE}}` | Architecture and trust-boundary reference. |
| `{{SECURITY_PRIVACY}}` | Security and privacy readiness evidence. |
| `{{RELIABILITY_CAPACITY}}` | Availability, capacity, quotas, and scaling evidence. |
| `{{OBSERVABILITY}}` | Logs, metrics, traces, alerts, dashboards, and ownership. |
| `{{RECOVERY}}` | Backup, restore, rollback, failover, and recovery evidence. |
| `{{OPERATIONS_SUPPORT}}` | Runbooks, support model, escalation, and maintenance. |
| `{{RELEASE_ROLLOUT}}` | Release, migration, rollout, and stop criteria. |
| `{{OPEN_RISKS}}` | Open risks and exceptions. |
| `{{DECISION}}` | Ready, ready-with-conditions, not-ready, or deferred. |
| `{{APPROVERS}}` | Authorized production approvers. |

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

- implementation and production readiness are separated
- operational owners accept responsibility
- recovery is tested rather than assumed
- observability reaches owned destinations
- open risks and conditions are explicit

## Common failure modes

- declaring ready because deployment succeeded
- listing backups without restore evidence
- assigning ownership to generic team names with no acceptance
- omitting cost, capacity, quota, and support
- approving with unknown rollback behavior

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
