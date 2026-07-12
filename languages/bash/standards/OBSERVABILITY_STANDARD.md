---
id: BASH-OBS-001
status: baseline
title: Bash Observability Standard
---

# Observability Standard

- Emit timestamped, severity-aware, actionable messages to the correct stream.
- Separate machine-readable output from diagnostic output.
- Use stable exit codes and summarize partial success accurately.
- Redact secrets and avoid unbounded command output.
- Record target, action, result, and correlation information without exposing sensitive data.
