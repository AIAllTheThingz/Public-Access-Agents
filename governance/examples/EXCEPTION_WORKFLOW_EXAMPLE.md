---
id: GOV-EX-EXCEPT-001
title: Exception Workflow Example
version: 0.2.0
status: baseline
---

# Exception Workflow Example

## Fictitious request

A supported dependency update cannot be completed before a release because an upstream compatibility defect remains unresolved.

## Required record

- exact dependency rule
- affected versions
- reason
- vulnerability and support risk
- compensating controls
- monitoring
- owner
- approver
- expiration
- remediation issue
- renewal criteria

## Decision

The exception is temporary and applies only to the named version and release. It does not approve unrelated unsupported components.

## Closure

Close when the supported update is deployed and verified. A vanished scanner finding is not closure evidence.
