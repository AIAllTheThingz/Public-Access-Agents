---
id: TEMPLATE-PKG-ARTIFACT-RECORD-001
title: Artifact Record Template Package
version: 0.2.0
status: baseline
---

# Artifact Record Template Package

## Purpose

Identify an artifact, immutable digest, source revision, build run, provenance, signing state, creation time, and limitations in schema-compatible JSON.

Status: **baseline**

This package provides a reusable starting structure. It does not supply project facts, authority, evidence, or approval.

## Use this template when

- publishing or reviewing a release artifact
- linking completion evidence to an immutable output
- recording provenance and signature verification

## This template does not replace

- the artifact itself
- a software bill of materials
- provenance or signature payloads
- release approval

## Package contents

```text
templates/artifact-record/
├── ARTIFACT_RECORD_TEMPLATE.json
├── README.md
├── REVIEW_CHECKLIST.md
└── examples/
    └── EXAMPLE.json
```

- [`ARTIFACT_RECORD_TEMPLATE.json`](ARTIFACT_RECORD_TEMPLATE.json) is the stable template entry point.
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
| `{{ARTIFACT_NAME}}` | Human-readable artifact name. |
| `{{ARTIFACT_TYPE}}` | Artifact kind such as archive, package, image, or executable. |
| `{{DIGEST}}` | Algorithm-qualified immutable digest. |
| `{{SOURCE_COMMIT}}` | Immutable source revision. |
| `{{BUILD_RUN}}` | Build or CI run identifier. |
| `{{PROVENANCE}}` | Provenance statement or durable location. |
| `{{SIGNED}}` | Boolean true or false. |
| `{{SIGNATURE_EVIDENCE}}` | Signature verification evidence or remove the field. |
| `{{CREATED_AT}}` | RFC 3339 creation timestamp. |
| `{{LIMITATION}}` | Known limitation or remove the array item. |

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

- digest is algorithm-qualified and immutable
- source revision and build run resolve
- provenance is durable
- signed state matches verification evidence
- limitations are explicit
- the instance validates against the versioned schema

## Common failure modes

- using a filename as an artifact identity
- recording a mutable branch rather than a source revision
- claiming signed without verification evidence
- using fictitious or truncated digests
- omitting build provenance

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
- [artifact-record.schema.json](../../schemas/artifact-record.schema.json)
- [README.md](../../disciplines/supply-chain/README.md)

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
