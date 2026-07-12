---
id: GOV-LIFECYCLE-001
title: Governance Policy Lifecycle
version: 0.2.0
status: baseline
---

# Governance Policy Lifecycle

## Purpose

Defines how governance policies are proposed, reviewed, versioned, approved, published, migrated, deprecated, and retired.

## Change classes

- **Editorial:** grammar or formatting with no semantic change.
- **Clarifying:** resolves ambiguity without changing expected behavior.
- **Additive:** introduces new requirements or records.
- **Behavior-changing:** changes required decisions, evidence, or controls.
- **Breaking:** invalidates existing references, approvals, exceptions, or adoption assumptions.
- **Emergency:** urgent temporary change with expedited review and mandatory follow-up.

## Lifecycle

1. Proposal
2. Impact analysis
3. Draft
4. Review
5. Approval
6. Publication
7. Adoption or migration
8. Monitoring
9. Periodic review
10. Deprecation or retirement

## Impact analysis

Evaluate:

- affected rule IDs
- dependent packages and examples
- existing approvals and exceptions
- automation and schemas
- training and communication
- compatibility and migration
- effective date
- transition period
- enforcement changes

## Versioning

- Preserve rule IDs when meaning remains compatible.
- Add IDs for new requirements.
- Deprecate IDs when replacement is required.
- Do not silently repurpose an ID.
- Record migration when evidence, templates, or automation change.

## Review triggers

Review a policy after:

- material incident or vulnerability
- recurring exception
- audit finding
- legal or contractual change
- major technology or operating-model change
- governance conflict
- evidence-quality failure
- periodic review date

## Emergency changes

Emergency policy changes require:

- reason
- authorized owner
- effective scope
- temporary controls
- communication
- expiration or follow-up review
- retrospective confirmation or rollback

## Retirement

A retired policy requires:

- replacement or rationale
- migration guidance
- treatment of historical records
- reference updates
- effective date
- approval
