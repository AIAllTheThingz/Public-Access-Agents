# PowerShell Documentation Standard

## Purpose

This standard defines documentation and code-comment requirements for PowerShell 7.x scripts, modules, functions, tests, and supporting repository documents.

Documentation must help a qualified administrator or developer understand:

- What the code does
- Why it exists
- How to use it
- What it changes
- What it depends on
- How it fails
- How to validate it
- How to maintain it safely

Comments are part of the implementation and must remain accurate.

## General Documentation Principles

Documentation must be:

- Accurate
- Current
- Specific
- Actionable
- Safe
- Appropriate for the intended audience
- Free of secrets and production-sensitive details
- Consistent with actual parameters and behavior

Avoid:

- Marketing language
- Unsupported claims
- Vague statements such as "handles errors"
- Instructions that omit required prerequisites
- Examples that use real production values
- Comments that merely restate obvious syntax
- Large blocks of commented-out code
- Documentation copied from another project without verification

## Required Documentation Levels

Documentation requirements apply at several levels:

1. Repository documentation
2. Script and module headers
3. Public function comment-based help
4. Private function documentation
5. Inline code comments
6. Configuration documentation
7. Test documentation
8. Completion evidence

Each level serves a different purpose and should not duplicate every other level.

## Repository Documentation

A repository containing PowerShell code should document, where applicable:

- Purpose and supported use cases
- PowerShell minimum version
- Supported operating systems
- Installation or deployment steps
- Required modules and dependencies
- Configuration method
- Credential and secret-management expectations
- Required privileges
- Basic usage examples
- Safety behavior
- `-WhatIf` and `-Confirm` behavior
- Test and validation commands
- Logging and report locations
- Known limitations
- Troubleshooting
- Upgrade or migration notes
- Exit codes for standalone automation scripts

The agent must update repository documentation when a change affects any of these items.

Do not duplicate the entire coding standard in the README. Link to standards where appropriate.

## Top-Level Script Help

Every public standalone script must include comment-based help near the beginning of the file.

Minimum required sections:

```text
.SYNOPSIS
.DESCRIPTION
.PARAMETER
.EXAMPLE
.NOTES
```

Include when applicable:

```text
.INPUTS
.OUTPUTS
.LINK
.COMPONENT
.ROLE
.FUNCTIONALITY
```

The help must describe actual behavior.

### `.SYNOPSIS`

Provide a concise one-sentence summary.

Good:

```text
.SYNOPSIS
    Tests whether a configuration file contains all required settings.
```

Avoid:

```text
.SYNOPSIS
    This script does things with configuration.
```

### `.DESCRIPTION`

Explain:

- Primary purpose
- Major workflow
- Read-only or state-changing behavior
- Important safety controls
- External systems or dependencies
- Output or report behavior
- Significant limitations

Do not use the description as a line-by-line code narration.

### `.PARAMETER`

Every public parameter must have a matching `.PARAMETER` entry.

Document:

- Accepted value
- Meaning
- Default
- Whether the parameter is mandatory
- Validation constraints
- Security considerations
- Interaction with other parameters
- Whether pipeline input is accepted

Do not describe a parameter that no longer exists.

### `.EXAMPLE`

Examples must:

- Match current parameter names
- Be safe
- Use fictitious values
- Explain expected behavior
- Demonstrate common usage
- Demonstrate `-WhatIf` for modifying operations
- Avoid real credentials, domains, hosts, or endpoints

A destructive example must not show unguarded production execution.

### `.NOTES`

Use for:

- Minimum PowerShell version
- Supported operating systems
- Required privileges
- Dependencies
- Code-signing considerations
- Authoring or maintenance notes
- Known limitations
- Exit-code references
- Links to operational documentation

Do not place secrets, internal account names, or environment-specific production data in notes.

## Module Documentation

Modules should document:

- Purpose
- Public commands
- Installation or import method
- Minimum PowerShell version
- Supported operating systems
- Required modules and assemblies
- Configuration expectations
- Authentication method
- Exported output types
- Side effects
- Examples
- Testing instructions
- Known limitations
- Compatibility or breaking changes

The module manifest description must accurately summarize the module.

Exported function names in documentation must match the manifest and implementation.

## Public Function Help

Every exported function must have complete comment-based help.

Minimum sections:

```text
.SYNOPSIS
.DESCRIPTION
.PARAMETER
.EXAMPLE
.NOTES
```

Include `.INPUTS` and `.OUTPUTS` when pipeline input or returned types are important.

Comment-based help must remain adjacent to the function or in an established external-help system.

The agent must not rely on the function name alone as documentation.

## Private Function Documentation

Private helper functions require documentation appropriate to their complexity.

Use full comment-based help when a private function:

- Has multiple parameters
- Performs non-trivial validation
- Uses remoting
- Handles credentials
- Implements retries
- Calls an external API
- Modifies state
- Has unusual error behavior
- Is likely to be reused
- Is not immediately understandable from its name and implementation

A concise purpose comment may be sufficient for a small obvious helper.

## Inline Comments

All non-trivial logic must include administrator-friendly comments explaining intent.

Inline comments should explain:

- Why a decision was made
- Why a safety check exists
- Why a workaround is required
- Why a specific API or command is used
- Expected external-system behavior
- Retry and backoff logic
- Concurrency and throttling decisions
- Credential flow
- Remoting and runspace behavior
- Idempotency decisions
- Failure and rollback behavior
- Assumptions that cannot be inferred safely
- Compatibility constraints
- Performance tradeoffs
- Parsing rules
- Regular expressions
- Complex object transformations
- Security boundaries

Comments should answer "why" and "what risk is controlled," not merely "what statement runs."

Bad:

```powershell
# Increment retry count.
$RetryCount++
```

Better:

```powershell
# Retry only the status request. Recreating the remote job could duplicate
# the state-changing operation if the first submission succeeded.
$RetryCount++
```

## Required Commenting Areas

The following areas require comments unless the behavior is completely obvious:

- State-changing operations
- `$PSCmdlet.ShouldProcess()` boundaries
- Destructive path validation
- Credential retrieval and use
- Secret redaction
- Remote execution
- Native command invocation
- API pagination
- API retry behavior
- Rate-limit handling
- Background jobs
- Parallel runspaces
- Throttle limits
- Temporary-file handling
- Cleanup logic
- Rollback or compensation logic
- Complex regular expressions
- Non-obvious culture or encoding behavior
- Platform-specific branches
- Suppressed PSScriptAnalyzer rules
- Test mocks that simulate operational failures

## Comments Around Safety Controls

Comments must identify why a safety control exists when removing it later could create operational risk.

Example:

```powershell
# Reject root paths before deletion. A blank configuration value can resolve
# to the drive root after path normalization.
if ($ResolvedPath -eq [System.IO.Path]::GetPathRoot($ResolvedPath)) {
    throw "Refusing to remove root path '$ResolvedPath'."
}
```

Do not add comments that reveal sensitive implementation details unnecessarily.

## Commented-Out Code

Do not retain obsolete code by commenting it out.

Remove unused code and rely on source control history.

A short commented example may remain only when it is intentionally instructional and clearly labeled.

Do not leave:

- Old implementations
- Debug output
- Alternate commands
- Credentials
- Temporary fixes
- Disabled validation
- Disabled security controls

inside source files as commented blocks.

## TODO and FIXME Comments

Use `TODO` or `FIXME` only when unfinished work is intentionally accepted.

Each marker must include:

- A specific description
- Reason it is not completed
- Tracking reference when available
- Expected condition for removal

Good:

```powershell
# TODO: Replace the temporary polling loop after API version 3 exposes
# event-based completion. Track in issue #123.
```

Avoid:

```powershell
# TODO: Fix later.
```

Do not use TODO comments to conceal incomplete required behavior.

## Documentation for Configuration

Every configuration source must document:

- File format
- Required properties
- Optional properties
- Default values
- Data types
- Allowed values
- Secret-handling rules
- Example values using fictitious data
- Validation behavior
- Precedence when multiple sources exist
- Reload or restart requirements
- Backward-compatibility expectations

Sample configuration files must not contain working credentials or realistic secrets.

For PSD1 configuration, document that executable expressions must not be placed in untrusted data files.

## Documentation for Credentials

Document:

- Supported authentication mechanisms
- Credential source
- Required privileges
- Whether interactive prompting is supported
- Whether unattended execution is supported
- Secret-rotation expectations
- Where credentials are never written
- How errors are redacted
- Any platform-specific limitations

Do not document actual credential identifiers unless the repository explicitly requires non-sensitive placeholders.

## Documentation for State Changes

State-changing scripts and functions must document:

- What is changed
- Target selection
- Validation performed before change
- `-WhatIf` behavior
- `-Confirm` behavior
- Idempotency
- Verification after change
- Partial-failure behavior
- Rollback or compensation behavior
- Required privileges
- Logs and reports
- Irreversible effects

High-risk or bulk actions must document the explicit execution opt-in.

## Documentation for Output

Document public output contracts:

- Object type or custom type name
- Property names
- Property data types
- Meaning of status values
- Meaning of `Changed` or equivalent
- Error representation
- Timestamp format
- Report schemas
- Exit codes

Do not change documented output without updating tests and compatibility notes.

## Documentation for Tests

Tests should make their intent clear through descriptive names.

Add comments in tests when:

- Mock behavior is non-obvious
- A regression scenario requires historical context
- A safety boundary is being asserted
- Platform-specific behavior is simulated
- Test setup intentionally differs from production
- A Pester limitation requires a workaround

Do not narrate every assertion.

## Documentation for Suppressions and Exceptions

Any exception to a standard must document:

- Rule being bypassed
- Technical reason
- Scope
- Risk
- Mitigation
- Review or removal condition

This applies to:

- PSScriptAnalyzer suppressions
- Security exceptions
- Compatibility shims
- Use of deprecated commands
- Use of `Invoke-Expression`
- Certificate-validation exceptions
- Test exclusions
- Skipped tests

Broad or unexplained exceptions are prohibited.

## Documentation Synchronization

When behavior changes, update all affected documentation in the same change.

Review:

- Comment-based help
- README
- Examples
- Configuration reference
- Function output documentation
- Test names
- Troubleshooting
- Changelog or release notes
- Runbooks
- API or report schemas

Outdated documentation is a defect.

## Documentation Quality Review

Before completion, verify:

- Every public parameter is documented.
- Examples execute with current parameter names.
- Examples use safe fictitious values.
- Comments match current behavior.
- No secrets appear.
- No production-specific values were invented.
- Safety behavior is described.
- Runtime and platform requirements are accurate.
- Output and exit-code descriptions match implementation.
- Removed behavior is no longer documented.
- New behavior is documented.
- Links and file paths are valid.

## Guiding Rule

> Document enough intent, risk, behavior, and operating context that another qualified administrator can safely maintain the code without the original author present.
