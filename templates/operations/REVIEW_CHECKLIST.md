---
id: TEMPLATE-REVIEW-OPERATIONS-001
title: Operational Runbook Review Checklist
version: 0.2.0
status: baseline
---

# Operational Runbook Review Checklist

## Identity

- Template type: `operational-runbook`
- Stable template: [`RUNBOOK_TEMPLATE.md`](RUNBOOK_TEMPLATE.md)
- Record reviewed:
- Reviewer:
- Review date:

## Template completion

- [ ] The correct template type was selected.
- [ ] Every allowed placeholder was replaced.
- [ ] No unknown project fact was invented.
- [ ] Required sections were preserved.
- [ ] Optional omissions are justified.
- [ ] Ownership and scope are explicit.
- [ ] Related evidence and decisions resolve.
- [ ] Review and approval roles are distinguished.
- [ ] No secret or sensitive production value is embedded.

## Content-specific review

- [ ] Diagnostics precede state-changing actions.
- [ ] Commands identify target and expected output.
- [ ] Privileged actions reference authorization.
- [ ] Stop and escalation criteria are explicit.
- [ ] Runbook ownership and review date are current.

## Validation

- [ ] Repository validation passed.
- [ ] Relative link validation passed.
- [ ] Template validation passed.
- [ ] Applicable schema validation passed.
- [ ] Checks not run are recorded.

## Decision

- [ ] Approved
- [ ] Approved with conditions
- [ ] Changes required
- [ ] Rejected

Conditions, findings, and limitations:
