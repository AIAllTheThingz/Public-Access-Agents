---
id: PROFILE-LIFECYCLE-001
title: Project Profile Lifecycle
version: 0.2.0
status: baseline
---
# Project Profile Lifecycle

## Purpose

Defines creation, adoption, review, change, migration, and deprecation of profiles.

## States

- proposed
- baseline
- stable
- deprecated
- retired

## Adoption lifecycle

1. identify project shape
2. select primary and secondary profiles
3. classify risk
4. select packages
5. tailor decisions and evidence
6. add scoped instructions
7. validate
8. review and approve
9. operate and collect feedback
10. reassess after material change

## Reassessment triggers

- new interface
- new user type
- new deployment model
- new platform
- sensitive data
- privilege increase
- tenant introduction
- public release
- destructive automation
- AI tool use
- operational incident
- support ownership change
- end-of-support runtime
- repeated exceptions

## Profile change types

- editorial
- clarifying
- additive
- behavior-changing
- risk-changing
- breaking
- deprecating

## Migration requirements

Behavior-changing and breaking profile updates should identify:

- affected profile IDs and packages
- previous and new requirements
- adoption impact
- evidence changes
- compatibility period
- deprecated paths
- update examples
- re-review triggers

## Deprecation

A deprecated profile remains documented long enough for migration. Do not repurpose its ID for a different project shape.

## Completion

A profile lifecycle action is incomplete until canonical files, package directories, manifests, examples, links, and migration guidance agree.
