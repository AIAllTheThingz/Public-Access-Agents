---
id: TOOL-PKG-RELEASE-001
title: Repository Release Tool
version: 1.0.0
status: baseline
---

# Repository Release Tool

## Purpose

The release package validates repository release contracts and builds deterministic release artifacts.

It contains two executable entry points:

- [`validate_release.py`](validate_release.py)
- [`build_release.py`](build_release.py)

The release validator is part of the permanent read-only validation pipeline. The release builder writes artifacts only to an explicit output directory.

## Stable entry points

```text
tools/release/validate_release.py
tools/release/build_release.py
```

Moving or renaming these files requires migration guidance, tool-catalog updates, workflow updates, and compatibility review.

## Inputs

The tools read:

- `VERSION`
- `CHANGELOG.md`
- `RELEASE_POLICY.md`
- `MATURITY_POLICY.md`
- `releases/<VERSION>.md`
- `releases/migrations/<VERSION>.md`
- `.github/workflows/release.yml`
- Git-tracked repository files
- Git commit and tag metadata

## Validate a release program

```bash
python tools/release/validate_release.py
```

Validate a proposed tag:

```bash
python tools/release/validate_release.py --tag v0.9.0
```

Require the current commit to carry the matching tag:

```bash
python tools/release/validate_release.py \
  --tag v0.9.0 \
  --require-head-tag
```

## Build release artifacts

```bash
python tools/release/build_release.py \
  --tag v0.9.0 \
  --output-dir dist
```

The builder refuses to replace an existing output directory unless `--force` is supplied:

```bash
python tools/release/build_release.py \
  --tag v0.9.0 \
  --output-dir dist \
  --force
```

## Generated files

The output directory contains:

```text
Public-Access-Agents-<VERSION>.zip
Public-Access-Agents-<VERSION>.tar.gz
SHA256SUMS.txt
release-manifest.json
RELEASE_NOTES.md
MIGRATION_NOTES.md
```

## Determinism

Archives are generated from Git-tracked files in sorted path order.

The builder normalizes:

- ZIP timestamps
- TAR timestamps
- archive ownership metadata
- archive root names
- file ordering
- checksum ordering

The same source commit and tool version should produce identical archive contents. Compression-library or platform differences must be investigated before claiming byte-for-byte reproducibility across environments.

## Checksums

`SHA256SUMS.txt` contains SHA-256 digests for the ZIP and TAR.GZ archives.

Verify locally:

```bash
cd dist
sha256sum -c SHA256SUMS.txt
```

Checksums establish artifact integrity relative to the published digest. They do not establish that the repository content is correct or safe.

## Release manifest

`release-manifest.json` records:

- format version
- repository version
- tag
- source commit
- archive root
- tracked-file count
- artifact names
- artifact sizes
- artifact SHA-256 digests
- release-note filename
- migration-note filename
- checksum filename

## Exit behavior

`validate_release.py` follows the shared tool contract:

- `0`: validation passed
- `1`: validation completed with findings
- `2`: invalid input or missing dependency
- `3`: unexpected internal failure

`build_release.py` returns:

- `0`: artifacts built successfully
- `2`: invalid version, tag, source, output, or Git state

## Safety boundaries

- The validator is read-only except for an optional report file supplied through the shared tool contract.
- The builder writes only beneath the selected output directory.
- Existing output is not replaced without `--force`.
- Release archives contain Git-tracked files only.
- The tool performs no network access.
- The tool does not create or push tags.
- The tool does not publish GitHub Releases.
- The tool does not grant release authority.

## Tag boundary

The canonical tag is:

```text
v<VERSION>
```

A supplied tag that does not match `VERSION` is rejected.

The release workflow uses `--require-head-tag` so a GitHub Release cannot be built from a commit that lacks the expected tag.

## GitHub Release workflow

The workflow under `.github/workflows/release.yml`:

1. checks out the tagged commit
2. installs pinned validation dependencies
3. validates the full repository and unit tests
4. validates the tag against `VERSION`
5. builds artifacts
6. verifies checksums
7. creates the GitHub Release using the release-note file
8. attaches archives, checksums, release manifest, and migration notes

Prerelease tags are marked as GitHub prereleases.

## Tests

Focused tests live in:

```text
tools/tests/test_release.py
```

Run:

```bash
python -m unittest discover -s tools/tests -p "test_release.py"
```

Run the complete pipeline:

```bash
python tools/validate-all/run_all.py --include-tests
```

## Failure handling

If validation fails, correct the repository through a reviewed pull request before tagging.

If artifact generation fails after a tag exists:

- do not move the tag
- preserve logs
- correct the release machinery through review
- publish a corrective version or prerelease when required

If a GitHub Release is partially created, determine what became public before retrying.

## Compatibility

Backward-compatible changes may add optional result metadata or additional artifacts.

Breaking changes include:

- renaming entry points
- changing tag interpretation
- changing checksum format
- changing archive root or public artifact names
- removing manifest fields
- changing overwrite behavior
- changing which tracked files are included

## Review requirements

Changes to release validation, artifact generation, or the GitHub Release workflow require:

- Release Manager review
- Tooling or CI specialist review
- compatibility analysis
- security analysis
- permanent CI
- independent specialist review when required by `MAINTAINERS.md`

## Limitations

- Artifact checksums do not certify normative correctness.
- GitHub repository settings and token restrictions require separate administrative review.
- Signed tags depend on maintainer signing capability.
- The repository currently has one active maintainer.
- Pre-1.0 releases do not establish the final stable compatibility promise.

## Completion boundary

A successful release build proves that the reviewed source snapshot was packaged according to the implemented process. It does not prove that all packages are stable, all guidance is correct, or any adopting system is production-ready.
