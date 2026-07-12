---
id: DISC-EX-SUPPLY-ADOPTION
title: Software Supply Chain Adoption Example
version: 0.1.0
status: baseline
---
# Software Supply Chain Adoption Example

This example shows composition, not a universal project design.

## Example project

A fictitious project determines that the **Software Supply Chain** discipline applies because:

- dependencies, build tools, package registries, containers, actions, plugins, or generated artifacts change
- software is published or deployed
- third-party code enters trusted build or runtime paths

The project composes:

- root governance standards
- one applicable language package
- one project profile
- this discipline package
- the [`CI/CD`](../../ci-cd/) discipline
- the [`Application Security`](../../application-security/) discipline
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

- dependency inventory or SBOM
- dependency and license review
- reproducible resolution evidence
- vulnerability results and exceptions
- artifact provenance or traceability

The completion report also lists checks not run, known limitations, accepted exceptions, residual risks, and follow-up owners.

All project names, targets, users, and values in an adopted example must be fictitious or approved for public documentation.
