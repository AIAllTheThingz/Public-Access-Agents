---
id: SCHEMA-MIGRATE-001
title: Schema Migration Guide
version: 0.3.0
status: baseline
---

# Schema Migration Guide

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
2. Use the appropriate `schemas/v1/` major-version path and pin a repository tag or commit when exact immutability is required.
3. Install or configure a Draft 2020-12 validator.
4. Enable format checking.
5. Validate stored representative records.
6. Add the current supported `schemaVersion` to newly produced records (`1.1.0` for project manifests using infrastructure package arrays; otherwise `1.0.0`).
7. Move non-standard fields under `extensions`.
8. Record failures and correct producers rather than weakening the contract.
9. Add contract tests to CI.
10. Retain the schema version with archived evidence.

## Rolling-path consumers

Consumers using `schemas/<name>.schema.json` should migrate to `schemas/v1/<name>.schema.json` for major-version compatibility. Consumers requiring an exact immutable artifact should resolve that path from a pinned repository tag or commit.

## Project manifest 1.1

Project-manifest version `1.1.0` adds three optional standard package arrays:

- `virtualization`
- `operatingSystems`
- `networking`

Version `1.0.0` manifests remain valid and require no migration when these package classes are not selected. The schema requires `schemaVersion: "1.1.0"` whenever any new array is present. Producers must verify each slug against the corresponding repository package directory and update composition consumers to include the selected package entry points.

The repository's `generate-manifest` and `compose-agents` tools version `1.1.0` implement these selections. Consumers pinned to an earlier tool version must upgrade before relying on the new fields.

## Identifier note

Schema `$id` values now use repository-backed canonical URLs. Consumers that cached the former placeholder completion-result identifier should update their registry mapping and record the migration.
