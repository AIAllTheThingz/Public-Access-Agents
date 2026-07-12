---
id: GOV-EX-MOD-001
title: Moderate-Risk Change Example
version: 0.2.0
status: baseline
---

# Moderate-Risk Change Example

## Fictitious change

Add a new API endpoint that reads non-sensitive operational data.

## Classification

- Risk: moderate
- External interface: yes
- Sensitive data: no
- Reversible: yes
- Production impact: possible

## Required governance

- independent code review
- API contract and negative tests
- authorization review
- observability review
- deployment and rollback plan
- completion evidence

## Decision

Approval applies to the reviewed commit and deployment candidate. Material contract or authorization change requires re-review.
