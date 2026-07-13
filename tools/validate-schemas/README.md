---
id: TOOL-SCHEMA-VALIDATE-001
title: Schema Validation Tool
version: 0.2.0
status: baseline
---

# Schema Validation Tool

## Purpose

Validates:

- Draft 2020-12 schema syntax
- rolling and versioned schema equivalence
- positive examples
- negative examples
- repository instances discovered by filename
- date and date-time formats

## Install

```bash
python -m pip install -r tools/validate-schemas/requirements.txt
```

## Run

```bash
python tools/validate-schemas/validate_schemas.py
```

## Dependency

The tool pins `jsonschema[format]` to a reviewed version so CI and local validation use the same implementation.

## Boundary

The tool validates structure. It does not establish truth, authorization, security, compliance, or production readiness.
