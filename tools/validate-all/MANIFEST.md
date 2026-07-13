---
id: TOOL-PKG-VALIDATE-ALL-001-MANIFEST
title: Validate All Tool Manifest
version: 1.0.0
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

## Acceptance checks

- entry point compiles
- `--help` exits successfully
- text output is readable
- JSON output conforms to the result contract
- exit codes match the common contract
- positive and negative tests pass
- stable path remains unchanged
- documentation and examples match behavior
