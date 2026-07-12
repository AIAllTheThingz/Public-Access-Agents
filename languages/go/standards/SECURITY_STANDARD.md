---
id: GO-SEC-001
status: baseline
title: Go Security Standard
---

# Security Standard

- Treat input, configuration, files, network responses, templates, and dependencies as untrusted.
- Prevent command, path, template, SQL, and request injection with structured APIs and validation.
- Use secure TLS defaults and bounded network operations.
- Never log or commit secrets.
- Apply least privilege and explicit authorization at trust boundaries.
- Review uses of `unsafe`, cgo, reflection, and custom cryptography as high risk.
