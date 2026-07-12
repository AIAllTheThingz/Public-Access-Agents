---
id: EX-FULL-TEST-001
title: Full-Stack Web Application Composition Example Test Strategy
version: 0.1.0
status: baseline
---
# Full-Stack Web Application Composition Example Test Strategy

## Purpose

This test strategy demonstrates how validation is selected from risk and architecture rather than from habit.

## Objectives

- verify intended behavior
- reject invalid and unauthorized behavior
- exercise boundaries and failure paths
- prevent regression
- validate compatibility and packaging
- produce honest, reproducible evidence

## Proposed validation

- .NET restore, format, build, unit, integration, and contract tests
- Frontend frozen install, formatting, linting, type checking, tests, and build
- Accessibility keyboard, semantics, focus, contrast, and automated checks
- Database migration and rollback rehearsal
- Container, Kubernetes, security, and release-evidence checks

## Test levels

### Static and structural checks

- formatting
- linting or static analysis
- type checking where applicable
- manifest and configuration parsing
- dependency and secret checks
- repository link and identifier validation

### Unit and component tests

Cover business rules, validation, branching, errors, cancellation, retries, and deterministic transformations.

### Integration and contract tests

Exercise representative dependency behavior, schemas, authentication, timeouts, duplicate delivery, and failure responses without using production systems.

### End-to-end tests

Use only when the project has meaningful cross-component workflows that cannot be verified at lower levels.

### Non-functional tests

Select performance, accessibility, security, recovery, concurrency, or resilience tests according to actual risk.

## Negative cases

Include:

- missing and malformed input
- boundary and oversized values
- unauthorized or forbidden access
- timeout and cancellation
- dependency failure
- duplicate or reordered work
- partial success
- configuration failure
- unavailable resources
- unsafe path or command input where relevant

## Test data

Use synthetic data. Never copy production data into tests or examples.

## Evidence

Record:

- exact command
- result
- environment
- timestamps when available
- relevant output or artifact location
- limitations
- checks not run

## Completion rule

A passing happy-path test does not prove the system is complete. Completion requires the risk-proportionate set of tests, review, and explicit limitations.
