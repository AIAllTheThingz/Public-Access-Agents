---
id: TOOL-PKG-GENERATE-MANIFEST-001-MANIFEST
title: Generate Manifest Tool Manifest
version: 1.0.0
status: baseline
---

# Generate Manifest Tool Manifest

## Required files

- `generate_manifest.py`
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
