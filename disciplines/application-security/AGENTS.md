---
id: DISC-SEC
title: Application Security Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - application-security
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Application Security Agent Standard

## Purpose

Turns security requirements into implementation and verification work.

## Mandatory rules

### SEC-INPUT-001

**Requirement:** Validate untrusted input at the trust boundary using explicit allowlists, size limits, type checks, and canonicalization where applicable.

**Evidence:** Tests for valid, invalid, boundary, and adversarial input.

### SEC-AUTHZ-002

**Requirement:** Enforce authorization server-side for every protected operation and object.

**Evidence:** Positive and negative authorization tests.

### SEC-SECRETS-003

**Requirement:** Keep secrets out of source, logs, errors, artifacts, and client-delivered code.

**Evidence:** Secret scan and configuration review.

### SEC-INJECTION-004

**Requirement:** Use parameterized APIs and avoid constructing commands, queries, templates, or paths from untrusted strings.

**Evidence:** Static review and injection-focused tests.

### SEC-ERRORS-005

**Requirement:** Return safe errors to callers while preserving actionable internal diagnostics.

**Evidence:** Error-path tests and log review.

### SEC-ABUSE-006

**Requirement:** Identify abuse cases, rate limits, resource exhaustion, and automation risks.

**Evidence:** Abuse-case test evidence.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.

## References

- https://owasp.org/www-project-application-security-verification-standard/
- https://cheatsheetseries.owasp.org/
