---
id: TEMPLATE-EX-ARCHITECTURE-DECISION-001
title: Architecture Decision Record Example
version: 0.2.0
status: baseline
---

# Architecture Decision Record Example

- ADR: `ADR-0042`
- Status: `accepted`
- Date: `2030-01-15`
- Owners: architecture owner
- Reviewers: security reviewer, operations owner
- Supersedes: none

## Context

A fictitious internal service needs durable job submission without coupling request latency to report generation.

## Decision drivers

- predictable API latency
- retry and replay support
- independent worker scaling
- traceable job state
- bounded operational complexity

## Considered options

1. Synchronous processing: simplest, but request duration and retry behavior are unacceptable.
2. Database-backed queue: fits existing operations but adds polling and contention.
3. Managed message broker: supports delivery semantics and worker scaling with added platform dependency.

## Decision

Use a managed message broker with explicit idempotency keys and a durable job-status store.

## Security and privacy impact

Messages contain identifiers, not report contents or credentials. Access uses workload identity.

## Compatibility and migration impact

The API adds a job resource and asynchronous status contract.

## Operational impact

Operations owns queue depth alerts, dead-letter handling, and replay runbooks.

## Consequences

Positive: decoupled scaling and retry. Negative: another service dependency. Neutral: clients must poll or consume callbacks.

## Validation and evidence

Load test, duplicate-delivery test, provider-failure test, and dead-letter rehearsal.

## Revisit triggers

Provider support changes, sustained queue delay, or a new cross-region requirement.
