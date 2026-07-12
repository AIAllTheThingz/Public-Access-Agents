---
id: FW-FASTAPI
title: FastAPI Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - fastapi
depends_on:
  - GOV-WORK
  - GOV-SECDEV
  - DISC-TEST
---
# FastAPI Agent Standard

## Requirements

### FASTAPI-MODEL-001

**Requirement:** Use explicit request and response models with validation and size limits.

### FASTAPI-AUTH-002

**Requirement:** Implement server-side authentication and authorization dependencies.

### FASTAPI-ASYNC-003

**Requirement:** Do not block the event loop with synchronous I/O in async paths.

### FASTAPI-ERROR-004

**Requirement:** Return safe consistent errors and preserve internal diagnostics.

### FASTAPI-TEST-005

**Requirement:** Test validation, dependency overrides, authorization, and integration behavior.

## Completion evidence

- Relevant framework tests
- Security-impact review
- Compatibility and migration notes
