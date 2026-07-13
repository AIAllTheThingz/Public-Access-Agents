---
id: TEMPLATE-RISK-001
title: Change Risk Assessment Template
version: 0.2.0
status: baseline
template_type: risk-assessment
---

# Change Risk Assessment Template

- Change ID: `{{CHANGE_ID}}`
- Summary: {{CHANGE_SUMMARY}}
- Classification: `{{RISK_LEVEL}}`
- Risk owner: {{RISK_OWNER}}
- Rollback required: `{{ROLLBACK_REQUIRED}}`

## Rationale

{{RISK_RATIONALE}}

## Risk factors

| Factor | Assessment |
|---|---|
| Data sensitivity | {{DATA_SENSITIVITY}} |
| Privilege | {{PRIVILEGE}} |
| External exposure | {{EXTERNAL_EXPOSURE}} |
| Blast radius | {{BLAST_RADIUS}} |
| Reversibility | {{REVERSIBILITY}} |
| Availability impact | {{AVAILABILITY_IMPACT}} |
| Safety impact | {{SAFETY_IMPACT}} |
| Dependency and supply-chain risk | {{DEPENDENCY_RISK}} |

## Required controls

{{REQUIRED_CONTROLS}}

Include required review, authorization, validation, rollout, observation, rollback, and evidence.

## Residual risk

{{RESIDUAL_RISK}}

## Reassessment triggers

{{REASSESSMENT_TRIGGERS}}

Risk must be reassessed when scope, data, privilege, target, dependency, rollout, or recovery assumptions change.
