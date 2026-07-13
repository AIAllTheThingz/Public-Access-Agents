---
id: TOOL-CONTRACT-001
title: Tool Result Contract
version: 1.0.0
status: baseline
---

# Tool Result Contract

## Purpose

`tool-result.schema.json` defines the common JSON result emitted by executable repository tools.

The contract separates:

- tool identity and version
- overall status
- summary counters
- structured findings
- non-normative metadata

## Status values

- `passed`: the tool completed and found no error-level findings
- `failed`: the tool completed and found one or more validation failures
- `error`: the tool could not complete because of configuration, dependency, input, or internal failure

## Finding severity

- `error`: causes validation failure
- `warning`: does not fail the tool unless a tool-specific strict mode says otherwise
- `info`: records useful context

## Compatibility

New optional summary or metadata fields may be added without changing the contract. Required top-level fields and status meanings are stable for version 1.

## Boundary

A `passed` result proves only that the named tool completed its implemented checks against the identified input. It does not prove security, compliance, semantic truth, authorization, or production readiness.
