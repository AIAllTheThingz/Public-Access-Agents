---
id: TEMPLATE-PKG-RELEASE-001
title: Release Plan Template Package
version: 0.2.0
status: baseline
---

# Release Plan Template Package

## Purpose

Define artifact identity, scope, prerequisites, migration order, rollout stages, validation, stop criteria, communication, rollback, and post-release monitoring.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- a release changes production behavior, dependencies, data, interfaces, or operations
- multiple deployment stages or owners must coordinate
- rollback and post-release observation must be planned before execution

## This template does not replace

- change authorization
- production-readiness approval
- a recovery runbook
- the release artifact record

## Package contents

```text
templates/release/
├── RELEASE_PLAN_TEMPLATE.md
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.md
```

- [`RELEASE_PLAN_TEMPLATE.md`](RELEASE_PLAN_TEMPLATE.md) is the stable template entry point.
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
| `{{RELEASE_ID}}` | Stable release identifier. |
| `{{RELEASE_SCOPE}}` | Features, fixes, and excluded work. |
| `{{ARTIFACTS}}` | Immutable artifacts and digests. |
| `{{TARGETS}}` | Environments, systems, regions, or tenants. |
| `{{PREREQUISITES}}` | Required approvals, backups, capacity, and dependencies. |
| `{{MIGRATION_ORDER}}` | Ordered data, API, infrastructure, and application steps. |
| `{{ROLLOUT_STAGES}}` | Canary, phased, blue-green, or other rollout stages. |
| `{{VALIDATION}}` | Pre-, during-, and post-release checks. |
| `{{STOP_CRITERIA}}` | Observable conditions that halt rollout. |
| `{{ROLLBACK}}` | Rollback, roll-forward, restore, or compensation. |
| `{{MONITORING}}` | Post-release signals, owners, and observation window. |
| `{{COMMUNICATION}}` | Stakeholders, notices, and escalation. |
| `{{OWNERS}}` | Release, technical, operational, and business owners. |
| `{{APPROVAL}}` | Release approval record. |

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

- artifacts are immutable
- migration and rollback order are compatible
- stop criteria are measurable
- monitoring and observation window have owners
- communications and escalation are ready

## Common failure modes

- deploying a different artifact than the reviewed one
- planning rollout without rollback prerequisites
- using vague stop criteria such as 'if things look bad'
- ending the release at command completion
- omitting data and dependency ordering

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
- [README.md](../../disciplines/release-engineering/README.md)
- [PRODUCTION_READINESS.md](../../governance/PRODUCTION_READINESS.md)

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
