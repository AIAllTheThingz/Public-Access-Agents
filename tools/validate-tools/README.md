---
id: TOOL-PKG-VALIDATE-TOOLS-001
title: Validate Tools Tool
version: 1.2.0
status: baseline
---

# Validate Tools Tool

## Purpose

Validate tool package structure, stable entry points, Python compilation, contracts, documentation, and unit-test coverage.

Status: **baseline**

## Stable entry point

[`validate_tools.py`](validate_tools.py)

The stable path is part of the repository tooling contract. Moving or renaming it requires migration guidance, release classification, and CI updates.

## Operating mode

- Reads: the tools collection and tests
- Writes: only an optional result file
- Network: none
- Default behavior: safe and non-destructive

## Common options

```text
--root PATH
--format text|json
--output PATH
--quiet
--help
```

Tool-specific options are shown by:

```bash
python tools/validate-tools/validate_tools.py --help
```

## Tool packages checked

The validator requires these packages:

- `validate-standards`
- `check-links`
- `validate-skills`
- `validate-schemas`
- `validate-templates`
- `validate-tools`
- `generate-manifest`
- `compose-agents`
- `validate-all`
- `release`

The release package contains both `validate_release.py` and `build_release.py`. Every Python entry point in a package is compiled, not merely the primary validator path.

## Checks and behavior

- required tools collection documents
- package README, manifest, examples, and primary entry point
- unique front-matter IDs
- README depth
- planned-tool remnants
- Python compilation for package entry points
- test-module count
- JSON result contract
- release-package presence

## Examples

```bash
python tools/validate-tools/validate_tools.py
```

```bash
python tools/validate-tools/validate_tools.py --run-unit-tests
```

## Text and JSON results

Text output is for interactive use. JSON output conforms to [`../contracts/tool-result.schema.json`](../contracts/tool-result.schema.json).

Finding codes are intended for automation. Message wording may improve, but a finding code must not silently change meaning.

## Exit codes

- `0`: completed and passed
- `1`: completed with validation failures
- `2`: invalid input, missing configuration, or dependency issue
- `3`: unexpected internal failure

## Safety requirements

- Repository paths are resolved from `--root`.
- The tool does not fetch external content.
- Compilation checks must not execute the target scripts.
- Sensitive values must not be included in findings.
- A passed result must not be described as proof beyond the implemented checks.
- Wrappers must preserve nonzero exit codes.

## Failure behavior

Input and configuration failures produce status `error`. Validation findings produce status `failed`. Unexpected exceptions produce status `error` and exit code `3`.

Do not catch and discard failures merely to keep CI green. Green output created by suppressing errors is not validation. It is interior decoration.

## Test coverage

Central tests live under [`../tests/`](../tests/).

The repository requires at least one test module per declared tool package. The release package is covered by `test_release.py`.

Run focused tests:

```bash
python -m unittest discover -s tools/tests -p "test_validate_tools*.py"
```

Run the complete suite:

```bash
python tools/validate-all/run_all.py --include-tests
```

## Compatibility

Backward-compatible changes may add optional flags, summary fields, metadata, package checks, or new finding codes.

Breaking changes include:

- changing the stable entry path
- changing exit-code meaning
- removing JSON fields
- removing a required package without migration
- changing how executable entry points are identified
- changing default write or overwrite behavior
- changing generated file semantics
- silently narrowing accepted input

Changes to the required package set must be classified under [`../../RELEASE_POLICY.md`](../../RELEASE_POLICY.md).

## Limitations

- compilation is not runtime correctness
- unit tests run only when requested
- package presence does not prove every secondary script is fully exercised
- does not inspect third-party package vulnerabilities
- does not verify private GitHub workflow permissions or rulesets

## Review checklist

Reviewers should confirm:

- documented behavior matches code
- the declared package list is complete
- release scripts are compiled and tested
- positive and negative tests exist
- output and exit codes are stable
- filesystem and subprocess handling are safe
- dependency changes are pinned and justified
- compatibility and release impact are documented
- the complete pipeline passes

## Maintenance

Update the script, README, manifest, examples, tests, catalog, changelog, release notes, and CI together when behavior changes.

## Completion boundary

A successful execution establishes only that the declared tool package structure and compilation checks passed. It does not prove runtime correctness, release authority, compliance, or production readiness.
