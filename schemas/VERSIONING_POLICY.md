---
id: SCHEMA-VERSION-001
title: Schema Versioning Policy
version: 0.3.0
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
- Versioned major paths preserve backward compatibility within that major. They may receive compatible patch or minor additions, but must not receive a breaking change.
- A new major version receives a new directory such as `v2/`.

Consumers that require byte-for-byte immutability must pin a repository tag or commit in addition to the major schema path and record the instance `schemaVersion`.

## Instance version

Instances may include:

```json
"schemaVersion": "1.1.0"
```

Version 1 instances may omit the property for backward compatibility and are then interpreted as `1.0.0`. The project-manifest contract requires `1.1.0` when standard virtualization, operating-system, or networking selections are used.

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
