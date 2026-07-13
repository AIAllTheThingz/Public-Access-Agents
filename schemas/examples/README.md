---
id: SCHEMA-EX-INDEX-001
title: Schema Examples
version: 0.2.0
status: baseline
---

# Schema Examples

## Purpose

The examples provide executable contract tests.

Each schema directory contains:

- `valid.example.json`, which must pass
- `invalid.example.json`, which must fail
- a README describing the boundary

## Safety

All values are fictitious. Do not add production credentials, internal endpoints, real incident records, personal data, or confidential vulnerability details.

## Validation

```bash
python tools/validate-schemas/validate_schemas.py
```
