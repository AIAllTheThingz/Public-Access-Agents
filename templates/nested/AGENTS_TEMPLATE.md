---
id: TEMPLATE-NESTED-001
title: Nested Agent Instructions Template
version: 0.2.0
status: baseline
template_type: nested-agents
---

# Nested Agent Instructions Template

## Template metadata

- Template ID: `TEMPLATE-NESTED-AGENTS-001`
- Template version: `0.2.0`
- Intended destination: `{{SCOPE_PATH}}/AGENTS.md`

> Replace every documented placeholder before adoption. Remove this note after validation.

## Scope

- Scope name: `{{SCOPE_NAME}}`
- Directory: `{{SCOPE_PATH}}`
- Responsibilities: {{SCOPE_RESPONSIBILITIES}}
- Local owners: {{LOCAL_OWNERS}}

These instructions apply only within this directory and its descendants.

## Parent instructions

All parent `AGENTS.md` files and selected shared standards remain applicable.

This file may add stricter or more-specific requirements. It must not silently weaken governance, authorization, security, compatibility, evidence, or review controls.

## Additional requirements

{{ADDITIONAL_REQUIREMENTS}}

## Prohibited local actions

{{PROHIBITED_LOCAL_ACTIONS}}

## Required local validation

{{LOCAL_VALIDATION_COMMANDS}}

Validation must target the actual files and behavior controlled by this scope.

## Local evidence

Required evidence:

{{LOCAL_EVIDENCE}}

## Escalation

Escalate through:

{{ESCALATION_PATH}}

Stop rather than guessing when local instructions conflict with parent authority, required facts are unavailable, or scope exceeds authorization.
