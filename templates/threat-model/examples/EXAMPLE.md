---
id: TEMPLATE-EX-THREAT-MODEL-001
title: Threat Model Example
version: 0.2.0
status: baseline
---

# Threat Model Example

- Threat model ID: `TM-EXAMPLE-001`
- Scope: Fictitious report-submission API
- Architecture reference: `docs/architecture/report-service.md`
- Owner: application security owner
- Reviewers: API owner, operations owner
- Review date: `2030-01-20`

## Assets

Job requests, service identities, report metadata, audit records.

## Actors and trust levels

Authenticated employees, worker service, administrators, compromised user accounts, and external attackers.

## Entry points

HTTPS API, message broker subscription, administrative replay command.

## Trust boundaries

Browser to API, API to broker, worker to data source, operator to replay command.

## Sensitive data flows

Asset identifiers flow through the broker; credentials remain in the workload-identity provider.

## Abuse cases

| ID | Abuse case | Preconditions | Impact | Mitigation | Evidence | Residual risk | Owner |
|---|---|---|---|---|---|---|---|
| TM-1 | Submit another department's report | Authenticated compromised user | Unauthorized data access | Object-level authorization | Negative authorization tests | Misclassified ownership data | API owner |
| TM-2 | Replay a privileged job | Operator access | Duplicate processing | Idempotency and approval | Replay test and audit record | Manual approval error | Operations owner |

## Assumptions

The identity provider supplies immutable subject identifiers.

## Out-of-scope items

Underlying provider compromise, owned by the platform threat model.

## Required follow-up

Add authorization tests and replay approval evidence.

## Revisit triggers

New public access, write actions, or cross-tenant reporting.
