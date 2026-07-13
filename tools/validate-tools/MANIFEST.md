---
id: TOOL-PKG-VALIDATE-TOOLS-001-MANIFEST
title: Validate Tools Tool Manifest
version: 1.1.0
status: baseline
---

# Validate Tools Tool Manifest

## Required files

- `validate_tools.py`
- `README.md`
- `MANIFEST.md`
- `examples/README.md`

## Shared contracts

- `../TOOL_CONTRACT.md`
- `../contracts/tool-result.schema.json`
- `../tests/`
- `../../RELEASE_POLICY.md`

## Required package checks

- nine declared executable tool packages
- release validator and deterministic release builder
- all package Python entry points compile
- at least one test module per declared package

## Acceptance checks

- entry point compiles
- `--help` exits successfully
- text output is readable
- JSON output conforms to the result contract
- exit codes match the common contract
- positive and negative tests pass
- release package is present and documented
- release scripts compile
- stable path remains unchanged
- documentation and examples match behavior
