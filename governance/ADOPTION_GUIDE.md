---
id: GOV-ADOPT-001
title: Governance Adoption Guide
version: 0.2.0
status: baseline
---

# Governance Adoption Guide

## Purpose

This guide describes how an organization or repository can adopt the governance baseline without pretending that generic Markdown already knows its authority model, risk appetite, laws, tools, or operating environment.

## Adoption phases

### 1. Discovery

Identify:

- applicable obligations
- repository and system owners
- existing engineering, security, change, incident, and release processes
- current approval and exception mechanisms
- evidence systems
- record retention and access requirements
- gaps between current practice and the governance baseline

### 2. Authority design

Define:

- who may request work
- who may authorize modifying, privileged, destructive, or production actions
- who reviews each risk class
- who accepts residual risk
- who approves exceptions
- who owns production readiness
- who owns vulnerability intake and disclosure
- delegated authority and escalation boundaries

### 3. Risk tailoring

Map project and change characteristics to low, moderate, high, and critical risk. Define required reviewers, validation, threat analysis, rollback, rollout, and evidence for each level.

### 4. Record design

Choose where governance records live:

- pull requests
- issue trackers
- change-management systems
- security systems
- release systems
- artifact stores
- incident systems
- version-controlled records

Define retention, access, confidentiality, and traceability.

### 5. Workflow integration

Integrate governance into:

- planning
- issue templates
- pull requests
- branch protection
- CI
- release approvals
- deployment
- infrastructure changes
- exceptions
- incident response
- vulnerability handling
- post-incident follow-up

### 6. Pilot

Pilot on representative low-, moderate-, and high-risk changes. Measure friction, missing decisions, ambiguous roles, and evidence quality.

### 7. Approval and rollout

Obtain accountable approval for the tailored governance package. Publish effective date, ownership, support, migration, and training guidance.

### 8. Review

Review periodically and after:

- material incidents
- audit findings
- policy conflicts
- recurring exceptions
- major tool or platform changes
- organization changes
- regulatory or contractual changes
- AI-assistance model changes

## Tailoring requirements

Tailoring must:

- preserve stable rule references or document migration
- assign real roles
- define actual risk thresholds
- identify required records
- define approval authority
- disclose inapplicable controls with rationale
- preserve non-negotiable authorization, honesty, and accountability controls
- avoid embedding secrets or sensitive identifiers

## Adoption evidence

A completed adoption should include:

- governance owner
- approved policy set and version
- authority matrix
- risk matrix
- record locations
- review and approval workflows
- exception and vulnerability processes
- production-readiness gate
- training or communication record
- pilot evidence
- known gaps and remediation plan
