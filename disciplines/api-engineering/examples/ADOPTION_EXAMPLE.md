---
id: DISC-EX-API-ADOPTION
title: API Engineering Adoption Example
version: 0.1.0
status: baseline
---
# API Engineering Adoption Example

This example shows composition, not a universal project design.

## Example project

A fictitious project determines that the **API Engineering** discipline applies because:

- HTTP, RPC, event, or programmatic interfaces are created or changed
- clients depend on a contract
- mutating operations require retry or idempotency semantics

The project composes:

- root governance standards
- one applicable language package
- one project profile
- this discipline package
- the [`Application Security`](../../application-security/) discipline
- the [`Testing and Quality Engineering`](../../testing/) discipline
- the [`Integration Engineering`](../../integration/) discipline

## Tailored project instructions

The project `AGENTS.md` adds:

- named owners and reviewers
- exact supported environments and boundaries
- project-specific tools and validation commands
- required evidence locations
- compatibility, migration, rollback, recovery, and support constraints
- stricter rules required by the organization

It does not remove shared controls merely because they are inconvenient.

## Example evidence summary

- machine-readable API contract
- positive and negative authorization tests
- compatibility analysis
- idempotency and retry tests
- operational limits and telemetry evidence

The completion report also lists checks not run, known limitations, accepted exceptions, residual risks, and follow-up owners.

All project names, targets, users, and values in an adopted example must be fictitious or approved for public documentation.
