---
id: TEMPLATE-EX-AUTHORIZATION-001
title: Change Authorization Record Example
version: 0.2.0
status: baseline
---

# Change Authorization Record Example

- Authorization ID: `AUTH-EXAMPLE-0042`
- Requester: application owner
- Implementer: operations engineer
- Approver: change authority
- Approval date: `2030-01-15`
- Valid from: `2030-01-20T02:00:00Z`
- Valid until: `2030-01-20T04:00:00Z`

## Target scope

Two named non-production worker instances.

## Allowed actions

Stop service, deploy reviewed artifact digest, start service, and run health validation.

## Prohibited actions

Database modification, production targets, identity changes, and unreviewed artifacts.

## Preconditions

Approved risk assessment, verified backup, artifact digest, and staffed escalation.

## Stop criteria

Unexpected target, failed backup check, health regression, or error rate above threshold.

## Required validation

Target identity, artifact digest, service health, logs, and functional smoke test.

## Recovery and escalation

Restore the previous artifact and escalate to the application owner.

## Required evidence

Command log, artifact record, validation output, and completion report.

## Boundary

The example is fictitious and grants no real authority.
