---
id: TEMPLATE-VALIDATE-001
title: Template Validation Guide
version: 0.2.0
status: baseline
---

# Template Validation Guide

## Commands

```bash
python -m pip install -r tools/validate-schemas/requirements.txt
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
python tools/validate-schemas/validate_schemas.py
python tools/validate-templates/validate_templates.py
```

## Template validator checks

- required collection files
- expected package inventory
- stable template paths
- Markdown front-matter IDs
- minimum README depth
- review checklist presence
- approved placeholder syntax
- placeholder inventory coverage
- placeholder absence from examples
- JSON parsing
- schema validation for JSON examples
- duplicate IDs
- secret-like content
- unresolved `TBD` or `<TODO>` outside template guidance
- permanent CI integration

## Adoption validation

An adopting repository should additionally check:

- no unresolved placeholders remain
- copied JSON records validate against pinned schemas
- project links resolve
- owners and reviewers exist
- decision vocabulary is valid
- evidence locations are durable
- no template warning text remains
- omitted sections are justified
- records are stored in the approved system of record

## Failure handling

Do not suppress the validator to merge a template change.

Resolve failures by:

- correcting the template
- correcting documentation
- correcting the example
- making a deliberate compatible or breaking change
- documenting migration
- updating validation when the validator is objectively wrong

A green validator proves structure, not judgment. A red validator at least has the courtesy to admit something is wrong.
