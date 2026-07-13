---
id: TOOL-INDEX-001
title: Validation Tools
version: 0.2.0
status: baseline
---

# Validation Tools

## Purpose

The tools validate repository structure, links, schema contracts, template packages, examples, and machine-readable evidence.

## Commands

Install the pinned schema-validation dependency:

```bash
python -m pip install -r tools/validate-schemas/requirements.txt
```

Run all validators:

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
python tools/validate-schemas/validate_schemas.py
python tools/validate-templates/validate_templates.py
```

## Tool catalog

- [`validate-standards`](validate-standards/) checks repository structure, identifiers, JSON parsing, and required references.
- [`check-links`](check-links/) checks relative Markdown links.
- [`validate-schemas`](validate-schemas/) checks Draft 2020-12 schemas, versioned equivalence, positive and negative examples, formats, and repository instances.
- [`validate-templates`](validate-templates/) checks template packages, stable paths, placeholders, examples, and schema-backed records.
- [`compose-agents`](compose-agents/) documents agent-instruction composition.
- [`generate-manifest`](generate-manifest/) documents manifest generation.

## Boundary

The tools detect structural and contract problems. They do not prove that a standard is secure, a record is truthful, an approver has authority, evidence is genuine, or a project is production-ready.
