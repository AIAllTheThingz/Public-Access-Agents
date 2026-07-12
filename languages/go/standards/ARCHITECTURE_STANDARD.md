---
id: GO-ARCH-001
status: baseline
title: Go Architecture Standard
---

# Architecture Standard

- Keep package boundaries aligned to cohesive responsibilities.
- Separate domain logic from transport, storage, process, and vendor integrations.
- Avoid cyclic conceptual dependencies even when package cycles are prevented by the compiler.
- Keep public interfaces narrow and stable.
- Document material tradeoffs and deployment assumptions.
