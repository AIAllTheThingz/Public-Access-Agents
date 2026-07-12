---
id: EX-WRK-THREAT-001
title: Worker Service Composition Example Threat Model
version: 0.1.0
status: baseline
---
# Worker Service Composition Example Threat Model

## Purpose

This is an illustrative threat model. It contains no real system details and does not satisfy a production security review.

## Assets

- Message consumer
- Processing pipeline
- Integration adapters
- Checkpoint and retry handling
- credentials and secret references
- contracts and configuration
- logs, metrics, traces, and artifacts
- data described by the example

## Trust boundaries

- Message broker
- External APIs
- Configuration and secret providers
- Container and Kubernetes control planes

## Actors

- legitimate user or producer
- authenticated but unauthorized user
- anonymous or malicious client
- compromised dependency or build input
- operator with excessive privilege
- unavailable or misbehaving external service

## Abuse cases

- malformed or oversized input
- authorization bypass
- injection into queries, commands, templates, paths, or logs
- replay or duplicate processing
- secret disclosure
- resource exhaustion
- dependency substitution
- telemetry data leakage
- unsafe rollback or recovery

## Mitigations

- boundary validation
- server-side authorization
- parameterized APIs
- least privilege
- bounded retries and limits
- secure secret storage
- dependency and artifact verification
- safe errors and redacted telemetry
- negative and abuse-case tests
- reviewed rollout and recovery

## Residual risk

Actual residual risk cannot be assessed without the real architecture, data, identities, environments, dependencies, and operational model.
