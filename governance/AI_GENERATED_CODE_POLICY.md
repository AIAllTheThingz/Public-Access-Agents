---
id: GOV-AI
title: AI-Generated Code Policy
version: 0.2.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - GOV-CONTRACT
---

# AI-Generated Code Policy

## Purpose

Defines responsibility, review, provenance, and validation expectations for work produced or modified by an AI system.

## Applicability

This policy applies to:

- AI-generated or AI-modified code, configuration, documentation, tests, schemas, infrastructure, and operational guidance
- AI-assisted reviews, migrations, dependency changes, and security recommendations

## Roles

- **Requester or operator:** controls scope and protects sensitive inputs.
- **Agent:** states assumptions, sources, limitations, and evidence honestly.
- **Human reviewer:** evaluates correctness, maintainability, security, licensing, and fit.
- **Accountable owner:** approves adoption and production use.

## Policy requirements

### GOV-AI-001

**Requirement:** AI-generated code is subject to the same or stricter review as human-written code.

**Expected evidence:** Review record identifies generated or materially assisted work.

### GOV-AI-002

**Requirement:** Generated dependencies, licenses, APIs, versions, and security claims must be verified.

**Expected evidence:** Primary source or repository evidence is recorded.

### GOV-AI-003

**Requirement:** Agents must not fabricate citations, changelogs, test results, or implementation status.

**Expected evidence:** Claims are traceable to sources or marked unverified.

### GOV-AI-004

**Requirement:** Security-sensitive generated code requires focused review and negative testing.

**Expected evidence:** Security review and adversarial tests are linked.

### GOV-AI-005

**Requirement:** The repository must remain maintainable by people who did not generate the code.

**Expected evidence:** Documentation, tests, naming, and architecture are understandable to non-authors.

### GOV-AI-006

**Requirement:** Sensitive, proprietary, personal, regulated, credential, and production data must not be supplied to an AI system without approved handling.

**Expected evidence:** Input-handling decision identifies permitted data classes.

### GOV-AI-007

**Requirement:** Generated output must be inspected for hidden assumptions, unsupported APIs, insecure defaults, unnecessary complexity, and invented environment details.

**Expected evidence:** Focused review checklist is completed.

### GOV-AI-008

**Requirement:** AI assistance must not obscure authorship, accountability, licensing obligations, or review responsibility.

**Expected evidence:** Change record identifies accountable humans and applicable provenance.

### GOV-AI-009

**Requirement:** An AI-generated test that only confirms the generated implementation is insufficient when independent behavior evidence is required.

**Expected evidence:** Tests include contract, negative, regression, or externally derived expectations as appropriate.

## Decision gates

- No acceptance of generated dependencies without verification.
- No security-sensitive merge without focused human review.
- No use of sensitive prompts or context outside approved handling.

## Required records and evidence

- Human review record
- Dependency and license verification
- Validation results
- Source and API verification
- Security-focused tests
- AI usage and data-handling disclosure where required

## Exceptions and prohibited shortcuts

AI use does not create an exception to security, privacy, licensing, human-review, or evidence requirements.

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
