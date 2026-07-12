---
id: DISC-EX-DOC-ADOPTION
title: Documentation Adoption Example
version: 0.1.0
status: baseline
---
# Documentation Adoption Example

This example shows composition, not a universal project design.

## Example project

A fictitious project determines that the **Documentation** discipline applies because:

- software, configuration, behavior, operations, interfaces, deployment, or support processes change
- non-authors need to understand, use, maintain, or recover the system
- material design decisions require a durable record

The project composes:

- root governance standards
- one applicable language package
- one project profile
- this discipline package
- the [`Architecture and System Design`](../../architecture/) discipline
- the [`Testing and Quality Engineering`](../../testing/) discipline
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

- audience and task coverage
- updated operational and user documentation
- validated examples and links
- decision records where needed
- documented ownership and known gaps

The completion report also lists checks not run, known limitations, accepted exceptions, residual risks, and follow-up owners.

All project names, targets, users, and values in an adopted example must be fictitious or approved for public documentation.
