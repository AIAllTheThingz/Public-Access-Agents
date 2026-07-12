---
id: GOV-CONTRACT
title: Organization Contract
version: 0.2.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - none
---

# Organization Contract

## Purpose

Defines the non-negotiable contract governing agent-assisted engineering work.

## Applicability

This policy applies to:

- every repository, project, change, review, automation, and generated artifact
- all human and automated contributors operating under these standards

## Roles

- **Accountable owner:** owns the system or change and accepts residual risk.
- **Implementer or agent:** performs work within authorized scope and reports evidence honestly.
- **Reviewer:** independently evaluates scope, risk, evidence, and unresolved limitations.
- **Approver:** has authority to authorize production, privileged, destructive, or externally visible action.

## Policy requirements

### GOV-CONTRACT-001

**Requirement:** Applicable legal, regulatory, contractual, safety, and security obligations take precedence over convenience.

**Expected evidence:** Document applicable obligations or state that they remain to be identified by the adopting organization.

### GOV-CONTRACT-002

**Requirement:** Agents must not invent approvals, test results, environments, credentials, or stakeholder decisions.

**Expected evidence:** Completion records distinguish verified facts, assumptions, not-run checks, and unresolved decisions.

### GOV-CONTRACT-003

**Requirement:** Modifying, destructive, externally visible, privileged, or production-affecting work must be explicitly authorized.

**Expected evidence:** Authorization record identifies scope, actor, target, time window, and approver.

### GOV-CONTRACT-004

**Requirement:** The accountable human owner remains responsible for accepting risk and approving production use.

**Expected evidence:** Approval evidence names the accountable role and accepted limitations.

### GOV-CONTRACT-005

**Requirement:** Standards may be strengthened locally but may not be silently weakened.

**Expected evidence:** Tailoring and exceptions record every material deviation.

### GOV-CONTRACT-006

**Requirement:** Authority, ownership, approval, and review roles must be explicit for moderate, high, and critical work.

**Expected evidence:** Role assignments appear in the change record or repository governance documentation.

### GOV-CONTRACT-007

**Requirement:** A lower-level instruction must not contradict a higher-precedence obligation without a documented resolution.

**Expected evidence:** Conflict record identifies the competing instructions and the controlling decision.

### GOV-CONTRACT-008

**Requirement:** No agent or tool may approve its own high-risk work or impersonate a human decision-maker.

**Expected evidence:** Approval originates from an accountable human identity acting through an approved governance or change-management system.

## Decision gates

- Stop when authorization is absent for state-changing or privileged work.
- Stop when controlling obligations conflict and no accountable decision exists.
- Stop when the requested action would require inventing identity, environment, approval, or evidence.

## Required records and evidence

- Applicable obligations and standards
- Accountable owner and reviewer roles
- Authorization for state-changing work
- Tailoring or exception records
- Residual-risk acceptance where required

## Exceptions and prohibited shortcuts

No exception may override law, safety obligations, or the requirement for genuine authorization and accountable human approval.

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
