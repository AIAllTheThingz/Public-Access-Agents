- JSON pointer to the failing value
- validator rule
- human-readable error

A validation error should be resolved by one of:

- correcting the instance
- correcting an unintended schema defect
- performing an approved versioned schema change
- documenting an explicit migration

Disabling validation is not remediation.

## Local consumer validation

Adopting repositories should add:

- representative contract tests
- producer tests
- consumer tests
- stored-record migration tests
- negative tests
- version compatibility tests
- CI gating for material records
"""), encoding='utf-8')

(root/'schemas'/'DESIGN_RULES.md').write_text(md("SCHEMA-DESIGN-001","Schema Design Rules", """
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
"""), encoding='utf-8')

(root/'schemas'/'CHANGE_CHECKLIST.md').write_text(md("SCHEMA-CHANGE-001","Schema Change Checklist", """
## Before editing

- [ ] Identify contract owner.
- [ ] Identify producers and consumers.
- [ ] Inventory repository instances.
- [ ] Classify compatibility.
- [ ] Define migration impact.
- [ ] Confirm target JSON Schema draft.

## During editing

- [ ] Preserve stable rolling filenames.
- [ ] Update the versioned copy.
- [ ] Keep rolling and versioned definitions synchronized.
- [ ] Add or update positive examples.
- [ ] Add or update negative examples.
- [ ] Update documentation and catalog.
- [ ] Keep custom data under `extensions`.
- [ ] Avoid production secrets and identities.

## Validation

- [ ] Meta-schema validation passed.
- [ ] Positive examples passed.
- [ ] Negative examples failed as expected.
- [ ] Repository instances passed.
- [ ] Format checking was enabled.
- [ ] Consumer tests were run where available.
- [ ] Checks not run are recorded.

## Review

- [ ] Compatibility and migration were reviewed.
- [ ] Breaking changes have explicit approval.
- [ ] Historical evidence handling is defined.
- [ ] Release and deprecation notes are complete.
"""), encoding='utf-8')

# examples
examples = {
"artifact-record": {
"valid": {
    "schemaVersion":"1.0.0",
    "name":"example-package",
    "type":"archive",
    "digest":"sha256:0123456789abcdef",
    "sourceCommit":"0000000000000000000000000000000000000000",
    "buildRun":"example-run-001",
    "provenance":"fictitious documentation example",
    "signed":False,
    "limitations":["Not a release artifact."]
},
"invalid":{"name":"","type":"archive","digest":"sha256:abc"}
},
"completion-result":{
"valid":{
    "schemaVersion":"1.0.0",
    "status":"partially-validated",
    "summary":"Illustrative standards-only validation record.",
    "filesChanged":["README.md"],
    "risk":"low",
    "validation":[{"name":"Schema validation","result":"passed","evidence":"example only"}],
    "limitations":["No runtime behavior was tested."],
    "reviewer":"fictitious-reviewer"
},
