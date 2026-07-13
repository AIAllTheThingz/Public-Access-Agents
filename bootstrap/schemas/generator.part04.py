See [`SCHEMA_CATALOG.md`](SCHEMA_CATALOG.md) for field-level ownership and instance discovery.

## Stable paths and versioned paths

Two paths are provided for each contract:

- `schemas/<name>.schema.json` is the rolling convenience entry point.
- `schemas/v1/<name>.schema.json` is the version-pinned version 1 contract.

Long-lived automation should pin the versioned path. The rolling path may advance according to the compatibility policy.

The six original filenames remain intact.

## Compatibility objective

Version 1 keeps all fields that were previously required and preserves the current repository examples.

The upgrade adds descriptions, optional metadata, normalized extension points, stronger non-empty constraints, and versioned copies. Existing valid repository instances remain valid.

See:

- [`VERSIONING_POLICY.md`](VERSIONING_POLICY.md)
- [`COMPATIBILITY_POLICY.md`](COMPATIBILITY_POLICY.md)
- [`MIGRATION_GUIDE.md`](MIGRATION_GUIDE.md)

## Extension model

All six schemas remain closed by default with `additionalProperties: false`.

Projects may add organization-specific data only inside the optional `extensions` object. Extension keys must be namespaced and must not redefine standard fields.

The optional `schemaVersion` property may be set to `1.0.0`. Legacy instances without it are interpreted as version 1.0.0.

See [`EXTENSION_POLICY.md`](EXTENSION_POLICY.md).

## Validation

Install the pinned dependency:

```bash
python -m pip install -r tools/validate-schemas/requirements.txt
```

Run all repository schema validation:

```bash
python tools/validate-schemas/validate_schemas.py
```

The validator:

- validates every schema against Draft 2020-12
- verifies rolling and versioned schemas remain equivalent except for identifier metadata
- validates positive examples
- confirms negative examples fail
- discovers and validates repository instances by filename
- enables format checking for dates and date-times
- reports the instance path and failing JSON pointer

See [`VALIDATION_GUIDE.md`](VALIDATION_GUIDE.md).

## Examples

Each schema has:

- one positive example that must validate
- one negative example that must fail
- a README explaining what the example proves and does not prove

Examples are under [`examples/`](examples/).

Negative examples are intentionally invalid. Do not copy them into production unless the production goal is to test whether anyone is awake.

## Required change process

Before changing a schema:

1. Identify affected instances and consumers.
2. Classify the change as compatible, conditionally compatible, or breaking.
3. Update rolling and versioned contracts deliberately.
4. Add or update positive and negative examples.
5. Update migration and compatibility guidance.
6. Run schema meta-validation and instance validation.
7. Review whether formats, enums, required fields, or closed-object behavior changed.
8. Record checks not run and unresolved consumer impact.
9. Obtain accountable review for breaking or evidence-affecting changes.

## Completion boundary

Schema validation proves only that an instance conforms to the selected structural contract under the validator used.

It does not prove:

- the evidence is genuine
- the command actually ran
- the reviewer has authority
- the risk classification is correct
- the artifact digest matches the deployed artifact
- the exception remains acceptable
- the project is production-ready
- a compliance obligation has been satisfied
"""
(root/'schemas'/'README.md').write_text(md("SCHEMA-INDEX-001","Schema Contracts",readme_body), encoding='utf-8')

(root/'schemas'/'AGENTS.md').write_text(md("SCHEMA-AGENT-001","Schema Agent Instructions", """
## Purpose

These instructions govern changes to schema contracts, examples, validation tooling, and schema documentation.

Schema changes can alter public machine-readable contracts. Treat them as API changes rather than tidy JSON edits.

## Scope

These instructions apply to:

- `schemas/*.schema.json`
