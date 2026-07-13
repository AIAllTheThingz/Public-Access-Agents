This catalog maps each machine-readable contract to stable paths, versioned paths, expected instances, owners, and compatibility concerns.

| Contract | Rolling path | Versioned path | Purpose |
|---|---|---|---|
{chr(10).join(catalog_rows)}

## Instance discovery

The repository validator maps files by naming convention:

| Instance filename | Schema |
|---|---|
| `project-manifest.json` | project manifest |
| `completion-result*.json` | completion result |
| `test-evidence*.json` | test evidence |
| `artifact-record*.json` | artifact record |
| `exception-record*.json` | exception record |
| `risk-classification*.json` | risk classification |

Files under `schemas/examples/` are handled as explicit positive or negative test cases.

## Ownership

The adopting repository must assign:

- contract owner
- consumer owners
- validator owner
- migration owner for breaking changes
- evidence owner for generated records
- release or automation owner where schemas gate delivery

## Consumer responsibilities

Consumers must:

- pin a versioned schema for durable automation
- reject unknown top-level fields unless an extension policy says otherwise
- retain the original instance used for a decision
- record the validator and schema version
- treat validation failure as a contract problem, not an invitation to disable validation
- avoid assuming that structural validity proves semantic truth
"""), encoding='utf-8')

(root/'schemas'/'VERSIONING_POLICY.md').write_text(md("SCHEMA-VERSION-001","Schema Versioning Policy", """
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
"""), encoding='utf-8')

(root/'schemas'/'COMPATIBILITY_POLICY.md').write_text(md("SCHEMA-COMPAT-001","Schema Compatibility Policy", """
## Compatibility classes

### Compatible

Examples:

- adding an optional property
- adding descriptions or examples
- adding an optional extension point
- fixing a validator defect that did not define intended contract behavior

### Conditionally compatible

Examples:

- broadening a string pattern
- adding an enum value that some consumers may not recognize
- changing format enforcement
- changing defaulting behavior outside the schema
- adding optional fields consumed as mandatory by downstream code

These changes require consumer review.

### Breaking

Examples:

- adding a required property
- removing or renaming a property
- narrowing an enum
- changing a property type
- closing an object that was previously open
- changing a field's meaning
- changing identifier or reference behavior relied on by consumers

## Required analysis

For each change, identify:

- currently valid instances that could fail
