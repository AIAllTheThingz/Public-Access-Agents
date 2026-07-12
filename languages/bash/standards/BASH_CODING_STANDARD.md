---
id: BASH-CODE-001
status: baseline
title: Bash Coding Standard
---

# Bash Coding Standard

- Use `#!/usr/bin/env bash` or an explicitly required absolute interpreter path.
- Use `set -o errexit`, `nounset`, and `pipefail` only with an understanding of their edge cases; do not treat them as a substitute for error handling.
- Quote parameter expansions unless intentional splitting or globbing is documented.
- Use arrays for argument lists and `printf` instead of ambiguous `echo` behavior.
- Use `[[ ... ]]` for Bash conditions and arithmetic contexts for numeric operations.
- Keep functions small, return meaningful status codes, and separate reusable output from user-facing formatting.
- Avoid parsing `ls` or human-formatted output.
- Avoid unrelated formatting and preserve calling contracts.
