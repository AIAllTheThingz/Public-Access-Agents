---
id: GOV-EVIDENCE
title: Completion Evidence
version: 0.2.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - GOV-CONTRACT
---

# Completion Evidence

## Purpose

Defines evidence required before an agent or contributor may report work as complete.

## Applicability

This policy applies to:

- all completion claims, handoffs, reviews, releases, and production-readiness decisions
- partial and blocked work as well as successful work

## Roles

- **Implementer or agent:** records exact work and validation.
- **Reviewer:** checks evidence relevance, freshness, and limitations.
- **Approver:** accepts residual risk where required.

## Policy requirements

### GOV-EVIDENCE-001

**Requirement:** Completion claims must distinguish implemented, validated, partially validated, and not validated work.

**Expected evidence:** Completion status uses explicit states.

### GOV-EVIDENCE-002

**Requirement:** Evidence must include changed files, tests, static analysis, build results, security checks, and limitations as applicable.

**Expected evidence:** Completion record links exact evidence.

### GOV-EVIDENCE-003

**Requirement:** A passing command is evidence only for the behavior it actually exercises.

**Expected evidence:** Evidence description states scope and exclusions.

### GOV-EVIDENCE-004

**Requirement:** Unavailable tools or environments must be reported rather than simulated.

**Expected evidence:** Not-run checks include reasons and impact.

### GOV-EVIDENCE-005

**Requirement:** High-risk work requires rollback and human-review evidence.

**Expected evidence:** Rollback and review records are present.

### GOV-EVIDENCE-006

**Requirement:** Evidence must be attributable, reproducible where practical, and fresh enough for the decision being made.

**Expected evidence:** Records include source, environment, timestamp or run reference, and relevant version.

### GOV-EVIDENCE-007

**Requirement:** Generated summaries must not replace primary command output, test reports, review records, or artifact metadata.

**Expected evidence:** Primary evidence is retained or linked.

### GOV-EVIDENCE-008

**Requirement:** Known limitations, failed checks, partial success, and unverified behavior must be stated prominently.

**Expected evidence:** Completion record lists limitations and unresolved work.

### GOV-EVIDENCE-009

**Requirement:** Evidence from a different commit, artifact, environment, or configuration must not be presented as evidence for the current change without justification.

**Expected evidence:** Traceability connects evidence to the reviewed change.

## Decision gates

- No validated status without successful relevant validation.
- No production-ready status without production-readiness evidence.
- No high-risk completion without independent review and rollback evidence.

## Required records and evidence

- Machine-readable completion result where supported
- Command output or CI links
- Changed-file inventory
- Artifact and source-commit traceability
- Explicit unvalidated behavior
- Human review and approval records

## Exceptions and prohibited shortcuts

Evidence may be unavailable, but its absence must be visible and must reduce the completion status rather than being hidden.

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
