---
id: DISC-EX-CICD-ADOPTION
title: CI/CD Adoption Example
version: 0.1.0
status: baseline
---
# CI/CD Adoption Example

This example shows composition, not a universal project design.

## Example project

A fictitious project determines that the **CI/CD** discipline applies because:

- automated workflows build, test, scan, package, release, deploy, or modify infrastructure
- third-party actions or tools execute
- secrets, environments, approvals, or production promotion are involved

The project composes:

- root governance standards
- one applicable language package
- one project profile
- this discipline package
- the [`Software Supply Chain`](../../supply-chain/) discipline
- the [`Testing and Quality Engineering`](../../testing/) discipline
- the [`Release Engineering`](../../release-engineering/) discipline

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

- workflow and trust-boundary review
- least-permission evidence
- pinned dependency review
- successful required gates
- artifact and deployment traceability

The completion report also lists checks not run, known limitations, accepted exceptions, residual risks, and follow-up owners.

All project names, targets, users, and values in an adopted example must be fictitious or approved for public documentation.
