---
id: FW-ASPNET
title: ASP.NET Core Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - aspnet-core
depends_on:
  - GOV-WORK
  - GOV-SECDEV
  - DISC-TEST
---
# ASP.NET Core Agent Standard

## Requirements

### ASPNET-CONFIG-001

**Requirement:** Use strongly typed validated configuration and keep secrets outside configuration files.

### ASPNET-AUTH-002

**Requirement:** Configure authentication and authorization explicitly; protect endpoints by default where appropriate.

### ASPNET-HTTP-003

**Requirement:** Use framework-provided encoding, antiforgery, HTTPS, rate limiting, and error handling features appropriately.

### ASPNET-DI-004

**Requirement:** Use dependency injection with clear lifetimes and avoid service-locator patterns.

### ASPNET-TEST-005

**Requirement:** Use unit and integration tests with representative hosting and middleware behavior.

## Completion evidence

- Relevant framework tests
- Security-impact review
- Compatibility and migration notes
