---
id: SCHEMA-EX-PROJECT-MANIFEST-001
title: Project Standards Manifest Examples
version: 0.3.0
status: baseline
---

# Project Standards Manifest Examples

## Positive example

[`valid.example.json`](valid.example.json) must validate against:

- [`../../project-manifest.schema.json`](../../project-manifest.schema.json)
- [`../../v1/project-manifest.schema.json`](../../v1/project-manifest.schema.json)

## Negative example

[`invalid.example.json`](invalid.example.json) is intentionally invalid and must be rejected.

It demonstrates the version boundary: project-manifest `1.0.0` cannot declare the virtualization, operating-system, or networking arrays introduced by `1.1.0`.

## Boundary

The positive `1.1.0` example demonstrates all three new package arrays and structural conformance only. It does not represent a production record, authorized decision, genuine artifact, executed command, or accepted risk.
