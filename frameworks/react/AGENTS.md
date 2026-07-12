---
id: FW-REACT
title: React Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - react
depends_on:
  - GOV-WORK
  - GOV-SECDEV
  - DISC-TEST
---
# React Agent Standard

## Requirements

### REACT-STATE-001

**Requirement:** Keep state ownership clear and avoid duplicating derived state.

### REACT-A11Y-002

**Requirement:** Use semantic HTML and verify keyboard, focus, labels, and announcements.

### REACT-SEC-003

**Requirement:** Do not inject untrusted HTML; treat client-side checks as usability only.

### REACT-PERF-004

**Requirement:** Measure before adding memoization or complex performance patterns.

### REACT-TEST-005

**Requirement:** Test user-observable behavior rather than implementation details.

## Completion evidence

- Relevant framework tests
- Security-impact review
- Compatibility and migration notes
