---
id: GOV-EX-ADOPT-001
title: Governance Adoption Example
version: 0.2.0
status: baseline
---

# Governance Adoption Example

## Fictitious context

A fictional engineering organization adopts this governance baseline for repositories containing internal tools and public services.

## Tailoring decisions

- Low-risk documentation changes may use author review.
- Moderate changes require one independent reviewer.
- High changes require independent technical review, rollback evidence, and accountable approval.
- Critical changes require specialist review and executive or delegated risk authority.
- Production deployments require an operational owner.
- Exceptions expire within a defined organization-specific period.
- Vulnerability records are access-controlled.

## Integration

- Risk and evidence are recorded in pull requests.
- Production authorization is recorded in a change system.
- Exceptions are tracked in an issue system with expiration alerts.
- Vulnerabilities are handled in a restricted security system.
- Release artifacts retain source and validation references.

## What remains unresolved

- Exact delegated authority
- Record retention
- Specialist-review thresholds
- Emergency change procedure
- Organization-specific legal obligations

This example is not an approved governance model. It demonstrates the decisions an adoption must make.
