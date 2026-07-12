---
id: GOV-SECDEV
title: Secure Development Policy
version: 0.2.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - GOV-CONTRACT
---

# Secure Development Policy

## Purpose

Integrates security into design, implementation, testing, delivery, maintenance, and retirement.

## Applicability

This policy applies to:

- all software, scripts, infrastructure, data processing, integrations, configuration, and build systems
- changes involving trust boundaries, identity, secrets, public interfaces, privileged actions, dependencies, or sensitive data

## Roles

- **Engineering owner:** ensures security work is planned and implemented.
- **Security reviewer:** provides specialist review where risk requires.
- **Implementer or agent:** applies secure defaults and records evidence.
- **Risk acceptor:** owns residual security risk.

## Policy requirements

### GOV-SECDEV-001

**Requirement:** Define trust boundaries, sensitive data, identities, privileges, and external dependencies.

**Expected evidence:** Architecture or threat documentation identifies each boundary.

### GOV-SECDEV-002

**Requirement:** Use secure defaults, least privilege, explicit validation, and fail-safe behavior.

**Expected evidence:** Configuration and tests demonstrate secure behavior.

### GOV-SECDEV-003

**Requirement:** Treat authentication, authorization, secrets, cryptography, deserialization, file handling, command execution, and network boundaries as security-sensitive.

**Expected evidence:** Focused review covers applicable sensitive areas.

### GOV-SECDEV-004

**Requirement:** Run proportionate security validation before release.

**Expected evidence:** Security checks and negative tests are recorded.

### GOV-SECDEV-005

**Requirement:** Track known vulnerabilities and unsupported components.

**Expected evidence:** Dependency and vulnerability records identify status and owner.

### GOV-SECDEV-006

**Requirement:** Security requirements must be derived from risk, threat analysis, data classification, architecture, and operating context.

**Expected evidence:** Security acceptance criteria are traceable to identified risks.

### GOV-SECDEV-007

**Requirement:** Secrets must be stored, accessed, rotated, logged, and revoked through approved mechanisms.

**Expected evidence:** Secret-handling design and access review are recorded without exposing values.

### GOV-SECDEV-008

**Requirement:** Security logging and diagnostics must support investigation without leaking secrets or unnecessarily sensitive data.

**Expected evidence:** Telemetry review verifies content and access.

### GOV-SECDEV-009

**Requirement:** Unsupported, unmaintained, or end-of-life components require remediation or an approved exception.

**Expected evidence:** Lifecycle status and decision are recorded.

### GOV-SECDEV-010

**Requirement:** Residual security risk must be explicit, owned, and accepted at the appropriate authority level.

**Expected evidence:** Risk acceptance names owner and expiration or review date.

## Decision gates

- No security-sensitive release without proportionate validation.
- No unknown trust boundary for high or critical work.
- No unsupported critical component without remediation or approved exception.

## Required records and evidence

- Threat or abuse analysis
- Security acceptance criteria
- Negative and abuse-case tests
- Dependency, secret, and configuration review
- Vulnerability status
- Residual-risk statement and owner

## Exceptions and prohibited shortcuts

Security exceptions must identify exact controls, compensating measures, monitoring, owner, approval, and expiration.

An approved exception must follow [EXCEPTION_PROCESS.md](EXCEPTION_PROCESS.md). Failed or unavailable validation must remain visible.

## Review triggers

Re-review this policy decision when scope, risk, architecture, data, privilege, environment, evidence, owner, approver, artifact, or assumptions change materially.

## Related governance

- [Organization Contract](ORGANIZATION_CONTRACT.md)
- [Agent Working Method](AGENT_WORKING_METHOD.md)
- [Risk Classification](RISK_CLASSIFICATION.md)
- [Completion Evidence](COMPLETION_EVIDENCE.md)
- [Human Review Policy](HUMAN_REVIEW_POLICY.md)
- [Exception Process](EXCEPTION_PROCESS.md)

## Completion boundary

Compliance with this policy is not established by the presence of this file. The adopting repository must implement, validate, review, and record the applicable controls.
