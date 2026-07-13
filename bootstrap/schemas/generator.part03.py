            "type":"object",
            "minProperties":1,
            "additionalProperties":{"type":"string","minLength":1}
        },
        "requiredReviewers":{"type":"array","items":{"type":"string","minLength":1},"uniqueItems":True},
        "rollbackRequired":{"type":"boolean"},
        "owner":{"type":"string","minLength":1},
        "classifiedAt":{"type":"string","format":"date-time"},
        "reassessmentTriggers":{"type":"array","items":{"type":"string","minLength":1},"uniqueItems":True}
    },
    ["level","rationale","factors"]
)

schemas["test-evidence"] = schema_base(
    "test-evidence",
    "Test Evidence",
    "Records an executed or explicitly not-run validation command, result, environment, timing, evidence, and limitations.",
    {
        "testType":{"type":"string","minLength":1},
        "command":{"type":"string","minLength":1},
        "result":{"enum":result_enum},
        "environment":{"type":"string","minLength":1},
        "startedAt":{"type":"string","format":"date-time"},
        "completedAt":{"type":"string","format":"date-time"},
        "evidence":{"type":"string","minLength":1},
        "limitations":{"type":"array","items":{"type":"string","minLength":1}},
        "artifact":{"type":"string","minLength":1},
        "exitCode":{"type":"integer"}
    },
    ["testType","command","result"]
)

# Write rolling and versioned copies. Versioned copies use versioned IDs.
for name, s in schemas.items():
    top = deepcopy(s)
    v1 = deepcopy(s)
    v1["$id"] = f"https://raw.githubusercontent.com/AIAllTheThingz/Public-Access-Agents/main/schemas/v1/{name}.schema.json"
    top["x-schemaVersion"] = "1.0.0"
    top["x-versionedSchema"] = f"v1/{name}.schema.json"
    v1["x-schemaVersion"] = "1.0.0"
    (root/'schemas'/f'{name}.schema.json').write_text(json.dumps(top, indent=2)+"\n", encoding='utf-8')
    (root/'schemas'/'v1'/f'{name}.schema.json').write_text(json.dumps(v1, indent=2)+"\n", encoding='utf-8')

# docs
readme_body = """
## Purpose

This directory defines the repository's machine-readable contracts for standards composition, risk, exceptions, testing, artifacts, and completion evidence.

Schemas make records structurally testable. They do not prove that the record is truthful, complete, authorized, secure, compliant, or tied to the correct artifact. A beautifully valid lie remains a lie, merely one with matching braces.

## Current dialect and implementation baseline

The schemas use JSON Schema Draft 2020-12.

The repository validator uses Python and the `jsonschema` package. The pinned validation dependency is documented under [`tools/validate-schemas/`](../tools/validate-schemas/).

Official references:

- [JSON Schema specification](https://json-schema.org/specification)
- [Draft 2020-12 meta-schema](https://json-schema.org/draft/2020-12/schema)
- [Python jsonschema documentation](https://python-jsonschema.readthedocs.io/)

## Schema catalog

| Schema | Purpose | Common repository instances |
|---|---|---|
| [`artifact-record.schema.json`](artifact-record.schema.json) | Identify an artifact, source revision, digest, provenance, and signing state. | `artifact-record*.json` |
| [`completion-result.schema.json`](completion-result.schema.json) | Record completion state, validation, limitations, risk, and review. | `completion-result*.json` |
| [`exception-record.schema.json`](exception-record.schema.json) | Record time-bounded standards exceptions and compensating controls. | `exception-record*.json` |
| [`project-manifest.schema.json`](project-manifest.schema.json) | Declare profile and package composition for a project. | `project-manifest.json` |
| [`risk-classification.schema.json`](risk-classification.schema.json) | Record risk level, rationale, factors, reviewers, and rollback need. | `risk-classification*.json` |
| [`test-evidence.schema.json`](test-evidence.schema.json) | Record exact validation commands, results, environment, and limitations. | `test-evidence*.json` |

