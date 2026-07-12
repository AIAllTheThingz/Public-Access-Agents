---
id: GOV-DECISION-001
title: Governance Decision Matrix
version: 0.2.0
status: baseline
---

# Governance Decision Matrix

## Purpose

Provides a starting point for scaling governance decisions by risk. Adopting organizations must tailor authority and evidence.

| Control | Low | Moderate | High | Critical |
|---|---|---|---|---|
| Risk record | brief | required | detailed | detailed and independently reviewed |
| Independent review | optional by policy | normally required | required | multiple accountable reviewers |
| Threat analysis | if triggered | if triggered | required for material trust or security change | required |
| Rollback or recovery | proportionate | required for consequential change | reviewed and tested where practical | rehearsed or explicitly risk-accepted |
| Authorization | requester or delegated owner | delegated owner | accountable approver | highest applicable authority |
| Security validation | applicable checks | focused checks | focused negative and abuse testing | independent specialist validation |
| Production readiness | if production | required | cross-discipline review | formal go/no-go decision |
| Exception approval | owner | independent approver | risk authority | highest applicable authority |
| Evidence retention | normal | traceable | durable and reviewable | durable, access-controlled, and auditable |
| Rollout | normal | monitored | staged or canary where applicable | staged with explicit stop criteria |

## Reclassification triggers

Escalate risk when:

- privilege or data sensitivity increases
- blast radius expands
- rollback becomes uncertain
- public or customer behavior changes
- a production target is introduced
- a vulnerability or incident is involved
- the change becomes difficult to observe
- multiple changes interact
- evidence is weaker than planned

## Decision rule

When risk is uncertain, use the higher plausible class until evidence supports reduction.
