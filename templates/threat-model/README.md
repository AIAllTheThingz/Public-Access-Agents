---
id: TEMPLATE-PKG-THREAT-MODEL-001
title: Threat Model Template Package
version: 0.2.0
status: baseline
---

# Threat Model Template Package

## Purpose

Document assets, actors, entry points, trust boundaries, abuse cases, mitigations, evidence, and residual risk for a defined system or change.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- new trust boundaries, public interfaces, privileged actions, sensitive data, tenant boundaries, or AI tools are introduced
- a high-risk change needs adversarial analysis
- security mitigations and residual risk need accountable review

## This template does not replace

- architecture documentation
- a vulnerability scan
- penetration testing
- risk acceptance or production approval

## Package contents

```text
templates/threat-model/
├── THREAT_MODEL_TEMPLATE.md
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.md
```

- [`THREAT_MODEL_TEMPLATE.md`](THREAT_MODEL_TEMPLATE.md) is the stable template entry point.
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
| `{{MODEL_ID}}` | Stable threat-model identifier. |
| `{{SYSTEM_SCOPE}}` | System, change, or boundary covered. |
| `{{ARCHITECTURE_REFERENCE}}` | Architecture document or diagram reference. |
| `{{ASSETS}}` | Assets requiring protection. |
| `{{ACTORS_TRUST_LEVELS}}` | Human, service, tenant, and attacker roles. |
| `{{ENTRY_POINTS}}` | Interfaces and ingestion paths. |
| `{{TRUST_BOUNDARIES}}` | Authorization and data-flow boundaries. |
| `{{SENSITIVE_DATA_FLOWS}}` | Sensitive data origins, transformations, and destinations. |
| `{{ABUSE_CASE_ROWS}}` | Structured abuse-case table rows. |
| `{{ASSUMPTIONS}}` | Assumptions that materially affect analysis. |
| `{{OUT_OF_SCOPE}}` | Explicit exclusions with ownership. |
| `{{FOLLOW_UP}}` | Required remediation, testing, or review actions. |
| `{{OWNER}}` | Accountable model owner. |
| `{{REVIEWERS}}` | Required reviewers. |
| `{{REVIEW_DATE}}` | Review date. |
| `{{REVISIT_TRIGGERS}}` | Conditions requiring update. |

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

- scope and architecture are current
- actors include untrusted and compromised cases
- trust boundaries are concrete
- abuse cases include evidence and residual risk
- out-of-scope items have owners

## Common failure modes

- listing generic threats with no system-specific path
- assuming authenticated actors are trusted
- omitting outbound and administrative paths
- marking mitigations complete without evidence
- never revisiting the model after architecture changes

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
- [THREAT_MODELING_POLICY.md](../../governance/THREAT_MODELING_POLICY.md)
- [README.md](../../disciplines/application-security/README.md)

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
