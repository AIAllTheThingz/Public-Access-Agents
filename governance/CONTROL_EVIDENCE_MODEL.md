---
id: GOV-CONTROL-001
title: Governance Control and Evidence Model
version: 0.2.0
status: baseline
---

# Governance Control and Evidence Model

## Purpose

Defines the minimum structure of a governance control and the evidence needed to evaluate it.

## Control structure

A control should include:

- stable ID
- requirement
- purpose
- applicability
- accountable role
- evidence
- decision gate
- exception boundary
- review trigger
- lifecycle status

## Evidence qualities

Evidence should be:

- relevant
- attributable
- traceable to scope and artifact
- reproducible where practical
- timely
- protected from unauthorized alteration
- understandable by reviewers
- honest about limitations

## Evidence hierarchy

Stronger evidence often includes:

1. operational verification in the relevant environment
2. independent review of primary test and artifact evidence
3. successful representative integration or system tests
4. build, static-analysis, and unit-test output
5. design and review records
6. plans or assertions without execution

The appropriate evidence depends on the decision. A design record can prove a decision was made. It cannot prove recovery succeeded.

## Control states

- not assessed
- not applicable with rationale
- planned
- implemented
- validated
- partially validated
- reviewed
- approved
- excepted
- failed
- expired
- remediated
- retired

## Evidence anti-patterns

- screenshots without context
- copied output from another commit
- generated summaries without primary records
- green CI with skipped required tests
- scanner disappearance treated as remediation
- approval without reviewed scope
- exception without expiration
- policy text treated as operational implementation

## Record linkage

Governance records should link:

```text
request
-> risk
-> authorization
-> change
-> validation
-> review
-> approval
-> artifact
-> deployment
-> operational evidence
-> follow-up or closure
```
