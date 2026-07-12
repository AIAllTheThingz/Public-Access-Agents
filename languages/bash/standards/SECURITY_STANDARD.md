---
id: BASH-SEC-001
status: baseline
title: Bash Security Standard
---

# Security Standard

- Treat parameters, environment variables, filenames, command output, archives, and downloaded content as untrusted.
- Prevent command, argument, path, glob, option, and temporary-file injection.
- Use `--` before untrusted positional arguments where supported.
- Never use `eval` or execute downloaded content directly.
- Verify downloads and use secure TLS defaults.
- Do not expose secrets through command lines, process listings, logs, traces, or temporary files.
