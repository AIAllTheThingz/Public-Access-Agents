---
id: SCHEMA-DESIGN-001
title: Schema Design Rules
version: 0.2.0
status: baseline
---

# Schema Design Rules

## Required design rules

- Use Draft 2020-12 explicitly.
- Give every schema a stable `$id`.
- Use clear titles and descriptions.
- Keep property meaning narrow and documented.
- Prefer explicit required fields.
- Keep top-level records closed.
- Provide a namespaced extension object where customization is expected.
- Use enums only when the vocabulary is genuinely controlled.
- Use `minLength`, `minItems`, and `uniqueItems` where empty or duplicate values are not meaningful.
- Use `format` only with validation tooling that enables format checking.
- Avoid defaults that consumers may apply inconsistently.
- Avoid clever conditional schemas when a clearer versioned contract is possible.
- Keep examples free of secrets and production facts.
- Preserve readable deterministic formatting.

## Review questions

- What valid instances become invalid?
- What invalid instances become valid?
- Is a field's meaning changing?
- Can every consumer handle the change?
- Does the schema accidentally encode organization-specific policy?
- Are historical records still valid?
- Is the extension point being abused as an ungoverned data swamp?
- Does the validator actually exercise every intended format and reference?
