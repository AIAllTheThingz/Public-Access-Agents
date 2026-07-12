---
id: DISC-EX-DATA-ADOPTION
title: Data Engineering Adoption Example
version: 0.1.0
status: baseline
---
# Data Engineering Adoption Example

This example shows composition, not a universal project design.

## Example project

A fictitious project determines that the **Data Engineering** discipline applies because:

- data is ingested, transformed, moved, aggregated, or published
- schemas or quality expectations change
- backfills or replay are possible

The project composes:

- root governance standards
- one applicable language package
- one project profile
- this discipline package
- the [`Database Engineering`](../../database/) discipline
- the [`Privacy and Data Governance`](../../privacy/) discipline
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

- data contract and ownership
- lineage documentation
- quality-test results
- replay or backfill evidence
- privacy and access review

The completion report also lists checks not run, known limitations, accepted exceptions, residual risks, and follow-up owners.

All project names, targets, users, and values in an adopted example must be fictitious or approved for public documentation.
