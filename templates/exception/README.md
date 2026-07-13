---
id: TEMPLATE-PKG-EXCEPTION-001
title: Standards Exception Record Template Package
version: 0.2.0
status: baseline
---

# Standards Exception Record Template Package

## Purpose

Request, review, approve, monitor, expire, and close a time-bounded deviation from a specific standards rule.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- an applicable rule cannot currently be satisfied
- a temporary deviation has a documented business need
- compensating controls and an expiry can be defined
- approval must be separated from implementation

## This template does not replace

- silently marking a rule inapplicable
- permanent policy changes
- risk classification
- production approval

## Package contents

```text
templates/exception/
├── EXCEPTION_RECORD_TEMPLATE.md
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.md
```

- [`EXCEPTION_RECORD_TEMPLATE.md`](EXCEPTION_RECORD_TEMPLATE.md) is the stable template entry point.
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
| `{{EXCEPTION_ID}}` | Stable exception identifier. |
| `{{REQUESTED_BY}}` | Requester identity or role. |
| `{{OWNER}}` | Accountable remediation owner. |
| `{{REQUEST_DATE}}` | ISO 8601 request date. |
| `{{EXPIRATION_DATE}}` | Mandatory expiry date. |
| `{{STATUS}}` | Requested, approved, rejected, expired, or closed. |
| `{{RULE_ID}}` | Exact rule being excepted. |
| `{{BUSINESS_NEED}}` | Why compliance is not currently feasible. |
| `{{RISK_STATEMENT}}` | Risk introduced by the deviation. |
| `{{RISK_LEVEL}}` | Normalized low, moderate, high, or critical level. |
| `{{COMPENSATING_CONTROLS}}` | Controls reducing likelihood or impact. |
| `{{SCOPE}}` | Systems, versions, environments, and users covered. |
| `{{MONITORING}}` | Validation, monitoring, and review cadence. |
| `{{REMEDIATION_PLAN}}` | Steps and owner to remove the exception. |
| `{{APPROVER}}` | Authorized human approver. |
| `{{APPROVAL_DATE}}` | Approval date or `not-approved`. |
| `{{CLOSURE_EVIDENCE}}` | Evidence when closed or `not-closed`. |

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

- rule ID and scope are precise
- exception is genuinely time-bounded
- compensating controls are testable
- approver is independent and authorized
- remediation and closure evidence are defined

## Common failure modes

- using exceptions as permanent policy
- requester approving their own exception
- missing expiry or remediation owner
- vague compensating controls
- allowing expired exceptions to continue silently

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
- [EXCEPTION_PROCESS.md](../../governance/EXCEPTION_PROCESS.md)
- [exception-record.schema.json](../../schemas/exception-record.schema.json)

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
