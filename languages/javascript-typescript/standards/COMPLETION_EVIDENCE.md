# JavaScript and TypeScript Completion Evidence Standard

## Purpose

This standard defines evidence required before JavaScript or TypeScript work is
considered complete.

The completion response must distinguish:

- Implemented
- Verified
- Assumed
- Not verified
- Not performed
- Remaining risk

## Required Completion Summary

## 1. Outcome

State:

- Completed
- Partially completed
- Blocked
- Not completed

Describe the requested outcome plainly.

## 2. Files Changed

List:

- Created
- Modified
- Deleted
- Generated
- Tests
- Documentation
- Package metadata
- Lockfiles
- Build configuration

Explain why each changed.

## 3. Behavior

Describe observable changes:

- Exports
- Routes
- Schemas
- Browser behavior
- Configuration
- Background work
- Errors
- Authorization
- Compatibility
- Breaking changes

## 4. Architecture

Report:

- New packages
- New application boundaries
- Module-format changes
- New framework or state management
- Background processing
- Messaging
- Caching
- ADRs
- Architectural limitations

## 5. Security

Report:

- Authentication
- Authorization
- Runtime validation
- Secret handling
- TLS
- CORS
- CSRF
- XSS controls
- Rate limiting
- Path restrictions
- Shell safety
- Dependency audit
- Source-map exposure

## 6. Dependencies

Report:

- Added
- Removed
- Updated
- Lockfile changes
- Lifecycle scripts
- Registry changes
- Direct and transitive advisories
- Runtime and package-manager changes

## 7. Documentation

Report updates to:

- README
- TSDoc/JSDoc
- API documentation
- Configuration reference
- ADRs
- Deployment guide
- Runbook
- Troubleshooting
- Comments

## 8. Commands Run

List exact material commands.

Typical sequence:

```bash
node --version
pnpm --version
pnpm install --frozen-lockfile
pnpm format:check
pnpm lint
pnpm typecheck
pnpm test
pnpm build
pnpm audit
pnpm pack --dry-run
```

Do not list commands that were not executed.

## 9. Validation Results

Report:

- Install
- Format
- Lint
- Typecheck
- Tests passed
- Tests failed
- Tests skipped
- Tests not run
- Coverage
- Build
- Package dry run
- Dependency audit
- Bundle or source-map review

## 10. Runtime and Environment

Report:

- Node.js version
- TypeScript version
- Package-manager version
- Operating system
- Architecture
- Test framework
- Browser versions
- Bundler
- External services

Do not imply validation on untested runtimes or browsers.

## 11. Assumptions

List material assumptions:

- Runtime
- Browser support
- Module system
- Deployment
- Authentication
- APIs
- Storage
- Scale
- Backward compatibility

## 12. Limitations and Not-Run Checks

For each item state:

- What was not run
- Why
- Remaining risk
- Required command or environment

## 13. Remaining Risks

Include:

- Untested browser
- Untested runtime
- External dependency
- Performance
- Concurrency
- Migration
- Security exception
- Existing lint finding
- Existing failing test
- Breaking-change impact
- Source-map or bundle concern

## 14. Diff Review

Confirm review for:

- Unrelated changes
- Secrets
- Debug output
- Placeholder values
- Temporary files
- Generated artifacts
- Package changes
- Lockfile changes
- Public-contract changes
- Documentation consistency
- Formatting churn
- Browser bundle exposure

## Completion Template

```markdown
# Completion Summary

## Outcome
Completed / Partially completed / Blocked

## Files Created
- `path`: Purpose

## Files Modified
- `path`: Purpose

## Files Deleted
- None

## Behavior
- Added:
- Changed:
- Preserved:
- Breaking changes:

## Architecture
- Changes:
- ADRs:

## Security
- Authentication:
- Authorization:
- Runtime validation:
- Secrets:
- Dependency audit:

## Dependencies
- Added:
- Removed:
- Updated:
- Lockfile:
- Lifecycle scripts:

## Documentation
- Updated:
- Not required:

## Validation Commands
```bash
<commands>
```

## Results
- Install:
- Format:
- Lint:
- Typecheck:
- Tests passed:
- Tests failed:
- Tests skipped:
- Build:
- Package:
- Audit:

## Runtime
- Node.js:
- TypeScript:
- Package manager:
- Operating system:
- Architecture:
- Test framework:
- Browsers:

## Assumptions
- None / list

## Limitations
- None / list

## Remaining Risks
- None / list

## Diff Review
- Unrelated changes: None found
- Secrets: None found
- Debug artifacts: None found
- Placeholder values: None found
- Lockfile surprises: None found
- Bundle exposure: None found
```

## Definition of Complete

Work is complete only when:

- Required behavior is implemented.
- Public contracts are intentionally preserved or changed.
- Security and runtime validation are satisfied.
- Documentation is current.
- Locked install, format, lint, typecheck, tests, build, and audit run where applicable.
- Package and bundle output are reviewed.
- Limitations are explicit.
- The final diff is reviewed.
- Completion evidence is accurate.

## Guiding Rule

> Report what was proven, identify what was not proven, and never replace evidence with confidence.
