---
id: RUST-SEC-001
status: baseline
title: Rust Security Standard
---

# Security Standard

- Treat input, deserialization, FFI, files, network data, process output, and dependencies as untrusted.
- Validate lengths, encodings, paths, integer conversions, and resource bounds.
- Review `unsafe`, build scripts, proc macros, and native dependencies as executable supply-chain code.
- Never commit or log secrets.
- Use maintained cryptographic libraries and secure transport defaults.
