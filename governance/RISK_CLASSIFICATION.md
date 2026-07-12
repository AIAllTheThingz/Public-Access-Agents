---
id: GOV-RISK
title: Risk Classification
version: 0.2.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - GOV-CONTRACT
---

# Risk Classification

## Purpose

Scales review, testing, authorization, and completion evidence to the potential impact of a change.

## Applicability

This policy applies to:

- every change before implementation
- reclassification when scope, exposure, or assumptions change

## Roles

- **Change owner:** proposes the classification and rationale.
- **Reviewer:** challenges factors and confirms required controls.
- **Risk acceptor:** approves high or critical residual risk.

## Policy requirements

### GOV-RISK-001

**Requirement:** Classify each change as low, moderate, high, or critical before implementation.

**Expected evidence:** Risk record includes level and rationale.

### GOV-RISK-002

**Requirement:** Consider data sensitivity, privilege, blast radius, reversibility, external exposure, availability, and safety.

**Expected evidence:** Risk factors are evaluated explicitly rather than inferred from change size.

### GOV-RISK-003

**Requirement:** High and critical changes require threat analysis, rollback planning, independent review, and explicit approval.

**Expected evidence:** Required high-risk records and approvals are linked.

### GOV-RISK-004

**Requirement:** Uncertain risk defaults to the higher plausible classification.

**Expected evidence:** Uncertainty and chosen conservative classification are documented.

### GOV-RISK-005

**Requirement:** Reassess risk when scope, architecture, data, privileges, dependencies, deployment targets, or rollback assumptions change.

**Expected evidence:** Updated classification is timestamped and reviewed.

### GOV-RISK-006

**Requirement:** Risk classification must control review depth, test scope, authorization, rollout, and evidence requirements.

**Expected evidence:** Change plan maps risk to controls.

### GOV-RISK-007

**Requirement:** Multiple individually small changes must be assessed for aggregate blast radius and interaction risk.

**Expected evidence:** Batch or release risk analysis covers cumulative effects.

### GOV-RISK-008

**Requirement:** Residual risk must identify an owner and acceptance authority.

**Expected evidence:** Risk acceptance record names the accountable role.

## Decision gates

- No implementation before classification unless the work is discovery-only and non-mutating.
- No high or critical execution without explicit approval.
- No closure while residual risk lacks an owner.

## Required records and evidence

- Risk level and rationale
- Factor analysis
- Required reviewers and approvers
- Validation and rollback requirements
- Residual-risk owner
- Reclassification history

## Exceptions and prohibited shortcuts

A risk exception may alter a control only through the exception process; it may not erase the underlying risk or its owner.

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
