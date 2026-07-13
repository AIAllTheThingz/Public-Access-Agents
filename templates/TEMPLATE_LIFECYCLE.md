---
id: TEMPLATE-LIFECYCLE-001
title: Template Lifecycle Policy
version: 0.2.0
status: baseline
---

# Template Lifecycle Policy

## States

Template packages use:

- `draft`
- `baseline`
- `stable`
- `deprecated`
- `retired`

## Review triggers

Review a template when:

- governance changes
- a linked schema changes
- an incident exposes missing fields
- consumers repeatedly misuse a section
- a placeholder becomes ambiguous
- a decision vocabulary changes
- validation tooling changes
- a stable path must move
- a template is unused or superseded
- new legal, contractual, safety, or security obligations apply

## Change classes

### Patch

Editorial clarification with no semantic or placeholder change.

### Compatible minor change

Optional section, additional guidance, new optional placeholder, stricter validation of template-library structure, or improved example.

### Breaking change

Stable path move, placeholder rename, required section removal or addition, changed decision vocabulary, changed field meaning, or incompatible schema alignment.

## Deprecation

Deprecation requires:

- replacement template
- migration guide
- deprecation date
- support window
- consumer notice
- retirement criteria

## Ownership

Each package must have a maintainer or accountable owning role in the adopting organization.

## Evidence

Template changes should record:

- compatibility class
- affected packages
- validators run
- examples updated
- consumers considered
- checks not run
- reviewer
