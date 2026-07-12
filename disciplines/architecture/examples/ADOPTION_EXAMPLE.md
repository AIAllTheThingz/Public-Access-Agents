---
id: DISC-EX-ARCH-ADOPTION
title: Architecture and System Design Adoption Example
version: 0.1.0
status: baseline
---
# Architecture and System Design Adoption Example

This example shows composition, not a universal project design.

## Example project

A fictitious project determines that the **Architecture and System Design** discipline applies because:

- a new component, service, data store, or external dependency is introduced
- a public contract or trust boundary changes
- availability, scalability, latency, recoverability, or maintainability is material

The project composes:

- root governance standards
- one applicable language package
- one project profile
- this discipline package
- the [`Application Security`](../../application-security/) discipline
- the [`Testing and Quality Engineering`](../../testing/) discipline
- the [`Observability`](../../observability/) discipline

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

- system context and component diagrams
- accepted ADRs
- quality-attribute acceptance criteria
- failure-mode analysis
- validation of high-risk assumptions

The completion report also lists checks not run, known limitations, accepted exceptions, residual risks, and follow-up owners.

All project names, targets, users, and values in an adopted example must be fictitious or approved for public documentation.
