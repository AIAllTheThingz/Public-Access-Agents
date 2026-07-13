---
id: SCHEMA-VERSION-001
title: Schema Versioning Policy
version: 0.2.0
status: baseline
---

# Schema Versioning Policy

## Version model

Schema contracts use semantic versioning principles:

- **Patch:** descriptions, examples, annotations, and validator fixes that do not change accepted instances.
- **Minor:** backward-compatible additions, such as optional properties or broader accepted values.
- **Major:** required-field changes, removed properties, narrowed enums, stricter formats, changed meanings, or any change that invalidates previously valid instances.

## Paths

- Rolling paths may advance within the compatibility policy.
- Versioned paths remain immutable within a major version except for non-semantic annotation corrections.
- A new major version receives a new directory such as `v2/`.

## Instance version

Instances may include:

```json
"schemaVersion": "1.0.0"
```

Version 1 instances may omit the property for backward compatibility.

## Release requirements

A schema release must identify:

- changed contracts
- compatibility class
- affected consumers
- migration steps
- positive and negative tests
- validator version
- unresolved limitations
- approval for breaking changes

## Deprecation

Deprecated fields or versions require:

- replacement guidance
- supported overlap period
- removal target
- consumer inventory
- migration evidence
- explicit status

Silently changing a field's meaning while preserving its name is not compatibility. It is an ambush with excellent syntax.
