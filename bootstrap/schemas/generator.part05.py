- `schemas/v1/*.schema.json`
- schema examples
- schema versioning and compatibility documents
- schema validation tooling
- repository instances governed by these schemas

## Instruction precedence

1. Applicable legal, contractual, safety, and security obligations
2. Explicit authorized requirements
3. Root repository `AGENTS.md`
4. Governance standards
5. These schema instructions
6. More-specific local instructions
7. Repository conventions

Local instructions may strengthen controls. They may not silently weaken compatibility, evidence integrity, or governance.

## Required behavior

- Preserve the six existing rolling filenames.
- Do not remove or rename a required field without a versioned breaking change.
- Keep rolling and versioned schema copies synchronized.
- Keep schemas closed by default.
- Put custom data under the `extensions` object.
- Do not reuse a standard property name for a different meaning.
- Validate schema documents against Draft 2020-12.
- Validate positive examples and require negative examples to fail.
- Identify affected repository instances and downstream consumers.
- Enable format checking when evaluating `date` and `date-time`.
- Do not claim semantic truth from structural validation.
- Do not add production secrets, identities, endpoints, or internal evidence to examples.
- State compatibility and migration impact.
- Preserve deterministic, readable JSON formatting.

## Required working method

1. Inspect the current schema, versioned copy, examples, consumers, and validation tooling.
2. Define the intended contract change.
3. Classify compatibility.
4. Update the smallest coherent set of files.
5. Add positive and negative cases.
6. Run schema meta-validation.
7. Run repository instance validation.
8. Review the diff for accidental required fields, enum narrowing, closed-object changes, and stale examples.
9. Document migration and checks not run.
10. Obtain accountable review.

## Completion gate

Schema work is incomplete until:

- rolling and versioned contracts agree
- schema documents pass meta-validation
- positive examples pass
- negative examples fail
- repository instances pass
- compatibility is classified
- migration guidance is updated when needed
- no unresolved placeholder or sensitive value remains
- evidence and limitations are recorded
"""), encoding='utf-8')

(root/'schemas'/'MANIFEST.md').write_text(md("SCHEMA-MANIFEST-001","Schema Package Manifest", """
## Required collection files

- `AGENTS.md`
- `README.md`
- `SCHEMA_CATALOG.md`
- `VERSIONING_POLICY.md`
- `COMPATIBILITY_POLICY.md`
- `EXTENSION_POLICY.md`
- `MIGRATION_GUIDE.md`
- `VALIDATION_GUIDE.md`
- `DESIGN_RULES.md`
- `CHANGE_CHECKLIST.md`

## Required schema files

Rolling and versioned copies are required for:

- artifact record
- completion result
- exception record
- project manifest
- risk classification
- test evidence

## Required examples

Each contract must have:

- `valid.example.json`
- `invalid.example.json`
- example README

## Required tooling

- `tools/validate-schemas/validate_schemas.py`
- `tools/validate-schemas/requirements.txt`
- `tools/validate-schemas/README.md`

## Acceptance checks

- Draft 2020-12 meta-validation passes.
- Rolling and versioned schemas are equivalent except for identifier metadata.
- All positive examples validate.
- All negative examples fail.
- All discovered repository instances validate.
- Format checking is enabled.
- Every JSON document parses.
- Relative Markdown links pass.
- No schema or example contains an unresolved placeholder.
- The six stable rolling filenames remain present.
"""), encoding='utf-8')

catalog_rows = []
for n, s in schemas.items():
    catalog_rows.append(f"| `{n}` | `{n}.schema.json` | `v1/{n}.schema.json` | {s['description']} |")
(root/'schemas'/'SCHEMA_CATALOG.md').write_text(md("SCHEMA-CATALOG-001","Schema Catalog", f"""
## Purpose

