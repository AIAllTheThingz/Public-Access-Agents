---
id: TEMPLATE-OPERATIONS-001
title: Operational Runbook Template
version: 0.2.0
status: baseline
template_type: operational-runbook
---

# Operational Runbook Template

- Runbook ID: `{{RUNBOOK_ID}}`
- System: {{SYSTEM}}
- Purpose: {{PURPOSE}}
- Owners: {{OWNERS}}
- Support hours: {{SUPPORT_HOURS}}
- Review date: `{{REVIEW_DATE}}`

## Prerequisites

{{PREREQUISITES}}

Never place credentials or private keys in the runbook.

## Health signals and expected state

{{HEALTH_SIGNALS}}

## Read-only diagnostic steps

{{DIAGNOSTIC_STEPS}}

For each step, identify the command, target, expected result, and interpretation.

## Authorized change procedures

{{CHANGE_PROCEDURES}}

State-changing procedures must reference authorization and include stop criteria.

## Recovery procedures

{{RECOVERY_PROCEDURES}}

## Stop criteria

{{STOP_CRITERIA}}

## Escalation and handoff

{{ESCALATION}}

## Required evidence

{{EVIDENCE}}

## Validation

{{VALIDATION}}
