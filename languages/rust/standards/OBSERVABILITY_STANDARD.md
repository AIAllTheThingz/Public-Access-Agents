---
id: RUST-OBS-001
status: baseline
title: Rust Observability Standard
---

# Observability Standard

- Emit structured diagnostics with consistent severity, event names, correlation, and redaction.
- Do not log secrets, private data, or unbounded payloads.
- Preserve error sources and useful context.
- Expose health, readiness, latency, error, and saturation signals for long-running services.
- Document expected failure signals and troubleshooting steps.
