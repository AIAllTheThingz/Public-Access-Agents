---
id: GOV-EXCEPTION
title: Exception Process
version: 0.2.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - GOV-CONTRACT
---

# Exception Process

## Purpose

Provides a controlled, time-bounded path for temporary deviations from standards.

## Applicability

This policy applies to:

- every requested deviation from a normative rule
- renewals, extensions, compensating controls, and closure of prior exceptions

## Roles

- **Requester:** documents the need and proposed controls.
- **Rule owner or subject-matter reviewer:** evaluates impact.
- **Risk approver:** accepts the risk within delegated authority.
- **Exception owner:** tracks expiration and remediation.

## Policy requirements

### GOV-EXCEPTION-001

**Requirement:** Exceptions must identify the exact rule, business need, risk, compensating controls, owner, and expiration.

**Expected evidence:** Completed exception record contains every required field.

### GOV-EXCEPTION-002

**Requirement:** Exceptions must be approved by an accountable human with authority to accept the risk.

**Expected evidence:** Approval record identifies the approver and authority.

### GOV-EXCEPTION-003

**Requirement:** Exceptions must be time-bounded and reviewed before renewal.

**Expected evidence:** Expiration and review date are recorded.

### GOV-EXCEPTION-004

**Requirement:** An exception must not be used to conceal failed validation or missing authorization.

**Expected evidence:** Failed or not-run checks remain visible.

### GOV-EXCEPTION-005

**Requirement:** The requester must not be the sole approver for moderate, high, or critical exceptions.

**Expected evidence:** Independent approval is recorded.

### GOV-EXCEPTION-006

**Requirement:** Compensating controls must be testable, owned, and monitored for the life of the exception.

**Expected evidence:** Control evidence and owner are linked.

### GOV-EXCEPTION-007

**Requirement:** Expired exceptions become noncompliant until renewed or closed; expiration is not passive permission.

**Expected evidence:** Status transitions are recorded.

### GOV-EXCEPTION-008

**Requirement:** Renewal requires fresh rationale, risk assessment, control evidence, and remediation status.

**Expected evidence:** Renewal record is not a copied approval.

## Decision gates

- No use of an exception before approval.
- No renewal after expiration without fresh review.
- No closure until the deviation is removed or replaced by an approved permanent policy change.

## Required records and evidence

- Exception record
- Risk assessment
- Approval and authority
- Compensating-control evidence
- Expiration and review date
- Remediation or closure plan

## Exceptions and prohibited shortcuts

The exception process cannot waive legal or safety obligations, fabricate authorization, or permit an agent to approve its own exception.

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
