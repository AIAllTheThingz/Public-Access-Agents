---
id: TEMPLATE-THREAT-MODEL-001
title: Threat Model Template
version: 0.2.0
status: baseline
template_type: threat-model
---

# Threat Model Template

- Threat model ID: `{{MODEL_ID}}`
- Scope: {{SYSTEM_SCOPE}}
- Architecture reference: {{ARCHITECTURE_REFERENCE}}
- Owner: {{OWNER}}
- Reviewers: {{REVIEWERS}}
- Review date: `{{REVIEW_DATE}}`

## Assets

{{ASSETS}}

## Actors and trust levels

{{ACTORS_TRUST_LEVELS}}

Include expected users, services, administrators, tenants, external systems, malicious actors, and compromised identities.

## Entry points

{{ENTRY_POINTS}}

## Trust boundaries

{{TRUST_BOUNDARIES}}

## Sensitive data flows

{{SENSITIVE_DATA_FLOWS}}

## Abuse cases

| ID | Abuse case | Preconditions | Impact | Mitigation | Evidence | Residual risk | Owner |
|---|---|---|---|---|---|---|---|
{{ABUSE_CASE_ROWS}}

## Assumptions

{{ASSUMPTIONS}}

## Out-of-scope items

{{OUT_OF_SCOPE}}

Out-of-scope risk must have an owner and rationale.

## Required follow-up

{{FOLLOW_UP}}

## Revisit triggers

{{REVISIT_TRIGGERS}}
