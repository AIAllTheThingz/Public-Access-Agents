---
id: JAVA-SEC-001
status: baseline
title: Java Security Standard
---

# Security Standard

## Requirements

- Treat external input, configuration, files, network responses, deserialization, and dependencies as untrusted.
- Use least privilege and secure defaults.
- Never commit secrets or expose them in logs, errors, examples, or test fixtures.
- Prevent injection with structured APIs and parameterization.
- Avoid unsafe native code, insecure deserialization, weak cryptography, and disabled TLS validation.
- Validate authentication and authorization at trust boundaries.
