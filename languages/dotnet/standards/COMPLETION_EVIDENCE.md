# .NET Completion Evidence Standard

## Purpose

This standard defines evidence required before .NET work is considered complete.

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
- Migrations
- Tests
- Documentation
- Package configuration

Explain why each changed.

## 3. Behavior

Describe observable changes:

- Public API
- Routes
- Request or response schemas
- Status codes
- Configuration
- Data model
- Background jobs
- Logging and telemetry
- Error handling
- Authorization
- Compatibility
- Breaking changes

## 4. Architecture

Report:

- New projects
- Dependency-direction changes
- New abstractions
- New background processing
- New messaging
- New caching
- ADRs
- Architectural limitations

State when no architectural change occurred.

## 5. Security

Report applicable controls:

- Authentication
- Authorization
- Input validation
- Secret handling
- TLS
- CORS
- CSRF
- Rate limiting
- File-upload controls
- SQL parameterization
- Path boundaries
- Error redaction
- Dependency vulnerabilities

## 6. Data

Report:

- Schema changes
- Migrations
- Generated SQL review
- Transactions
- Concurrency
- Backfill
- Rollback
- Provider tested
- Production migration process

## 7. Dependencies

Report:

- Packages added
- Packages removed
- Package version changes
- Direct and transitive vulnerability findings
- Tool changes
- Workload changes
- Package-source changes

## 8. Documentation

Report updates to:

- README
- XML documentation
- OpenAPI
- Configuration reference
- ADRs
- Deployment guide
- Migration guide
- Runbook
- Troubleshooting
- Comments

## 9. Commands Run

List exact material commands.

Typical sequence:

```bash
dotnet --info
dotnet restore
dotnet format --verify-no-changes
dotnet build --no-restore
dotnet test --no-build
dotnet package list --vulnerable --include-transitive
dotnet publish --configuration Release --no-restore
```

Do not list commands that were not executed.

## 10. Build and Format Results

Report:

- Restore result
- Format result
- Build result
- Warning count
- Error count
- Configuration
- Target framework
- Runtime identifier when applicable

## 11. Test Results

Report:

- Test command
- Passed
- Failed
- Skipped
- Not run
- Test categories
- Coverage when collected
- Integration dependencies
- Flaky or quarantined tests

Do not say all tests passed without distinguishing skipped or excluded tests.

## 12. Runtime and Environment

Report:

- SDK version
- Runtime version
- Target framework
- Operating system
- Architecture
- Test framework
- Database provider
- Containers or external services
- Relevant tool versions

Do not imply validation on platforms not tested.

## 13. Assumptions

List material assumptions:

- Deployment
- Runtime
- Configuration
- Authentication
- Database
- External services
- Scale
- Platform
- Backward compatibility

## 14. Limitations and Not-Run Checks

For each item:

- What was not run
- Why
- Remaining risk
- Required command or environment

## 15. Remaining Risks

Include:

- Untested platform
- Untested migration
- External dependency
- Performance
- Concurrency
- Rollback
- Security exception
- Existing warning
- Existing failing test
- Breaking-change impact

## 16. Diff Review

Confirm review for:

- Unrelated changes
- Secrets
- Debug output
- Placeholder values
- Temporary files
- Generated artifacts
- Package changes
- Public-contract changes
- Migration safety
- Documentation consistency
- Formatting churn

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
- Validation:
- Secrets:
- Dependency audit:

## Data
- Migrations:
- Transactions:
- Concurrency:
- Rollback:

## Dependencies
- Added:
- Removed:
- Updated:
- Vulnerabilities:

## Documentation
- Updated:
- Not required:

## Validation Commands
```bash
<commands>
```

## Results
- Restore:
- Format:
- Build:
- Warnings:
- Tests passed:
- Tests failed:
- Tests skipped:
- Publish:
- Vulnerability audit:

## Runtime
- SDK:
- Target framework:
- Operating system:
- Architecture:
- Test framework:
- Database:

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
- Unreviewed migrations: None
```

## Definition of Complete

Work is complete only when:

- Required behavior is implemented.
- Public contracts are intentionally preserved or changed.
- Security controls are satisfied.
- Documentation is current.
- Restore, format, build, tests, and dependency audit are run where available.
- Data migrations are reviewed.
- Limitations are explicit.
- The final diff is reviewed.
- Completion evidence is accurate.

## Guiding Rule

> Report what was proven, identify what was not proven, and never replace evidence with confidence.
