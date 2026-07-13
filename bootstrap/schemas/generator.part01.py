from pathlib import Path
import json, textwrap, shutil, os, re, hashlib, tarfile, lzma, base64
from copy import deepcopy

root = Path.cwd()
(root/'schemas').mkdir(parents=True, exist_ok=True)
(root/'schemas'/'v1').mkdir(parents=True, exist_ok=True)
(root/'schemas'/'examples').mkdir(parents=True, exist_ok=True)
(root/'tools'/'validate-schemas').mkdir(parents=True, exist_ok=True)

def md(doc_id, title, body, version="0.2.0", status="baseline"):
    return f"""---
id: {doc_id}
title: {title}
version: {version}
status: {status}
---

# {title}

{body.strip()}
"""

common_extensions = {
    "schemaVersion": {
        "type": "string",
        "const": "1.0.0",
        "description": "Optional explicit instance contract version. Omitted legacy instances are interpreted as version 1.0.0."
    },
    "extensions": {
        "type": "object",
        "description": "Namespaced extension data. Extension keys must be organization- or product-specific and must not redefine standard fields.",
        "propertyNames": {
            "pattern": "^[A-Za-z][A-Za-z0-9_.-]{1,127}$"
        },
        "additionalProperties": True
    }
}

def schema_base(name, title, description, properties, required, defs=None):
    s = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"https://raw.githubusercontent.com/AIAllTheThingz/Public-Access-Agents/main/schemas/{name}.schema.json",
        "title": title,
        "description": description,
        "type": "object",
        "additionalProperties": False,
        "required": required,
        "properties": {**properties, **deepcopy(common_extensions)}
    }
    if defs:
        s["$defs"] = defs
    return s

nonempty = {"type": "string", "minLength": 1}
risk_enum = ["low", "moderate", "high", "critical"]
result_enum = ["passed", "failed", "not-run"]

schemas = {}

schemas["artifact-record"] = schema_base(
    "artifact-record",
    "Artifact Record",
    "Identifies a produced artifact, its source revision, digest, build context, provenance, and signing state.",
    {
        "name": {"type":"string","minLength":1,"description":"Human-readable artifact name."},
        "type": {"type":"string","minLength":1,"description":"Artifact kind, such as container-image, package, archive, executable, or standards-composition."},
        "digest": {"type":"string","minLength":1,"description":"Algorithm-qualified digest or another immutable integrity identifier."},
        "sourceCommit": {"type":"string","minLength":1,"description":"Source commit or immutable source revision."},
        "buildRun": {"type":"string","minLength":1,"description":"Build or CI run identifier."},
        "provenance": {"type":"string","minLength":1,"description":"Provenance statement or location."},
        "signed": {"type":"boolean","description":"Whether the artifact carries an approved cryptographic signature."},
        "signatureEvidence": {"type":"string","minLength":1,"description":"Optional signature verification evidence or location."},
        "createdAt": {"type":"string","format":"date-time","description":"Artifact creation time in RFC 3339 form."},
        "limitations": {"type":"array","items":{"type":"string","minLength":1},"uniqueItems":True}
    },
    ["name","type","digest","sourceCommit"]
)

schemas["completion-result"] = schema_base(
    "completion-result",
    "Completion Result",
    "Records implementation state, validation outcomes, limitations, risk, compatibility impact, and review without treating a single successful command as proof of full completion.",
    {
        "status": {"enum":["implemented","validated","partially-validated","not-completed"],"description":"Overall completion state."},
        "summary": {"type":"string","minLength":1},
        "filesChanged": {"type":"array","items":{"type":"string","minLength":1},"uniqueItems":True},
        "risk": {"enum":risk_enum},
        "securityImpact": {"type":"string","minLength":1},
