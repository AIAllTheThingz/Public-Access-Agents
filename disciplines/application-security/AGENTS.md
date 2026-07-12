---
id: DISC-SEC
title: Application Security Agent Standard
version: 0.2.0
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

This file defines mandatory agent behavior for work governed by the **Application Security** discipline.

Its objective is to turn security requirements into concrete design, implementation, verification, and vulnerability-management work.

> Make the smallest safe, reviewable, testable, and evidence-backed change that satisfies the requirement.

## Scope

This discipline applies to:

- authentication and authorization
- input validation and output encoding
- secret and key handling
- secure error behavior
- abuse resistance
- security testing and vulnerability remediation

## Instruction priority

When instructions conflict, apply them in this order:

1. explicit user requirements
2. the nearest more-specific `AGENTS.md`
3. this discipline `AGENTS.md`
4. the supporting standards in this package
5. repository conventions
6. general agent preferences

Do not resolve a material conflict silently. Follow the higher-priority instruction and report the conflict.

## Required supporting standards

Read every applicable supporting standard before implementation:

- [`standards/THREAT_MODELING_STANDARD.md`](standards/THREAT_MODELING_STANDARD.md)
- [`standards/AUTHENTICATION_AUTHORIZATION_STANDARD.md`](standards/AUTHENTICATION_AUTHORIZATION_STANDARD.md)
- [`standards/INPUT_OUTPUT_SECURITY_STANDARD.md`](standards/INPUT_OUTPUT_SECURITY_STANDARD.md)
- [`standards/SECRETS_CRYPTOGRAPHY_STANDARD.md`](standards/SECRETS_CRYPTOGRAPHY_STANDARD.md)
- [`standards/SECURITY_TESTING_STANDARD.md`](standards/SECURITY_TESTING_STANDARD.md)
- [`standards/VULNERABILITY_MANAGEMENT_STANDARD.md`](standards/VULNERABILITY_MANAGEMENT_STANDARD.md)
- [`standards/SECURE_OPERATIONS_STANDARD.md`](standards/SECURE_OPERATIONS_STANDARD.md)
- [`standards/COMPLETION_EVIDENCE.md`](standards/COMPLETION_EVIDENCE.md)

The supporting standards extend this file. This `AGENTS.md` takes precedence if wording conflicts.

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

## Non-negotiable behavior

- Inspect existing code, configuration, contracts, tests, documentation, ownership, and operational context before changing anything.
- Do not invent production values, identities, endpoints, schemas, credentials, infrastructure, legal obligations, or compatibility promises.
- Classify risk and identify trust boundaries, sensitive data, state changes, and reversibility.
- Default to safe, narrow, reversible behavior and stop when prerequisites or target identity are ambiguous.
- Do not weaken tests, security, privacy, accessibility, approvals, or evidence requirements to make work appear complete.
- Preserve public behavior unless change is explicitly authorized and migration or compatibility work is included.
- Keep examples fictitious and keep secrets and sensitive data out of source, tests, logs, errors, artifacts, and documentation.
- Record exact commands, results, limitations, assumptions, exceptions, and remaining risk.

## Required working method

1. Determine whether this discipline applies and document the reason.
2. Inspect the current implementation, contracts, evidence, and ownership.
3. Identify risk, trust boundaries, dependencies, failure modes, and affected users or operators.
4. Define acceptance criteria and required evidence before implementation.
5. Make the smallest coherent change.
6. Add or update tests, documentation, runbooks, contracts, diagrams, and evidence as applicable.
7. Run package-specific validation and review the final diff for unrelated or unsafe changes.
8. Report what changed, what was verified, what was not verified, and what risk remains.

## Completion gate

Do not report this discipline complete until:

- applicable mandatory rules are satisfied
- supporting standards were considered
- required evidence is recorded
- checks not run are identified
- limitations, assumptions, exceptions, and remaining risks are stated

## References

- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
