---
id: FW-SPRING
title: Spring Boot Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - spring-boot
depends_on:
  - GOV-WORK
  - GOV-SECDEV
  - DISC-TEST
---
# Spring Boot Agent Standard

## Requirements

### SPRING-CONFIG-001

**Requirement:** Use validated externalized configuration and approved secret management.

### SPRING-SEC-002

**Requirement:** Configure Spring Security explicitly and test authorization failures.

### SPRING-DATA-003

**Requirement:** Use parameterized data access, transactions, and migration tooling.

### SPRING-OBS-004

**Requirement:** Expose safe health and telemetry endpoints with appropriate protection.

### SPRING-TEST-005

**Requirement:** Use unit, slice, integration, and containerized dependency tests where appropriate.

## Completion evidence

- Relevant framework tests
- Security-impact review
- Compatibility and migration notes
