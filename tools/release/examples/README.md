---
id: TOOL-RELEASE-EXAMPLES-001
title: Release Tool Examples
version: 1.0.0
status: baseline
---

# Release Tool Examples

## Validate the current release program

```bash
python tools/release/validate_release.py
```

## Validate a tag

```bash
python tools/release/validate_release.py --tag v0.9.0
```

## Build artifacts

```bash
python tools/release/build_release.py \
  --tag v0.9.0 \
  --output-dir dist
```

## Verify checksums

```bash
cd dist
sha256sum -c SHA256SUMS.txt
```

The commands are examples only. Tag creation and release publication require the review and authority defined in `MAINTAINERS.md` and `RELEASE_POLICY.md`.
