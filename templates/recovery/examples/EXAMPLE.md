---
id: TEMPLATE-EX-RECOVERY-001
title: Rollback and Recovery Plan Example
version: 0.2.0
status: baseline
---

# Rollback and Recovery Plan Example

- Plan ID: `RECOVERY-EXAMPLE-0042`
- Scope: Fictitious worker deployment
- Recovery objectives: restore prior behavior within fifteen minutes with no job loss
- Authority: operations lead during the approved change window
- Most recent test: staging rehearsal on `2030-01-10`

## Failure scenarios

Worker fails health checks, queue depth grows, or duplicate processing appears.

## Prerequisites

Previous artifact digest, deployment access, queue visibility, and replay runbook.

## Trigger criteria

Two failed health checks or duplicate rate above the approved threshold.

## Rollback or reversal steps

Stop canary, deploy previous digest, restore previous retry configuration, restart, and verify.

## Restore, failover, compensation, or recreation steps

Replay only confirmed unprocessed messages using the approved replay tool.

## Validation

Health, queue stabilization, duplicate metric, sample report, and audit log.

## Stop and escalation criteria

Unknown message state, target mismatch, or failed rollback.

## Communication

Notify change authority and incident lead if recovery exceeds ten minutes.

## Evidence

Command log, metrics snapshot, artifact identity, and completion report.

## Boundary

This example is fictitious and does not prove the procedure works in any real environment.
