---
id: GOV-SECDEV
title: Secure Development Policy
version: 0.1.0
status: baseline
applies_to:
  - all-projects
depends_on:
  - none
---
# Secure Development Policy

## Purpose

Integrates security activities into normal design, implementation, testing, delivery, and maintenance.

## Requirements

### GOV-SECDEV-001

**Requirement:** Define trust boundaries, sensitive data, identities, privileges, and external dependencies.

### GOV-SECDEV-002

**Requirement:** Use secure defaults, least privilege, explicit validation, and fail-safe behavior.

### GOV-SECDEV-003

**Requirement:** Treat authentication, authorization, secrets, cryptography, deserialization, file handling, command execution, and network boundaries as security-sensitive.

### GOV-SECDEV-004

**Requirement:** Run proportionate security validation before release.

### GOV-SECDEV-005

**Requirement:** Track known vulnerabilities and unsupported components.

## Minimum evidence

- Threat or abuse analysis
- Security test evidence
- Dependency review
- Residual-risk statement

## Exceptions

Use the documented exception process.
