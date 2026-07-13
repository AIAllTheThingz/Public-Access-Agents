---
id: TEMPLATE-PLACEHOLDER-001
title: Template Placeholder Conventions
version: 0.2.0
status: baseline
---

# Template Placeholder Conventions

## Syntax

The only supported placeholder syntax is:

```text
{{UPPER_SNAKE_CASE}}
```

Valid examples:

- `{{PROJECT_NAME}}`
- `{{RISK_LEVEL}}`
- `{{VALIDATION_COMMANDS}}`

Invalid examples:

- `{PROJECT_NAME}`
- `<<PROJECT_NAME>>`
- `{{projectName}}`
- `{{ PROJECT_NAME }}`
- `TBD`
- `<fill this in>`

## Naming rules

Placeholder names must:

- start with an uppercase letter
- contain only uppercase letters, digits, and underscores
- describe one stable concept
- avoid implementation-specific abbreviations unless widely understood
- remain consistent across packages where meaning is identical

## Documentation

Every placeholder must appear in the package README's placeholder inventory.

The inventory must explain:

- meaning
- expected source
- expected type or format when relevant
- whether an optional property or list item may be removed

## JSON templates

JSON templates must remain syntactically valid JSON.

Some placeholder values represent non-string types. After replacement:

- booleans must become `true` or `false`
- integers must be unquoted integers
- arrays must contain valid typed values
- optional properties or items should be removed when inapplicable

JSON templates are scaffolds. Completed examples prove the final typed shape.

## Examples

Examples must not contain placeholder tokens.

## Adopted records

Adopted records must not contain:

- approved placeholder syntax
- `TBD`
- `<TODO>`
- instructional filler
- template-only warning text

Unknown facts must be resolved or explicitly recorded as unresolved with an owner. They must not be disguised as completed content.
