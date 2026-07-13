---
id: MATURITY-REVIEW-INDEX-001
title: Maturity Review Records
version: 0.9.0
status: baseline
---

# Maturity Review Records

## Purpose

This directory stores evidence-backed decisions that promote, defer, reject, demote, or deprecate repository components.

Requirements are defined by [`../MATURITY_POLICY.md`](../MATURITY_POLICY.md).

## Required structure

```text
maturity-reviews/
├── README.md
├── TEMPLATE.md
└── examples/
    └── BASELINE_TO_STABLE_EXAMPLE.md
```

Completed review records should use a stable filename such as:

```text
<component-id>-<from>-to-<to>-<yyyy-mm-dd>.md
```

## Decision boundary

A maturity review records repository confidence in a component. It does not certify an adopting project, guarantee future compatibility beyond the release policy, or replace specialist review.
