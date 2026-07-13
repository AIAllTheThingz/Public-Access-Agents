---
id: TEMPLATE-EX-EXCEPTION-001
title: Standards Exception Record Example
version: 0.2.0
status: baseline
---

# Standards Exception Record Example

- Exception ID: `EXAMPLE-EXCEPTION-0042`
- Requested by: component owner
- Owner: dependency remediation owner
- Request date: `2030-01-10`
- Expiration date: `2030-03-31`
- Status: `requested`
- Rule ID: `SUPPLY-PIN-003`
- Normalized risk level: `moderate`

## Business need

A supported vendor integration temporarily requires an older pinned client.

## Risk introduced

The client lacks a non-exploitable maintenance fix and may become unsupported.

## Compensating controls

Restricted network path, additional logging, dependency monitoring, and a blocked public deployment.

## Scope

One non-production integration worker and one pinned package version.

## Validation and monitoring

Weekly advisory review and integration test on every dependency update.

## Remediation plan

Upgrade after the vendor compatibility release. Owner: dependency remediation owner.

## Approval

- Approver: fictitious risk approver
- Approval date: `not-approved`

## Closure evidence

`not-closed`

## Boundary

This is an illustrative request, not an approved exception.
