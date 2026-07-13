---
id: SCHEMA-MIGRATE-001
title: Schema Migration Guide
version: 0.2.0
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
