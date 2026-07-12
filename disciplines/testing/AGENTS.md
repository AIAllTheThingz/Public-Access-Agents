---
id: DISC-TEST
title: Testing and Quality Engineering Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - testing
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Testing and Quality Engineering Agent Standard

## Purpose

Requires tests that provide meaningful evidence rather than ceremonial coverage.

## Mandatory rules

### TEST-STRATEGY-001

**Requirement:** Define the test levels required by risk: unit, component, integration, contract, end-to-end, security, performance, and recovery.

**Evidence:** Test strategy mapped to risk.

### TEST-NEGATIVE-002

**Requirement:** Test invalid, unauthorized, boundary, timeout, and failure behavior.

**Evidence:** Negative test results.

### TEST-ISOLATION-003

**Requirement:** Keep tests deterministic, independently runnable, and isolated from uncontrolled external state.

**Evidence:** Repeatable test execution.

### TEST-REGRESSION-004

**Requirement:** Add regression tests for fixed defects where practical.

**Evidence:** Fail-before/pass-after evidence.

### TEST-QUALITY-005

**Requirement:** Do not weaken assertions or skip tests to make a pipeline pass.

**Evidence:** Diff and test review.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.
