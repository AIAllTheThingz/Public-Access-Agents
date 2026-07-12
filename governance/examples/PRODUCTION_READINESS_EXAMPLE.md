---
id: GOV-EX-PROD-001
title: Production Readiness Example
version: 0.2.0
status: baseline
---

# Production Readiness Example

## Fictitious candidate

A moderate-risk background service with an immutable artifact and a staged deployment.

## Readiness evidence

- reviewed configuration sources
- service account and permissions
- dependency timeouts and retries
- health, metrics, and alerts
- runbook and escalation
- resource limits
- rollback procedure
- failure-injection results
- artifact digest and source commit
- operational owner

## Decision

Ready with a condition that one non-critical dashboard is completed before general availability. The condition, owner, and due date are recorded.
