---
id: TEMPLATE-PKG-PROJECT-MANIFEST-001
title: Project Standards Manifest Template Package
version: 0.3.0
status: baseline
---

# Project Standards Manifest Template Package

## Purpose

Declare the project's selected profile, languages, disciplines, frameworks, platforms, virtualization systems, operating systems, networking systems, risk, exceptions, ownership, and evidence location in machine-readable form.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- adopting this standards repository into a project
- automating package-selection validation
- recording a stable composition contract for CI and review

## This template does not replace

- the selected standards themselves
- project-specific `AGENTS.md` files
- risk assessment or production approval
- architecture and ownership records

## Package contents

```text
templates/project-manifest/
├── PROJECT_MANIFEST_TEMPLATE.json
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.json
```

- [`PROJECT_MANIFEST_TEMPLATE.json`](PROJECT_MANIFEST_TEMPLATE.json) is the stable template entry point.
- [`REVIEW_CHECKLIST.md`](REVIEW_CHECKLIST.md) supports accountable review.
- [`examples/EXAMPLE.json`](examples/EXAMPLE.json) demonstrates a completed fictitious record.

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
| `{{PROJECT_NAME}}` | Stable project name. |
| `{{PRIMARY_PROFILE}}` | Canonical profile identifier. |
| `{{SECONDARY_PROFILE}}` | Secondary profile identifier or remove the array item. |
| `{{LANGUAGE_PACKAGE}}` | Language package slug. |
| `{{DISCIPLINE_PACKAGE}}` | Discipline package slug. |
| `{{PLATFORM_PACKAGE}}` | Platform package slug or remove the array item. |
| `{{FRAMEWORK_PACKAGE}}` | Framework package slug or remove the array item. |
| `{{VIRTUALIZATION_PACKAGE}}` | Virtualization package slug or remove the array item. |
| `{{OPERATING_SYSTEM_PACKAGE}}` | Operating-system package slug or remove the array item. |
| `{{NETWORKING_PACKAGE}}` | Networking package slug or remove the array item. |
| `{{RISK_LEVEL}}` | Low, moderate, high, or critical. |
| `{{EXCEPTION_ID}}` | Exception record identifier or remove the array item. |
| `{{OWNER_ROLE}}` | Accountable owner role. |
| `{{EVIDENCE_LOCATION}}` | Repository-relative evidence location. |

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

- profile and language, discipline, framework, platform, virtualization, operating-system, and networking package slugs exist
- selected packages match actual project shape
- risk is backed by an assessment
- exception identifiers resolve
- owners and evidence locations are real
- the instance validates against the versioned schema

## Common failure modes

- treating the manifest as a package installer
- listing aspirational packages that are not actually adopted
- omitting a material hypervisor, operating-system, or network control boundary from the composition record
- omitting secondary profiles for distinct project shapes
- using the rolling schema in long-lived automation
- leaving template placeholders in committed JSON

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
- [README.md](../../profiles/README.md)
- [project-manifest.schema.json](../../schemas/project-manifest.schema.json)

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
