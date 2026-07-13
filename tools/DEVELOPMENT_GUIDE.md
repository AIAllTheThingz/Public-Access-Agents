---
id: TOOL-DEVELOP-001
title: Tool Development Guide
version: 1.0.0
status: baseline
---

# Tool Development Guide

## Design principles

- Prefer the Python standard library for repository-local behavior.
- Pin unavoidable dependencies used in CI.
- Keep validators read-only.
- Separate discovery, validation, reporting, and writing.
- Return structured findings rather than printing ad hoc prose from deep functions.
- Keep path handling explicit and rooted.
- Avoid shell execution when direct subprocess argument lists are available.
- Treat generated content as a public contract.

## Adding a tool

A new tool package requires:

1. stable entry point
2. shared command-line options
3. structured result output
4. package README and manifest
5. examples README
6. unit tests
7. tool catalog entry
8. permanent CI integration when applicable
9. compatibility classification
10. security-boundary review

## Changing a validator

Review whether the change:

- rejects content that previously passed
- accepts content that previously failed
- changes finding codes
- changes path or line reporting
- changes scope or exclusions
- changes dependency behavior

Add fixtures for both old and new behavior.

## Changing a generator

Review:

- overwrite behavior
- dry-run fidelity
- deterministic ordering
- partial failure handling
- path traversal
- source traceability
- sensitive data handling
- migration of generated files

## Code review

Reviewers should inspect:

- unsafe filesystem operations
- broad exception swallowing
- shell injection
- ambiguous root resolution
- unstable ordering
- hidden network access
- unbounded recursion or file loading
- misleading success statuses
- untested negative paths
