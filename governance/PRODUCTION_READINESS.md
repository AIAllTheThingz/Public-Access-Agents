---
id: GOV-PROD
title: Production Readiness
version: 0.2.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - GOV-CONTRACT
---

# Production Readiness

## Purpose

Defines minimum operational, security, support, recovery, and evidence gates before production use.

## Applicability

This policy applies to:

- new production systems, services, automations, data pipelines, infrastructure, and material production changes
- changes affecting deployment, data, dependencies, support, recovery, or public behavior

## Roles

- **Change owner:** assembles readiness evidence.
- **Operations or service owner:** accepts support and recovery responsibility.
- **Security, privacy, data, accessibility, or platform reviewers:** review applicable concerns.
- **Approver:** authorizes production use.

## Policy requirements

### GOV-PROD-001

**Requirement:** Document deployment, configuration, secrets, observability, support ownership, rollback, and recovery.

**Expected evidence:** Readiness record links each required plan.

### GOV-PROD-002

**Requirement:** Validate failure modes, dependency outages, resource limits, and data migration behavior as applicable.

**Expected evidence:** Representative failure and recovery evidence is recorded.

### GOV-PROD-003

**Requirement:** Define service-level objectives or operational expectations where applicable.

**Expected evidence:** Operational targets and ownership are documented.

### GOV-PROD-004

**Requirement:** Do not equate successful build or unit tests with production readiness.

**Expected evidence:** Readiness decision considers deployment and operations evidence.

### GOV-PROD-005

**Requirement:** Production configuration, identities, secrets, certificates, endpoints, quotas, and dependencies must be reviewed without committing sensitive values.

**Expected evidence:** Configuration review records sources and ownership.

### GOV-PROD-006

**Requirement:** Data migrations and irreversible changes require rehearsal, backup or recovery planning, and explicit go/no-go criteria.

**Expected evidence:** Migration and recovery evidence is linked.

### GOV-PROD-007

**Requirement:** Monitoring, alerting, dashboards, runbooks, escalation, and support ownership must be usable before production dependence.

**Expected evidence:** Operational readiness evidence identifies owners and tests.

### GOV-PROD-008

**Requirement:** Readiness approval applies to a defined artifact, configuration, environment, and change scope.

**Expected evidence:** Decision is traceable to the deployed candidate.

### GOV-PROD-009

**Requirement:** Known limitations and accepted residual risks must be visible to operators and approvers.

**Expected evidence:** Readiness record lists limitations, owners, and follow-up dates.

## Decision gates

- No production approval without deployment and recovery plans.
- No irreversible migration without tested recovery or accepted risk.
- No production-ready claim without operational owner and relevant evidence.

## Required records and evidence

- Deployment and rollback or roll-forward plan
- Monitoring and alerting plan
- Recovery and migration evidence
- Operational owner and escalation path
- Security and privacy review where applicable
- Artifact and configuration traceability
- Accepted limitations

## Exceptions and prohibited shortcuts

An exception may modify a readiness gate only with explicit risk acceptance, compensating controls, expiry, and accountable production approval.

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
