---
id: SCHEMA-INDEX-001
title: Schema Contracts
version: 0.3.0
status: baseline
---

# Schema Contracts

## Purpose

This directory defines the repository's machine-readable contracts for standards composition, risk, exceptions, testing, artifacts, and completion evidence.

Schemas make records structurally testable. They do not prove that the record is truthful, complete, authorized, secure, compliant, or tied to the correct artifact. A beautifully valid lie remains a lie, merely one with matching braces.

## Current dialect and implementation baseline

The schemas use JSON Schema Draft 2020-12.

The repository validator uses Python and the `jsonschema` package. The pinned validation dependency is documented under [`tools/validate-schemas/`](../tools/validate-schemas/).

Official references:

- [JSON Schema specification](https://json-schema.org/specification)
- [Draft 2020-12 meta-schema](https://json-schema.org/draft/2020-12/schema)
- [Python jsonschema documentation](https://python-jsonschema.readthedocs.io/)

## Schema catalog

| Schema | Purpose | Common repository instances |
|---|---|---|
| [`artifact-record.schema.json`](artifact-record.schema.json) | Identify an artifact, source revision, digest, provenance, and signing state. | `artifact-record*.json` |
| [`completion-result.schema.json`](completion-result.schema.json) | Record completion state, validation, limitations, risk, and review. | `completion-result*.json` |
| [`exception-record.schema.json`](exception-record.schema.json) | Record time-bounded standards exceptions and compensating controls. | `exception-record*.json` |
| [`project-manifest.schema.json`](project-manifest.schema.json) | Declare profile and package composition for a project. | `project-manifest.json` |
| [`risk-classification.schema.json`](risk-classification.schema.json) | Record risk level, rationale, factors, reviewers, and rollback need. | `risk-classification*.json` |
| [`test-evidence.schema.json`](test-evidence.schema.json) | Record exact validation commands, results, environment, and limitations. | `test-evidence*.json` |

See [`SCHEMA_CATALOG.md`](SCHEMA_CATALOG.md) for field-level ownership and instance discovery.

## Stable paths and versioned paths

Two paths are provided for each contract:

- `schemas/<name>.schema.json` is the rolling convenience entry point.
- `schemas/v1/<name>.schema.json` is the backward-compatible major-version 1 contract.

Long-lived automation should use the major-version path. Consumers requiring an exact immutable contract must also pin a repository tag or commit. The rolling path may advance according to the compatibility policy.

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

The optional `schemaVersion` property may be set to `1.0.0` or `1.1.0` for project manifests and to `1.0.0` for the other version 1 contracts. Project-manifest version `1.1.0` adds optional `virtualization`, `operatingSystems`, and `networking` arrays; using any of those arrays requires the instance to declare `1.1.0`. Legacy instances without `schemaVersion` are interpreted as version `1.0.0`.

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
