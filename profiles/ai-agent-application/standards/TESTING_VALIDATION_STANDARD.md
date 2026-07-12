---
id: PROFILE-AI-AGENT-TEST-001
title: AI Agent Application Project Profile Testing and Validation Standard
version: 0.2.0
status: baseline
---
# Testing and Validation Standard

## Purpose

Define risk-based tests, negative behavior, representative environments, and exact completion evidence.

## Requirements

### AIAGENT-TEST-001

**Requirement:** Define test layers based on profile and risk.

**Expected evidence:** test strategy.

### AIAGENT-TEST-002

**Requirement:** Test public contracts and user-observable behavior.

**Expected evidence:** commands and results.

### AIAGENT-TEST-003

**Requirement:** Include negative, unauthorized, timeout, failure, recovery, and migration paths.

**Expected evidence:** negative and failure evidence.

### AIAGENT-TEST-004

**Requirement:** Use representative environments and data without exposing production information.

**Expected evidence:** environment details.

### AIAGENT-TEST-005

**Requirement:** Keep tests deterministic and repeatable where practical.

**Expected evidence:** coverage limitations.

### AIAGENT-TEST-006

**Requirement:** Record exact commands, outcomes, and checks not run.

**Expected evidence:** coverage limitations.

## Decision gate

Do not close this area while required evidence is missing or material uncertainty is concealed.

## Exceptions

Use the governance exception process. An exception does not erase the underlying risk or the need for an accountable owner.

## Completion boundary

The presence of this standard is not evidence that the requirement was implemented or validated.
