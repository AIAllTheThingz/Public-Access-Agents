---
id: SCHEMA-COMPAT-001
title: Schema Compatibility Policy
version: 0.3.0
status: baseline
---

# Schema Compatibility Policy

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
- currently invalid instances that could pass
- code generators and strongly typed consumers
- validation libraries and supported drafts
- stored historical records
- CI, release, governance, and audit dependencies
- external consumers not visible in this repository

## Compatibility promise

The version 1 contracts preserve the repository's existing required fields and current valid instances. Compatible optional properties may be added within the `v1/` major path; consumers requiring an immutable artifact must also pin a repository tag or commit.

The optional `schemaVersion` and `extensions` properties are backward-compatible additions. Project-manifest version `1.1.0` adds optional `virtualization`, `operatingSystems`, and `networking` arrays without invalidating version `1.0.0` instances. Any instance containing one of those arrays must declare version `1.1.0`.

## Validation versus compatibility

A schema can pass meta-validation and still introduce a breaking consumer change. The meta-schema checks schema syntax and dialect rules. It does not know what your consumers built around last Tuesday's interpretation.
