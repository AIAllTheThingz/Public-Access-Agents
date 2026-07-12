---
id: BASH-PORT-001
status: baseline
title: Bash Portability Standard
---

# Shell Portability Standard

- Choose Bash or POSIX shell explicitly.
- Do not advertise `/bin/sh` compatibility while using Bash syntax.
- Avoid GNU-only options when portability is claimed unless guarded by capability checks.
- Account for filesystem, path, locale, newline, and command differences across supported systems.
- Document required operating systems and external command behavior.
