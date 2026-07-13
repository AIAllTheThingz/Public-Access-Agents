- currently invalid instances that could pass
- code generators and strongly typed consumers
- validation libraries and supported drafts
- stored historical records
- CI, release, governance, and audit dependencies
- external consumers not visible in this repository

## Compatibility promise

The version 1 contracts preserve the repository's existing required fields and current valid instances.

The optional `schemaVersion` and `extensions` properties are backward-compatible additions.

## Validation versus compatibility

A schema can pass meta-validation and still introduce a breaking consumer change. The meta-schema checks schema syntax and dialect rules. It does not know what your consumers built around last Tuesday's interpretation.
"""), encoding='utf-8')

(root/'schemas'/'EXTENSION_POLICY.md').write_text(md("SCHEMA-EXT-001","Schema Extension Policy", """
## Default rule

Top-level schema objects remain closed with `additionalProperties: false`.

Custom fields must be placed under the optional `extensions` object.

## Extension keys

Use namespaced keys such as:

```json
{
  "extensions": {
    "example.org.ticketId": "CHG-1234",
    "example.org.ownerTeam": "platform-engineering"
  }
}
```

Do not use vague keys such as `custom`, `misc`, or `extraData`.

## Prohibited extensions

Extensions must not:

- redefine a standard field
- weaken a required control
- hide validation failure
- contain secrets or unrestricted sensitive data
- impersonate approval or evidence
- change the meaning of the standard status, risk, or result fields
- create an undocumented second contract

## Promoting an extension

Promote an extension to a standard property only when:

- multiple consumers need it
- ownership and meaning are stable
- compatibility is analyzed
- examples and migration guidance exist
- a schema version decision is recorded
"""), encoding='utf-8')

(root/'schemas'/'MIGRATION_GUIDE.md').write_text(md("SCHEMA-MIGRATE-001","Schema Migration Guide", """
## Migration from the original baseline

The original six rolling filenames remain available.

Version 1 adds:

- versioned copies under `schemas/v1/`
- descriptions and stronger non-empty constraints
- optional `schemaVersion`
- optional namespaced `extensions`
- additional optional evidence metadata
- executable positive and negative validation
- format checking for dates and date-times

Current valid repository instances remain valid.

## Recommended consumer migration

1. Inventory every producer and consumer.
2. Pin the appropriate `schemas/v1/` path.
3. Install or configure a Draft 2020-12 validator.
4. Enable format checking.
5. Validate stored representative records.
6. Add `schemaVersion: "1.0.0"` to newly produced records.
7. Move non-standard fields under `extensions`.
8. Record failures and correct producers rather than weakening the contract.
9. Add contract tests to CI.
10. Retain the schema version with archived evidence.

## Rolling-path consumers

Consumers using `schemas/<name>.schema.json` should migrate to `schemas/v1/<name>.schema.json` before relying on stable long-term behavior.

## Identifier note

Schema `$id` values now use repository-backed canonical URLs. Consumers that cached the former placeholder completion-result identifier should update their registry mapping and record the migration.
"""), encoding='utf-8')

(root/'schemas'/'VALIDATION_GUIDE.md').write_text(md("SCHEMA-VALIDATE-001","Schema Validation Guide", """
## Install

```bash
python -m pip install -r tools/validate-schemas/requirements.txt
```

## Run

```bash
python tools/validate-schemas/validate_schemas.py
```

## Validation layers

1. JSON parsing
2. Draft 2020-12 meta-schema validation
3. rolling-versus-versioned equivalence
4. positive example validation
5. negative example rejection
6. repository instance discovery and validation
7. date and date-time format checking

## Error interpretation

Validation output identifies:

- instance file
- schema file
