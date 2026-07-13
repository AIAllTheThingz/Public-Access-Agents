---
id: TEMPLATE-EX-OPERATIONS-001
title: Operational Runbook Example
version: 0.2.0
status: baseline
---

# Operational Runbook Example

- Runbook ID: `RUNBOOK-EXAMPLE-0042`
- System: Fictitious report worker
- Purpose: Diagnose delayed jobs and safely restart a non-production worker
- Owners: operations owner, application owner
- Support hours: business hours with on-call escalation
- Review date: `2030-04-01`

## Prerequisites

Read-only dashboard access, approved restart authorization, and target inventory.

## Health signals and expected state

Queue depth below threshold, heartbeat within two minutes, and no dead-letter growth.

## Read-only diagnostic steps

1. Confirm environment and worker identity.
2. Review queue depth and oldest-message age.
3. Review worker heartbeat and recent errors.
4. Confirm dependency health.

## Authorized change procedures

Restart only the named non-production worker after authorization.

## Recovery procedures

If restart fails, restore the previous artifact and escalate.

## Stop criteria

Target mismatch, production target, unavailable rollback artifact, or unknown message state.

## Escalation and handoff

Operations lead, then application owner, then incident lead.

## Required evidence

Target, timestamps, commands, outputs, authorization, and validation.

## Validation

Heartbeat, queue movement, functional sample, and error-rate check.

## Boundary

No credentials or real infrastructure identifiers are included.
