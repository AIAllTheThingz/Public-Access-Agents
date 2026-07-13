---
id: TOOL-PKG-VALIDATE-STANDARDS-001
title: Validate Standards Tool
version: 1.0.0
status: baseline
---

# Validate Standards Tool

## Purpose

Validate repository root files, JSON parsing, unique document IDs, AGENTS.md depth, and final-branch hygiene.

Status: **baseline**

## Stable entry point

[`validate_repository.py`](validate_repository.py)

The stable path is part of the repository tooling contract. Moving or renaming it requires migration guidance and CI updates.

## Operating mode

- Reads: repository files and paths
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
python tools/validate-standards/validate_repository.py --help
```

## Checks and behavior

- required root files
- JSON syntax
- duplicate front-matter IDs
- minimum AGENTS.md depth
- temporary bootstrap and diagnostic artifacts

## Examples

```bash
python tools/validate-standards/validate_repository.py
```

```bash
python tools/validate-standards/validate_repository.py --format json --output reports/structure.json
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
- Sensitive values must not be included in findings.
- A passed result must not be described as proof beyond the implemented checks.
- Wrappers must preserve nonzero exit codes.

## Failure behavior

Input and configuration failures produce status `error`. Validation findings produce status `failed`. Unexpected exceptions produce status `error` and exit code `3`.

Do not catch and discard failures merely to keep CI green. Green output created by suppressing errors is not validation. It is interior decoration.

## Test coverage

Central tests live under [`../tests/`](../tests/).

Run focused tests:

```bash
python -m unittest discover -s tools/tests -p "test_validate_standards*.py"
```

Run the complete suite:

```bash
python tools/validate-all/run_all.py --include-tests
```

## Compatibility

Backward-compatible changes may add optional flags, summary fields, metadata, or new finding codes.

Breaking changes include:

- changing the stable entry path
- changing exit-code meaning
- removing JSON fields
- changing default write or overwrite behavior
- changing generated file semantics
- silently narrowing accepted input

## Limitations

- does not require front matter on every Markdown file
- does not validate semantic correctness
- does not replace schema, template, or link validation

## Review checklist

Reviewers should confirm:

- documented behavior matches code
- positive and negative tests exist
- output and exit codes are stable
- filesystem and subprocess handling are safe
- dependency changes are pinned and justified
- compatibility impact is documented
- the complete pipeline passes

## Maintenance

Update the script, README, manifest, examples, tests, catalog, and CI together when behavior changes.

## Completion boundary

A successful execution establishes only the outcome of this tool's implemented checks or generation plan against the identified input. It does not grant authority, certify compliance, or prove production readiness.
