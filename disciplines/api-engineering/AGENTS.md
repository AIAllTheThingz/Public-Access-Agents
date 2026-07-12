---
id: DISC-API
title: API Engineering Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - api-engineering
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# API Engineering Agent Standard

## Purpose

Defines stable, secure, observable, and evolvable interfaces.

## Mandatory rules

### API-CONTRACT-001

**Requirement:** Define request, response, errors, authentication, authorization, pagination, limits, and versioning.

**Evidence:** Machine-readable contract and examples.

### API-VALIDATION-002

**Requirement:** Validate all externally supplied values and reject ambiguous or oversized input.

**Evidence:** Contract and negative tests.

### API-IDEMPOTENCY-003

**Requirement:** Define idempotency and retry semantics for mutating operations.

**Evidence:** Retry tests and documentation.

### API-COMPAT-004

**Requirement:** Treat compatibility as a release concern and document breaking changes.

**Evidence:** Compatibility report.

### API-OBS-005

**Requirement:** Emit correlation identifiers and useful metrics without leaking secrets.

**Evidence:** Telemetry evidence.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.

## References

- https://owasp.org/www-project-api-security/
