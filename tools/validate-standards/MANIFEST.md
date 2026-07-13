---
id: TOOL-PKG-VALIDATE-STANDARDS-001-MANIFEST
title: Validate Standards Tool Manifest
version: 1.1.0
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

## Repository contracts checked

- required root files
- Apache-2.0 license markers
- NOTICE attribution and copyright
- LICENSING.md SPDX and stable-link declarations
- README and CONTRIBUTING license declarations
- JSON syntax
- unique front-matter IDs
- AGENTS.md minimum depth
- final-branch hygiene

## Acceptance checks

- entry point compiles
- `--help` exits successfully
- text output is readable
- JSON output conforms to the result contract
- exit codes match the common contract
- positive and negative tests pass
- missing or invalid licensing files fail validation
- stable path remains unchanged
- documentation and examples match behavior
