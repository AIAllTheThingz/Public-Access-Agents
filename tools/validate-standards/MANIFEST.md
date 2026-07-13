---
id: TOOL-PKG-VALIDATE-STANDARDS-001-MANIFEST
title: Validate Standards Tool Manifest
version: 1.0.0
status: baseline
---

# Validate Standards Tool Manifest

## Required files

- `validate_repository.py`
- `README.md`
- `MANIFEST.md`
- `examples/README.md`

## Shared contracts

- `../TOOL_CONTRACT.md`
- `../contracts/tool-result.schema.json`
- `../tests/`

## Acceptance checks

- entry point compiles
- `--help` exits successfully
- text output is readable
- JSON output conforms to the result contract
- exit codes match the common contract
- positive and negative tests pass
- stable path remains unchanged
- documentation and examples match behavior
