---
id: DISC-EX-REL-ADOPTION
title: Release Engineering Adoption Example
version: 0.1.0
status: baseline
---
# Release Engineering Adoption Example

This example shows composition, not a universal project design.

## Example project

A fictitious project determines that the **Release Engineering** discipline applies because:

- software or infrastructure is versioned, packaged, promoted, deployed, published, or handed to operations
- breaking changes, migrations, or coordinated rollout exist
- release artifacts require integrity or provenance

The project composes:

- root governance standards
- one applicable language package
- one project profile
- this discipline package
- the [`CI/CD`](../../ci-cd/) discipline
- the [`Software Supply Chain`](../../supply-chain/) discipline
- the [`Site Reliability Engineering`](../../sre/) discipline

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

- version and compatibility decision
- release plan and approvals
- immutable artifact identity
- release notes and migration guidance
- rollout and rollback evidence

The completion report also lists checks not run, known limitations, accepted exceptions, residual risks, and follow-up owners.

All project names, targets, users, and values in an adopted example must be fictitious or approved for public documentation.
