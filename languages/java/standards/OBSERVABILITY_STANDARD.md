---
id: JAVA-OBS-001
status: baseline
title: Java Observability Standard
---

# Observability Standard

## Requirements

- Emit structured, actionable diagnostics at external and operational boundaries.
- Use consistent severity, event names, correlation identifiers, and redaction.
- Do not log secrets, tokens, private data, or unbounded payloads.
- Expose health, readiness, latency, error, and saturation signals for long-running services.
- Document expected failure signals and troubleshooting steps.
