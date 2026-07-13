---
id: TOOL-TEMPLATE-VALIDATE-001
title: Template Validation Tool
version: 0.2.0
status: baseline
---

# Template Validation Tool

## Purpose

Validates the reusable template library, including:

- required collection and package files
- stable legacy template paths
- unique Markdown document identifiers
- minimum README depth
- approved placeholder syntax
- placeholder documentation
- placeholder-free examples
- JSON template parsing
- schema-backed JSON example validation
- review checklist decision sections
- secret-like values in examples

## Install

The validator uses the schema package's pinned dependency:

```bash
python -m pip install -r tools/validate-schemas/requirements.txt
```

## Run

```bash
python tools/validate-templates/validate_templates.py
```

## Exit behavior

- `0`: structural template validation passed
- `1`: one or more template violations were found

## Boundary

The validator proves structure and contract alignment. It does not prove that an adopted record contains true facts, valid authority, genuine evidence, sound risk, or an acceptable decision.
