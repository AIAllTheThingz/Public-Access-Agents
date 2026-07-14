---
id: TEMPLATE-PKG-ROOT-001
title: Root Agent Instructions Template Package
version: 0.3.0
status: baseline
---

# Root Agent Instructions Template Package

## Purpose

Define repository-wide facts, selected standards, authority boundaries, working methods, validation, evidence, and prohibited behavior for coding agents.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- creating or replacing the root `AGENTS.md` in an adopting repository
- establishing project-wide facts and non-negotiable controls
- declaring selected profiles, languages, disciplines, frameworks, platforms, virtualization systems, operating systems, and networking systems
- defining the project's completion and evidence model

## This template does not replace

- root governance and organization policy
- actual architecture and risk decisions
- nested instructions for materially different local scopes
- human authorization for privileged or production-affecting actions

## Package contents

```text
templates/root/
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
| `{{PROJECT_NAME}}` | Stable project or repository name. |
| `{{PROJECT_PURPOSE}}` | Concise statement of the project outcome and intended users. |
| `{{PROJECT_NON_GOALS}}` | Explicitly excluded outcomes or responsibilities. |
| `{{PRIMARY_PROFILE}}` | Canonical primary profile identifier or path. |
| `{{SECONDARY_PROFILES}}` | Secondary profiles or `none`. |
| `{{LANGUAGE_PACKAGES}}` | Selected language package paths. |
| `{{DISCIPLINE_PACKAGES}}` | Selected discipline package paths. |
| `{{FRAMEWORK_PACKAGES}}` | Selected framework package paths or `none`. |
| `{{PLATFORM_PACKAGES}}` | Selected platform package paths or `none`. |
| `{{VIRTUALIZATION_PACKAGES}}` | Selected virtualization package paths or `none`. |
| `{{OPERATING_SYSTEM_PACKAGES}}` | Selected operating-system package paths or `none`. |
| `{{NETWORKING_PACKAGES}}` | Selected networking package paths or `none`. |
| `{{SUPPORTED_RUNTIMES}}` | Supported runtime, SDK, or interpreter versions. |
| `{{DEPLOYMENT_ENVIRONMENTS}}` | Named environment classes without secrets or internal credentials. |
| `{{SENSITIVE_DATA}}` | Data classifications and handling boundaries. |
| `{{PRIVILEGED_OPERATIONS}}` | Operations requiring explicit authorization and stronger evidence. |
| `{{COMPATIBILITY_COMMITMENTS}}` | Supported APIs, formats, platforms, or migration promises. |
| `{{REQUIRED_REVIEWERS}}` | Roles required for accountable review. |
| `{{VALIDATION_COMMANDS}}` | Exact repository validation commands. |
| `{{EVIDENCE_LOCATION}}` | Where completion and review evidence is stored. |

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

- project facts are specific and not invented
- selected package paths match the repository manifest
- authority and prohibited actions are explicit
- validation commands are executable
- completion requires evidence rather than assertion
- nested scopes are identified where responsibility changes

## Common failure modes

- copying the template without replacing project facts
- listing packages that do not exist or omitting material packages
- allowing nested instructions to weaken parent governance
- using vague phrases such as 'test appropriately' instead of commands
- treating an agent instruction file as production approval

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
- [README.md](../../governance/README.md)
- [README.md](../../profiles/README.md)

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
