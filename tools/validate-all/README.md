---
id: TOOL-PKG-VALIDATE-ALL-001
title: Validate All Tool
version: 1.1.0
status: baseline
---

# Validate All Tool

## Purpose

Run the complete repository validation pipeline in a stable order and aggregate structured results.

Status: **baseline**

## Stable entry point

[`run_all.py`](run_all.py)

The stable path is part of the repository tooling contract. Moving or renaming it requires migration guidance, release classification, and CI updates.

## Operating mode

- Reads: validator entry points and repository content
- Writes: only an optional aggregate result file
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
python tools/validate-all/run_all.py --help
```

## Validators

The runner executes:

1. `validate-standards`
2. `check-links`
3. `validate-schemas`
4. `validate-templates`
5. `validate-tools`
6. `validate-release`
7. unit tests when `--include-tests` is supplied

Release validation checks the repository version, changelog, release notes, migration notes, release and maturity policies, tag workflow, and optional tag matching.

## Checks and behavior

- validator discovery
- JSON result parsing
- exit-code propagation
- aggregate status
- repository release-contract validation
- optional unit tests
- optional fail-fast behavior

## Examples

```bash
python tools/validate-all/run_all.py
```

```bash
python tools/validate-all/run_all.py --include-tests --format json --output reports/validation.json
```

Run only release validation through the aggregator:

```bash
python tools/validate-all/run_all.py \
  --tool validate-release \
  --format json
```

List validators:

```bash
python tools/validate-all/run_all.py --list
```

## Text and JSON results

Text output is for interactive use. JSON output conforms to [`../contracts/tool-result.schema.json`](../contracts/tool-result.schema.json).

Each child validator result is retained in aggregate metadata with its exit code. Child failures are not converted into wrapper success.

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
- The runner does not build artifacts, create tags, or publish releases.

## Failure behavior

Input and configuration failures produce status `error`. Validation findings produce status `failed`. Unexpected exceptions produce status `error` and exit code `3`.

Do not catch and discard failures merely to keep CI green. Green output created by suppressing errors is not validation. It is interior decoration.

## Permanent CI

The permanent repository workflow runs:

```bash
python tools/validate-all/run_all.py --include-tests
```

Tool order remains in this Python entry point rather than being duplicated in workflow YAML.

The tag-driven release workflow runs the same complete pipeline before validating the tag and building release artifacts.

## Test coverage

Central tests live under [`../tests/`](../tests/).

Run focused tests:

```bash
python -m unittest discover -s tools/tests -p "test_validate_all*.py"
```

Release-specific tests are under:

```text
tools/tests/test_release.py
```

Run the complete suite:

```bash
python tools/validate-all/run_all.py --include-tests
```

## Compatibility

Backward-compatible changes may add optional flags, summary fields, metadata, validators, or new finding codes.

Adding a validator is normally backward-compatible but may expose repository defects that previously escaped automated checks. The release impact must still be classified.

Breaking changes include:

- changing the stable entry path
- changing exit-code meaning
- removing JSON fields
- changing validator ordering in a way that changes observable contract behavior
- silently removing a validator from the complete pipeline
- changing default test inclusion behavior
- silently narrowing accepted input

## Limitations

- does not replace tool-specific diagnostics
- captures only bounded subprocess output
- cannot prove checks omitted by underlying validators
- validates release files but does not verify private GitHub repository settings
- does not create tags or prove release authority
- cannot establish semantic correctness from structural success

## Review checklist

Reviewers should confirm:

- documented behavior matches code
- the validator list is complete
- release validation remains in the permanent pipeline
- positive and negative tests exist
- output and exit codes are stable
- filesystem and subprocess handling are safe
- dependency changes are pinned and justified
- compatibility and release impact are documented
- the complete pipeline passes

## Maintenance

Update the script, README, manifest, examples, tests, catalog, release notes, and CI together when behavior changes.

## Completion boundary

A successful execution establishes only the outcome of the implemented child checks against the identified input. It does not grant authority, certify compliance, publish a release, promote package maturity, or prove production readiness.
