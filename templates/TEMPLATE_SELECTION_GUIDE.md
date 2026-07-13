---
id: TEMPLATE-SELECT-001
title: Template Selection Guide
version: 0.2.0
status: baseline
---

# Template Selection Guide

## Selection questions

Ask:

1. Is this an instruction, decision, evidence record, authorization, delivery plan, or operational procedure?
2. Does governance require a specific record?
3. Does a versioned schema apply?
4. Is the record human-readable, machine-readable, or both?
5. Who owns, reviews, approves, operates, and retains it?
6. What event makes it stale?
7. Which other records must be linked?

## Selection matrix

| Need | Primary template | Common companion templates |
|---|---|---|
| Repository-wide agent behavior | Root Agent Instructions | Project Manifest, Risk Assessment |
| Local agent behavior | Nested Agent Instructions | Root Agent Instructions |
| Consequential technical decision | Architecture Decision Record | Risk Assessment, Threat Model |
| Change-risk classification | Change Risk Assessment | Authorization, Recovery, Completion |
| Adversarial analysis | Threat Model | Architecture Decision, Risk Assessment |
| Temporary deviation | Standards Exception Record | Risk Assessment, Human Review |
| Work completion evidence | Completion Report | Test Evidence, Artifact Record |
| Machine-readable standards composition | Project Standards Manifest | Root Agent Instructions |
| Machine-readable test result | Test Evidence Record | Completion Report |
| Immutable artifact identity | Artifact Record | Release Plan, Completion Report |
| Consequential action authority | Change Authorization Record | Risk Assessment, Release Plan |
| Accountable review | Human Review Record | Any reviewed record |
| Production acceptance | Production Readiness Review | Risk, Threat, Release, Recovery |
| Coordinated deployment | Release Plan | Authorization, Artifact, Recovery |
| Failure reversal or restoration | Rollback and Recovery Plan | Release Plan, Runbook |
| Operator procedure | Operational Runbook | Authorization, Recovery |

## Common compositions

### Moderate-risk application change

```text
risk assessment
+ architecture decision when design changes
+ test evidence
+ completion report
```

### High-risk production change

```text
risk assessment
+ threat model when trust changes
+ change authorization
+ release plan
+ rollback and recovery plan
+ production readiness review
+ artifact and test evidence
+ completion report
```

### New repository adoption

```text
project manifest
+ root AGENTS.md
+ nested AGENTS.md where needed
+ architecture decisions
+ risk assessment
```

## Selection boundaries

Do not use:

- a completion report as authorization
- a review record as risk acceptance
- an ADR as a threat model
- a runbook as architecture documentation
- an exception record as permanent policy
- a release plan as recovery evidence
- a production-readiness review as implementation evidence

Distinct records exist because distinct decisions have distinct owners. Combining them all into “CHANGE_NOTES_FINAL_v7.md” does not simplify governance. It conceals it.
