---
id: DISC-EX-APPSEC-ADOPTION
title: Application Security Adoption Example
version: 0.1.0
status: baseline
---
# Application Security Adoption Example

This example shows composition, not a universal project design.

## Example project

A fictitious project determines that the **Application Security** discipline applies because:

- the system accepts untrusted input
- protected operations or sensitive data exist
- the change crosses a trust boundary

The project composes:

- root governance standards
- one applicable language package
- one project profile
- this discipline package
- the [`Architecture and System Design`](../../architecture/) discipline
- the [`Testing and Quality Engineering`](../../testing/) discipline
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

- threat model or security review
- positive and negative authorization tests
- input and abuse-case tests
- dependency and secret-scan results
- documented residual risks and exceptions

The completion report also lists checks not run, known limitations, accepted exceptions, residual risks, and follow-up owners.

All project names, targets, users, and values in an adopted example must be fictitious or approved for public documentation.
