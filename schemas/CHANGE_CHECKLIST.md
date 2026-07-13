---
id: SCHEMA-CHANGE-001
title: Schema Change Checklist
version: 0.2.0
status: baseline
---

# Schema Change Checklist

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
