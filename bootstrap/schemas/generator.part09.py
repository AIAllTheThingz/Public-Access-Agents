"invalid":{"status":"done","summary":"","filesChanged":"README.md","validation":[],"limitations":[]}
},
"exception-record":{
"valid":{
    "schemaVersion":"1.0.0",
    "id":"EXAMPLE-EXCEPTION-001",
    "ruleId":"EXAMPLE-RULE-001",
    "owner":"fictitious-owner",
    "reason":"Illustrative temporary compatibility constraint.",
    "risk":"A bounded unsupported component remains temporarily.",
    "riskLevel":"moderate",
    "compensatingControls":["Restricted exposure","Additional monitoring"],
    "expiresOn":"2030-01-31",
    "status":"requested"
},
"invalid":{"id":"EX-1","ruleId":"RULE-1","owner":"","reason":"","risk":"","compensatingControls":[],"expiresOn":"not-a-date","status":"permanent"}
},
"project-manifest":{
"valid":{
    "schemaVersion":"1.0.0",
    "name":"example-service",
    "profile":"WEB_API",
    "languages":["python"],
    "disciplines":["application-security","testing"],
    "platforms":["containers"],
    "frameworks":["fastapi"],
    "risk":"moderate",
    "exceptions":[]
},
"invalid":{"name":"example-service","profile":"","languages":[],"disciplines":"testing"}
},
"risk-classification":{
"valid":{
    "schemaVersion":"1.0.0",
    "level":"high",
    "rationale":"Illustrative privileged production change.",
    "factors":{"privilege":"administrative","blastRadius":"multiple systems"},
    "requiredReviewers":["security-reviewer","operations-owner"],
    "rollbackRequired":True
},
"invalid":{"level":"severe","rationale":"","factors":{}}
},
"test-evidence":{
"valid":{
    "schemaVersion":"1.0.0",
    "testType":"schema-validation",
    "command":"python tools/validate-schemas/validate_schemas.py",
    "result":"passed",
    "environment":"fictitious CI runner",
    "startedAt":"2030-01-01T00:00:00Z",
    "completedAt":"2030-01-01T00:00:01Z",
    "evidence":"illustrative example",
    "limitations":["No application runtime was exercised."],
    "exitCode":0
},
"invalid":{"testType":"","command":"","result":"maybe","completedAt":"yesterday"}
}
}

for name, pair in examples.items():
    d = root/'schemas'/'examples'/name
    d.mkdir(parents=True)
    (d/'valid.example.json').write_text(json.dumps(pair['valid'], indent=2)+"\n", encoding='utf-8')
    (d/'invalid.example.json').write_text(json.dumps(pair['invalid'], indent=2)+"\n", encoding='utf-8')
    (d/'README.md').write_text(md(f"SCHEMA-EX-{name.upper().replace('-','-')}-001", f"{schemas[name]['title']} Examples", f"""
## Positive example

[`valid.example.json`](valid.example.json) must validate against:

- [`../../{name}.schema.json`](../../{name}.schema.json)
- [`../../v1/{name}.schema.json`](../../v1/{name}.schema.json)

## Negative example

[`invalid.example.json`](invalid.example.json) is intentionally invalid and must be rejected.

## Boundary

A positive example demonstrates structural conformance only. It does not represent a production record, authorized decision, genuine artifact, executed command, or accepted risk.
"""), encoding='utf-8')

(root/'schemas'/'examples'/'README.md').write_text(md("SCHEMA-EX-INDEX-001","Schema Examples", """
## Purpose

The examples provide executable contract tests.

Each schema directory contains:

- `valid.example.json`, which must pass
- `invalid.example.json`, which must fail
- a README describing the boundary

## Safety

All values are fictitious. Do not add production credentials, internal endpoints, real incident records, personal data, or confidential vulnerability details.

## Validation

```bash
python tools/validate-schemas/validate_schemas.py
```
"""), encoding='utf-8')

# validation tool
validator = r'''#!/usr/bin/env python3
"""Validate schema documents, examples, and repository instances."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
    import jsonschema
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    raise SystemExit(
        "Missing dependency 'jsonschema'. Install with: "
