---
id: BASH-DEP-001
status: baseline
title: Bash Dependency Management Standard
---

# Dependency Management Standard

- Document every required external command and minimum behavior or version.
- Detect prerequisites before mutation.
- Prefer broadly available interfaces when portability is claimed.
- Do not download tools at runtime without explicit authorization, integrity verification, and controlled installation.
- Pin container images, actions, or downloaded helper versions used by automation.
