            errors.append(f"Missing positive example: {valid_path.relative_to(ROOT)}")
        else:
            errors.extend(validate_instance(valid_path, versioned_path, True))

        if not invalid_path.is_file():
            errors.append(f"Missing negative example: {invalid_path.relative_to(ROOT)}")
        else:
            errors.extend(validate_instance(invalid_path, versioned_path, False))

    for path in sorted(ROOT.rglob("*.json")):
        if SCHEMA_ROOT in path.parents:
            continue
        schema_name = discover_schema(path)
        if schema_name is None:
            continue
        schema_path = SCHEMA_ROOT / "v1" / f"{schema_name}.schema.json"
        errors.extend(validate_instance(path, schema_path, True))

    if errors:
        print("Schema validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Schema validation passed: "
        f"{len(SCHEMA_NAMES)} rolling schemas, "
        f"{len(SCHEMA_NAMES)} versioned schemas, "
        f"{len(SCHEMA_NAMES)} positive examples, "
        f"{len(SCHEMA_NAMES)} negative examples."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''
(root/'tools'/'validate-schemas'/'validate_schemas.py').write_text(validator, encoding='utf-8')
(root/'tools'/'validate-schemas'/'requirements.txt').write_text("jsonschema[format]==4.26.0\n", encoding='utf-8')
(root/'tools'/'validate-schemas'/'README.md').write_text(md("TOOL-SCHEMA-VALIDATE-001","Schema Validation Tool", """
## Purpose

Validates:

- Draft 2020-12 schema syntax
- rolling and versioned schema equivalence
- positive examples
- negative examples
- repository instances discovered by filename
- date and date-time formats

## Install

```bash
python -m pip install -r tools/validate-schemas/requirements.txt
```

## Run

```bash
python tools/validate-schemas/validate_schemas.py
```

## Dependency

The tool pins `jsonschema[format]` to a reviewed version so CI and local validation use the same implementation.

## Boundary

The tool validates structure. It does not establish truth, authorization, security, compliance, or production readiness.
"""), encoding='utf-8')

# Root docs content based on current fetched state.
catalog_current = """# Standards Catalog

This catalog lists the standards available for composition into a project.

## Governance

The governance system defines authority, precedence, risk, evidence, review, exceptions, secure development, production readiness, threat modeling, vulnerability response, and policy lifecycle across every package in this repository.

| Standard | Purpose |
|---|---|
| [Governance index](governance/README.md) | Selection, precedence, operating model, adoption, evidence states, and maintenance |
| [Organization Contract](governance/ORGANIZATION_CONTRACT.md) | Defines precedence, non-negotiable controls, authority, and accountability |
| [Agent Working Method](governance/AGENT_WORKING_METHOD.md) | Defines discovery, planning, implementation, validation, and reporting |
| [Risk Classification](governance/RISK_CLASSIFICATION.md) | Scales review, testing, authorization, rollback, and evidence |
| [Completion Evidence](governance/COMPLETION_EVIDENCE.md) | Defines proof required before claiming completion |
| [Exception Process](governance/EXCEPTION_PROCESS.md) | Provides a time-bounded, reviewed path for deviations |
| [AI-Generated Code Policy](governance/AI_GENERATED_CODE_POLICY.md) | Defines responsibility, verification, provenance, and review for AI-assisted work |
| [Human Review Policy](governance/HUMAN_REVIEW_POLICY.md) | Defines work requiring accountable human review and approval |
| [Production Readiness](governance/PRODUCTION_READINESS.md) | Defines operational, recovery, support, and go-live gates |
| [Secure Development Policy](governance/SECURE_DEVELOPMENT_POLICY.md) | Integrates security into design, implementation, testing, delivery, and maintenance |
