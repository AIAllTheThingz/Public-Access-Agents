---
id: GOV-WORK
title: Agent Working Method
version: 0.2.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - GOV-CONTRACT
---

# Agent Working Method

## Purpose

Defines the required sequence for discovery, planning, implementation, validation, and reporting.

## Applicability

This policy applies to:

- all engineering changes, reviews, investigations, documentation changes, and automation work
- both code-producing and non-code-producing agents

## Roles

- **Requester:** states the desired outcome and explicit constraints.
- **Implementer or agent:** discovers context, controls scope, validates work, and reports evidence.
- **Reviewer:** checks assumptions, risk, scope, validation, and completion claims.

## Policy requirements

### GOV-WORK-001

**Requirement:** Inspect repository instructions, architecture, tests, dependencies, and affected code before editing.

**Expected evidence:** Discovery record lists instructions and relevant files inspected.

### GOV-WORK-002

**Requirement:** State assumptions and resolve material uncertainty before high-risk implementation.

**Expected evidence:** Assumptions and unresolved questions are recorded before execution.

### GOV-WORK-003

**Requirement:** Make the smallest coherent change and avoid unrelated refactoring.

**Expected evidence:** Diff review confirms scope and identifies intentionally related changes.

### GOV-WORK-004

**Requirement:** Implement in safe phases: discovery, validation, simulation where applicable, reporting, then execution.

**Expected evidence:** Work record shows which phases were performed and why any phase was inapplicable.

### GOV-WORK-005

**Requirement:** Run relevant validation and report failures honestly.

**Expected evidence:** Exact commands, environments, results, and failure details are recorded.

### GOV-WORK-006

**Requirement:** Do not claim completion until required evidence exists.

**Expected evidence:** Completion result is linked to validation and review evidence.

### GOV-WORK-007

**Requirement:** Classify change type, risk, affected contracts, and required reviewers before implementation.

**Expected evidence:** Change plan identifies risk and acceptance criteria.

### GOV-WORK-008

**Requirement:** Define rollback, roll-forward, or recovery expectations before consequential mutation.

**Expected evidence:** Recovery plan is reviewed before execution.

### GOV-WORK-009

**Requirement:** Stop when prerequisites, target identity, authorization, or safe validation are missing.

**Expected evidence:** Stop condition is recorded rather than bypassed.

### GOV-WORK-010

**Requirement:** Review the final diff for unrelated changes, secrets, unsafe defaults, compatibility regressions, and false completion claims.

**Expected evidence:** Final diff review appears in completion evidence.

## Decision gates

- Discovery complete before planning.
- Risk and acceptance criteria defined before implementation.
- Validation complete before completion reporting.
- Authorization and rollback readiness confirmed before consequential execution.

## Required records and evidence

- Scope statement
- Files and instructions inspected
- Risk and acceptance criteria
- Implementation plan
- Validation commands and results
- Final diff review
- Limitations and remaining risks

## Exceptions and prohibited shortcuts

Urgency may shorten ceremony but does not permit fabricated evidence, missing authorization, or concealed risk.

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
