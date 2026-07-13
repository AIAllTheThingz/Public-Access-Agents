---
id: TOOL-COMPAT-001
title: Tool Release and Compatibility
version: 1.1.0
status: baseline
---

# Tool Release and Compatibility

## Authority

Repository-wide versioning, deprecation, migration, tags, and GitHub Releases are governed by [`../RELEASE_POLICY.md`](../RELEASE_POLICY.md).

This document specializes that policy for executable tools and generated output.

## Versioning

Tools use semantic versioning principles within the repository release contract.

- Patch: bug fix without public contract change
- Minor: backward-compatible option, field, artifact, validator, or finding addition
- Major: path, exit-code, required-field, generated-output, artifact-format, or behavior break

A tool's own version does not override the repository `VERSION`. Both may need to change when a public tool contract changes.

## Stable interfaces

- executable paths
- common options
- exit-code meanings
- JSON result fields
- finding-code meanings
- generated file names and semantic roles
- default read/write behavior
- dry-run and overwrite behavior
- release artifact names
- release archive root
- checksum format
- release-manifest fields
- tag interpretation

## Compatibility classification

Tool changes must identify whether they are:

- compatible
- conditionally compatible
- breaking
- not applicable

Examples of breaking changes include:

- moving a stable script
- changing exit-code meaning
- removing a JSON result field
- turning a read-only command into a writing command
- removing overwrite protection
- changing generated file semantics
- changing release artifact names or checksum format
- changing accepted tag syntax incompatibly

## Deprecation

A deprecated option or path requires:

- warning period
- replacement guidance
- removal target
- consumer inventory
- migration tests
- changelog and release-note entry

Stable executable paths, JSON result fields, release artifact names, and machine-readable contracts follow the 180-day and two-minor-release window in `RELEASE_POLICY.md` unless an approved security exception applies.

## Release tooling

The release package under `tools/release/` is a public tool contract.

Changes require review of:

- tag-to-version matching
- source commit identity
- tracked-file inclusion
- archive determinism
- artifact names
- checksum generation
- release-manifest structure
- overwrite behavior
- GitHub workflow permissions
- failure and partial-publication handling

## CI compatibility

Permanent CI should invoke `validate-all` rather than duplicating tool order in YAML. Tool-specific jobs may supplement but not silently replace the complete pipeline.

The release workflow must invoke the same complete validation pipeline before artifact creation.

## Migration

Breaking tool changes require:

- versioned release notes
- migration notes
- overlap or deprecation window where feasible
- affected-consumer analysis
- tests for old and new behavior
- independent specialist review

## Release evidence

Record:

- changed tools
- tool and repository versions
- source commit
- tests
- compatibility class
- migration guidance
- validation results
- checks not run
- release artifact names
- SHA-256 digests
- release manifest
- known limitations

## Boundary

Compatibility policy makes changes predictable. It does not guarantee that every consumer uses the documented interface correctly or that a successful release is semantically safe.
