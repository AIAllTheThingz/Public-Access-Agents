---
id: TEMPLATE-PKG-ARCHITECTURE-DECISION-001
title: Architecture Decision Record Template Package
version: 0.2.0
status: baseline
---

# Architecture Decision Record Template Package

## Purpose

Record a consequential architecture decision, its context, considered alternatives, impacts, evidence, ownership, and revisit triggers.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- a decision changes system boundaries, dependencies, interfaces, data, deployment, or operations
- multiple viable options exist and future maintainers need the rationale
- compatibility, migration, security, privacy, or recovery impact is material
- a decision should be reviewed independently from its implementation

## This template does not replace

- implementation design details that belong in code or lower-level documentation
- a threat model when abuse paths are material
- a risk acceptance or standards exception
- production-readiness approval

## Package contents

```text
templates/architecture-decision/
├── ADR_TEMPLATE.md
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.md
```

- [`ADR_TEMPLATE.md`](ADR_TEMPLATE.md) is the stable template entry point.
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
| `{{ADR_NUMBER}}` | Stable sequential or project-approved ADR identifier. |
| `{{DECISION_TITLE}}` | Short decision title. |
| `{{DECISION_STATUS}}` | Proposed, accepted, superseded, deprecated, or rejected. |
| `{{DECISION_DATE}}` | Decision date in ISO 8601 form. |
| `{{OWNERS}}` | Accountable decision owners. |
| `{{REVIEWERS}}` | Required reviewers. |
| `{{CONTEXT}}` | Problem, constraints, and current state. |
| `{{DECISION_DRIVERS}}` | Prioritized forces that influence the choice. |
| `{{CONSIDERED_OPTIONS}}` | Viable options with trade-offs. |
| `{{DECISION}}` | Chosen option and exact boundaries. |
| `{{SECURITY_PRIVACY_IMPACT}}` | Security, privacy, and trust-boundary impact. |
| `{{COMPATIBILITY_MIGRATION_IMPACT}}` | Compatibility, rollout, and migration consequences. |
| `{{OPERATIONAL_IMPACT}}` | Reliability, support, observability, recovery, and cost impact. |
| `{{CONSEQUENCES}}` | Positive, negative, and neutral consequences. |
| `{{VALIDATION}}` | Evidence supporting the decision. |
| `{{REVISIT_TRIGGERS}}` | Conditions requiring re-evaluation. |
| `{{SUPERSEDES}}` | Prior ADR identifiers or `none`. |

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

- options are genuinely viable rather than a fake comparison
- decision boundaries and ownership are explicit
- security, privacy, compatibility, operations, and cost are considered
- evidence supports key assumptions
- revisit triggers are observable

## Common failure modes

- writing the ADR after implementation only to justify a predetermined choice
- omitting rejected options and trade-offs
- recording a technology choice without its operating model
- using vague consequences such as 'more scalable'
- never updating superseded decisions

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
- [README.md](../../disciplines/architecture/README.md)

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
