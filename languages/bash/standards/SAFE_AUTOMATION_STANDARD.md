---
id: BASH-SAFE-001
status: baseline
title: Bash Safe Automation Standard
---

# Safe Automation Standard

- Default to discovery and validation before mutation.
- Support dry-run or preview behavior for consequential changes.
- Use explicit allowlists and require authorization for destructive or bulk operations.
- Validate current state, perform the narrowest change, and verify resulting state.
- Use safe temporary directories, restrictive permissions, locks where needed, and traps for cleanup.
- Make reruns idempotent or document why they are not.
