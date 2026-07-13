---
id: TEMPLATE-EX-NESTED-001
title: Nested Agent Instructions Example
version: 0.2.0
status: baseline
---

# Nested Agent Instructions Example

## Example purpose

This fictitious nested instruction file governs `src/export/`.

## Scope

- Scope name: Export adapters
- Directory: `src/export`
- Responsibilities: CSV and JSON serialization, output-path validation, and redaction.
- Local owners: reporting maintainers

## Parent instructions

All root instructions remain applicable.

## Additional requirements

- Escape formula-leading CSV cells.
- Preserve documented column order.
- Redact fields classified as confidential.
- Reject output paths outside the configured report directory.

## Prohibited local actions

- Do not add network calls.
- Do not write credentials or raw secrets.
- Do not change public columns without compatibility review.

## Required validation

```bash
python -m pytest tests/export
python -m ruff check src/export tests/export
```

## Local evidence

Store export test reports under `docs/evidence/export/`.

## Boundary

The example does not weaken root rules or authorize production writes.
