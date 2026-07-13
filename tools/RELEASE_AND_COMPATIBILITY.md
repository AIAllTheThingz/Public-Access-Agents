---
id: TOOL-COMPAT-001
title: Tool Release and Compatibility
version: 1.0.0
status: baseline
---

# Tool Release and Compatibility

## Versioning

Tools use semantic versioning principles.

- Patch: bug fix without contract change
- Minor: backward-compatible option, field, or finding addition
- Major: path, exit-code, required-field, generated-output, or behavior break

## Stable interfaces

- executable paths
- common options
- exit-code meanings
- JSON result fields
- finding-code meanings
- generated file names and semantic roles

## Deprecation

A deprecated option or path requires:

- warning period
- replacement guidance
- removal target
- consumer inventory
- migration tests

## CI compatibility

Permanent CI should invoke `validate-all` rather than duplicating tool order in YAML. Tool-specific jobs may supplement but not silently replace the complete pipeline.

## Release evidence

Record changed tools, tests, compatibility class, migration guidance, validation results, and checks not run.
