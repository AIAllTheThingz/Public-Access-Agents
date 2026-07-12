---
id: DISC-EX-OBS-ADOPTION
title: Observability Adoption Example
version: 0.1.0
status: baseline
---
# Observability Adoption Example

This example shows composition, not a universal project design.

## Example project

A fictitious project determines that the **Observability** discipline applies because:

- software runs as a service, job, workflow, integration, or operational process
- failures require diagnosis
- availability, latency, throughput, backlog, or business outcomes matter

The project composes:

- root governance standards
- one applicable language package
- one project profile
- this discipline package
- the [`Site Reliability Engineering`](../../sre/) discipline
- the [`Application Security`](../../application-security/) discipline
- the [`Privacy and Data Governance`](../../privacy/) discipline

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

- telemetry plan tied to operations
- sample logs, metrics, and traces
- health-check tests
- alert and runbook review
- redaction and cardinality review

The completion report also lists checks not run, known limitations, accepted exceptions, residual risks, and follow-up owners.

All project names, targets, users, and values in an adopted example must be fictitious or approved for public documentation.
