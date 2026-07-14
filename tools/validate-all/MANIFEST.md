---
id: TOOL-PKG-VALIDATE-ALL-001-MANIFEST
title: Validate All Tool Manifest
version: 1.2.0
status: baseline
---

# Validate All Tool Manifest

## Required files

- `run_all.py`
- `README.md`
- `MANIFEST.md`
- `examples/README.md`

## Shared contracts

- `../TOOL_CONTRACT.md`
- `../contracts/tool-result.schema.json`
- `../tests/`
- `../../RELEASE_POLICY.md`

## Required validators

- `validate-standards`
- `check-links`
- `validate-skills`
- `validate-schemas`
- `validate-templates`
- `validate-tools`
- `validate-release`

## Acceptance checks

- entry point compiles
- `--help` exits successfully
- `--list` includes every required validator
- text output is readable
- JSON output conforms to the result contract
- child results and exit codes are preserved
- release validation remains in the complete pipeline
- exit codes match the common contract
- positive and negative tests pass
- stable path remains unchanged
- documentation and examples match behavior
- permanent CI invokes this runner with unit tests
