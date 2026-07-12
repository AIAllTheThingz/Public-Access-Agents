---
id: DISC-EX-INT-ADOPTION
title: Integration Engineering Adoption Example
version: 0.1.0
status: baseline
---
# Integration Engineering Adoption Example

This example shows composition, not a universal project design.

## Example project

A fictitious project determines that the **Integration Engineering** discipline applies because:

- two systems exchange data or commands
- a vendor or external service is introduced
- message delivery, retries, duplication, or ordering matter

The project composes:

- root governance standards
- one applicable language package
- one project profile
- this discipline package
- the [`API Engineering`](../../api-engineering/) discipline
- the [`Application Security`](../../application-security/) discipline
- the [`Data Engineering`](../../data-engineering/) discipline

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

- owned integration contract
- data mapping and classification
- failure and duplicate-delivery tests
- migration and rollback plan
- monitoring and reconciliation evidence

The completion report also lists checks not run, known limitations, accepted exceptions, residual risks, and follow-up owners.

All project names, targets, users, and values in an adopted example must be fictitious or approved for public documentation.
