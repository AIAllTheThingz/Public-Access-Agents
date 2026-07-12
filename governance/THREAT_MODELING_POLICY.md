---
id: GOV-THREAT
title: Threat Modeling Policy
version: 0.2.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - GOV-CONTRACT
---

# Threat Modeling Policy

## Purpose

Defines when, how, and by whom threat modeling is performed and maintained.

## Applicability

This policy applies to:

- new trust boundaries, sensitive data flows, privileged operations, public interfaces, material architecture changes, and high-risk integrations
- changes that invalidate existing threat assumptions or mitigations

## Roles

- **System or change owner:** owns the model and mitigation backlog.
- **Facilitator or security reviewer:** supports analysis proportional to risk.
- **Implementer:** turns mitigations into engineering requirements.
- **Risk acceptor:** owns residual threats.

## Policy requirements

### GOV-THREAT-001

**Requirement:** Threat modeling is required for new trust boundaries, sensitive data flows, privileged operations, public interfaces, and material architecture changes.

**Expected evidence:** Change record identifies whether threat modeling is required.

### GOV-THREAT-002

**Requirement:** Identify assets, actors, entry points, trust boundaries, abuse cases, mitigations, and residual risk.

**Expected evidence:** Threat model covers required elements.

### GOV-THREAT-003

**Requirement:** Threat models must be updated when architecture or assumptions change.

**Expected evidence:** Model version is traceable to current architecture.

### GOV-THREAT-004

**Requirement:** Threat models must produce actionable engineering requirements.

**Expected evidence:** Mitigations are assigned and tracked.

### GOV-THREAT-005

**Requirement:** The method may vary, but the model must be understandable, reviewable, and proportionate to risk.

**Expected evidence:** Method and scope are documented.

### GOV-THREAT-006

**Requirement:** Mitigations must identify status, owner, validation, and residual risk.

**Expected evidence:** Mitigation register is maintained.

### GOV-THREAT-007

**Requirement:** Accepted threats and deferred mitigations require accountable risk acceptance.

**Expected evidence:** Residual-risk decision is recorded.

### GOV-THREAT-008

**Requirement:** Threat-model review must include operational, supply-chain, identity, data, and abuse concerns where applicable.

**Expected evidence:** Review checklist covers relevant categories.

## Decision gates

- No high or critical design approval when required threat analysis is absent.
- No threat-model closure while material mitigations lack owners or decisions.
- No reuse of a stale model after material architecture change.

## Required records and evidence

- Threat-model document
- Architecture and data-flow references
- Mitigation register
- Validation evidence
- Residual-risk owner
- Review record

## Exceptions and prohibited shortcuts

A threat-model exception requires documented rationale, compensating analysis, risk approval, and expiration; it does not erase identified threats.

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
