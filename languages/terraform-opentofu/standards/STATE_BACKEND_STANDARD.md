---
id: TF-STATE-001
status: baseline
title: Terraform and OpenTofu State and Backend Standard
---

# State and Backend Standard

- Use a remote backend with locking and encryption for shared environments.
- Treat state as sensitive data and restrict access to the narrowest required identities.
- Never commit state or backend credentials.
- Document ownership, naming, backup, recovery, migration, and retention.
- Back up and test recovery before risky state operations.
- Use state surgery only as a controlled, reviewed recovery action with evidence.
