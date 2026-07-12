---
id: GOV-REVIEW
title: Human Review Policy
version: 0.2.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - GOV-CONTRACT
---

# Human Review Policy

## Purpose

Defines work that requires accountable human review, reviewer independence, and approval evidence.

## Applicability

This policy applies to:

- production, privileged, destructive, externally visible, security-sensitive, privacy-sensitive, high-risk, and contract-changing work
- exceptions, risk acceptance, and production-readiness decisions

## Roles

- **Author or agent:** provides reviewable scope and evidence.
- **Reviewer:** evaluates work and may request changes.
- **Approver:** authorizes the decision within delegated authority.
- **Accountable owner:** accepts remaining risk and operational responsibility.

## Policy requirements

### GOV-REVIEW-001

**Requirement:** Production changes, privileged actions, destructive operations, public interfaces, security controls, and sensitive-data handling require human review.

**Expected evidence:** Review record identifies reviewed scope.

### GOV-REVIEW-002

**Requirement:** Reviewers must be independent enough to challenge assumptions and evidence.

**Expected evidence:** Reviewer relationship and role are recorded where risk warrants.

### GOV-REVIEW-003

**Requirement:** Approval must identify what was reviewed and any accepted limitations.

**Expected evidence:** Approval record includes scope, evidence, conditions, and limitations.

### GOV-REVIEW-004

**Requirement:** Agents may recommend approval; they may not impersonate an approver.

**Expected evidence:** Approval originates from an accountable human acting through an approved governance or change-management system.

### GOV-REVIEW-005

**Requirement:** Reviewers must have appropriate competence for the risk and subject matter or obtain specialist input.

**Expected evidence:** Reviewer role or specialist participation is documented.

### GOV-REVIEW-006

**Requirement:** Self-review alone is insufficient for high and critical work.

**Expected evidence:** Independent reviewer or approval is recorded.

### GOV-REVIEW-007

**Requirement:** Approval expires when material scope, evidence, architecture, risk, artifact, or deployment conditions change.

**Expected evidence:** Re-review trigger and decision history are retained.

### GOV-REVIEW-008

**Requirement:** Requested changes, rejected evidence, and unresolved concerns must remain visible until resolved or explicitly accepted.

**Expected evidence:** Review conversation or decision record is preserved.

## Decision gates

- No required approval from an agent identity.
- No high-risk approval without competent independent review.
- No reuse of approval after material change without re-review.

## Required records and evidence

- Reviewer identity and role
- Reviewed scope and commit or artifact
- Evidence considered
- Approval, rejection, or requested changes
- Accepted limitations and conditions
- Re-review trigger

## Exceptions and prohibited shortcuts

Emergency handling may use expedited review, but retrospective review, authorization, and incident or change records remain required.

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
