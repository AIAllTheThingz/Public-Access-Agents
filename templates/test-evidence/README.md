---
id: TEMPLATE-PKG-TEST-EVIDENCE-001
title: Test Evidence Record Template Package
version: 0.2.0
status: baseline
---

# Test Evidence Record Template Package

## Purpose

Record an exact validation command, outcome, environment, timing, artifact, evidence, exit code, and limitations in schema-compatible JSON.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- capturing machine-readable validation evidence
- linking CI or local checks to a completion record
- recording explicitly not-run checks with limitations

## This template does not replace

- the test output itself
- a completion report
- security or production approval
- human interpretation of test coverage

## Package contents

```text
templates/test-evidence/
├── TEST_EVIDENCE_TEMPLATE.json
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.json
```

- [`TEST_EVIDENCE_TEMPLATE.json`](TEST_EVIDENCE_TEMPLATE.json) is the stable template entry point.
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
| `{{TEST_TYPE}}` | Stable test or validation category. |
| `{{COMMAND}}` | Exact command or check executed. |
| `{{RESULT}}` | Passed, failed, or not-run. |
| `{{ENVIRONMENT}}` | Environment in which the check ran. |
| `{{STARTED_AT}}` | RFC 3339 start timestamp. |
| `{{COMPLETED_AT}}` | RFC 3339 completion timestamp. |
| `{{EVIDENCE}}` | Log, report, artifact, or durable evidence reference. |
| `{{LIMITATION}}` | Known limitation or remove the array item. |
| `{{ARTIFACT}}` | Commit, digest, tag, or artifact identifier. |
| `{{EXIT_CODE}}` | Integer process exit code. |

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

- command is exact and reproducible
- result matches evidence
- environment and artifact are identified
- timestamps are coherent
- limitations describe coverage gaps
- the instance validates against the versioned schema

## Common failure modes

- recording only a test name with no command
- using passed when the check was skipped
- linking ephemeral evidence that will disappear
- omitting the artifact under test
- treating a successful exit code as proof of complete behavior

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
- [test-evidence.schema.json](../../schemas/test-evidence.schema.json)
- [COMPLETION_EVIDENCE.md](../../governance/COMPLETION_EVIDENCE.md)

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
