---
id: GOV-OPERATE-001
title: Governance Operating Model
version: 0.2.0
status: baseline
---

# Governance Operating Model

## Purpose

Defines the roles, decisions, handoffs, and records required to operate the governance policies.

## Core roles

### Accountable owner

Owns the system or change, accepts residual risk, ensures resources exist, and remains accountable after approval.

### Requester

Defines desired outcome, business need, constraints, and urgency. Requesting work does not automatically authorize execution.

### Implementer or agent

Performs authorized work, controls scope, validates results, and reports evidence and limitations.

### Reviewer

Challenges assumptions, checks evidence, identifies defects, and confirms whether requirements are satisfied.

### Approver

Makes an authorized decision within delegated authority. Approval must identify scope, conditions, and limitations.

### Operator or service owner

Accepts support, monitoring, escalation, recovery, and ongoing operational responsibility.

### Specialist reviewer

Provides expertise for security, privacy, accessibility, data, legal, architecture, platform, reliability, or release concerns.

### Exception owner

Maintains compensating controls, expiry, remediation, and closure of a deviation.

## Separation of duties

Low-risk work may combine roles. High and critical work requires enough separation to prevent self-approval and challenge assumptions.

At minimum:

- the agent is not the human approver
- the requester is not the sole risk approver for high or critical work
- the implementer is not the only reviewer for high or critical work
- the exception requester is not the sole exception approver
- production readiness includes operational ownership

## Decision types

- authorization to investigate
- authorization to modify
- risk classification
- design approval
- exception approval
- merge or release approval
- production-readiness approval
- residual-risk acceptance
- vulnerability disclosure decision
- vulnerability closure
- policy change approval

## Decision records

Each decision should identify:

- decision type
- scope
- owner
- reviewer or approver
- evidence considered
- conditions
- limitations
- expiration or re-review trigger
- artifact or commit
- date or system record

## Escalation

Escalate when:

- authority is unclear
- obligations conflict
- risk exceeds delegated authority
- evidence is incomplete
- reviewer independence is insufficient
- rollback is unavailable
- a vulnerability creates urgent exposure
- an exception would exceed risk appetite
- production ownership is absent

## Operating metrics

Useful indicators include:

- exception age and recurrence
- high-risk changes without independent review
- changes reclassified after implementation
- not-run validation at approval
- expired risk acceptances
- production changes without rollback evidence
- vulnerability time to triage, contain, fix, and verify
- policy conflicts and unresolved ownership
- repeated AI-generated defects or unsupported dependencies

Metrics inform improvement. They are not proof that individual work is safe.
