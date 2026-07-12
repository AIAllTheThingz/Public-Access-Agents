---
id: DISC-EX-DB-ADOPTION
title: Database Engineering Adoption Example
version: 0.1.0
status: baseline
---
# Database Engineering Adoption Example

This example shows composition, not a universal project design.

## Example project

A fictitious project determines that the **Database Engineering** discipline applies because:

- schemas, indexes, constraints, stored code, or queries change
- data migration or backfill occurs
- transactional integrity or concurrency matters

The project composes:

- root governance standards
- one applicable language package
- one project profile
- this discipline package
- the [`Architecture and System Design`](../../architecture/) discipline
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

- reviewed schema and migration
- query-plan evidence
- constraint and concurrency tests
- least-privilege review
- restore or recovery evidence

The completion report also lists checks not run, known limitations, accepted exceptions, residual risks, and follow-up owners.

All project names, targets, users, and values in an adopted example must be fictitious or approved for public documentation.
