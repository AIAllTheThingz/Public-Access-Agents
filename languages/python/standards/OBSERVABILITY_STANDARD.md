---
id: PY-OBS-001
status: baseline
title: Python Observability Standard
---

# Observability Standard

## Requirements

- Emit structured, actionable diagnostics at external and operational boundaries.
- Use consistent severity, event names, correlation identifiers, and redaction.
- Do not log secrets, tokens, private data, or unbounded payloads.
- Expose health, readiness, latency, error, and saturation signals when the artifact is long-running.
- Document expected failure signals and troubleshooting steps.

## Evidence

Completion evidence must identify the files and checks that demonstrate these requirements. Exceptions must follow the repository exception process and must not be implied by omission.
