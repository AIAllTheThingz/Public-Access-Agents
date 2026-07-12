# Completion Evidence Standard

## Purpose

This standard defines the evidence a coding agent must provide before PowerShell work is considered complete.

The completion response must distinguish between:

- Implemented
- Verified
- Assumed
- Not verified
- Not performed
- Remaining risk

Do not claim more certainty than the available evidence supports.

## Required Completion Summary

Use the following structure.

## 1. Outcome

State the requested outcome and whether it was:

- Completed
- Partially completed
- Blocked
- Not completed

Do not use vague statements such as "should be good."

## 2. Files Changed

List:

- Files created
- Files modified
- Files deleted
- Generated artifacts
- Configuration examples
- Tests
- Documentation

For each file, summarize why it changed.

## 3. Behavior Added or Changed

Describe observable behavior:

- New commands
- New parameters
- Changed defaults
- New output properties
- Error behavior
- Safety behavior
- Compatibility changes
- Deprecations
- Breaking changes

Do not describe implementation details as if they were user-visible behavior.

## 4. Safety Controls

State whether applicable controls were implemented and verified:

- Input validation
- Prerequisite validation
- `SupportsShouldProcess`
- `$PSCmdlet.ShouldProcess()`
- `-WhatIf`
- `-Confirm`
- Explicit execution mode
- Idempotency
- Post-change verification
- Secret redaction
- Least privilege
- Target-boundary checks
- Cleanup

If a control does not apply, state why briefly.

## 5. Documentation

State which documentation was added or updated:

- Script help
- Function help
- README
- Configuration reference
- Examples
- Troubleshooting
- Output schema
- Exit codes
- Compatibility notes
- Known limitations

State whether comments were reviewed for accuracy.

## 6. Tests

Report:

- Test files added or changed
- Test command
- Passed count
- Failed count
- Skipped count
- Not-run tests
- Regression tests
- Unit versus integration scope
- Coverage when collected

Example:

```text
Command:
pwsh -NoProfile -Command "Invoke-Pester -Path ./tests -Output Detailed"

Result:
- Passed: 42
- Failed: 0
- Skipped: 2
- Not run: Integration tests requiring a controlled API endpoint
```

Do not say "all tests passed" when some tests were skipped or not run without stating that distinction.

## 7. Static Analysis

Report:

- PSScriptAnalyzer command
- Tool version
- Errors
- Warnings
- Information findings when relevant
- Existing findings
- New findings
- Suppressions

Example:

```text
Invoke-ScriptAnalyzer -Path ./src -Recurse -Severity Warning,Error

Result:
- Errors: 0
- Warnings: 0
```

Do not conceal findings with broad suppressions.

## 8. Syntax and Import Validation

Report applicable checks:

- Parser validation
- Module import
- Manifest validation
- Exported command discovery
- Help discovery
- Configuration load
- Native dependency detection

Example:

```text
- PowerShell parser: Passed
- Test-ModuleManifest: Passed
- Import-Module under pwsh -NoProfile: Passed
```

## 9. Runtime and Environment

Report:

- PowerShell version
- PowerShell edition
- Operating system
- Architecture
- Pester version
- PSScriptAnalyzer version
- Relevant module versions
- External-service availability
- Privilege level when relevant

Do not imply validation across versions or platforms that were not tested.

## 10. Commands Run

List material validation commands exactly enough to reproduce.

Do not list commands that were planned but not executed.

If a command was not run, place it in the limitations section.

## 11. Assumptions

List assumptions that materially affect behavior, such as:

- Minimum PowerShell version
- Operating-system scope
- Configuration schema
- External command availability
- Authentication method
- Target naming
- API behavior
- Privilege model

Do not bury assumptions inside implementation prose.

## 12. Limitations and Not-Run Checks

For each unperformed validation step, state:

- What was not run
- Why it was not run
- Remaining risk
- Command or environment needed to complete it

Example:

```text
Not run:
Integration tests against the external service.

Reason:
No controlled test endpoint or credentials were available.

Remaining risk:
Authentication and API response compatibility were not verified.

Required validation:
Run ./tests/Integration in the approved non-production environment.
```

## 13. Remaining Risks

List unresolved risks:

- Untested platforms
- Untested PowerShell versions
- External dependency behavior
- Privileged operation behavior
- Concurrency behavior
- Large-scale behavior
- Rollback limitations
- Existing analyzer findings
- Existing failing tests
- Migration impact
- Breaking changes

Do not omit risks merely because they are inconvenient.

## 14. Diff Review

State that the final change set was reviewed for:

- Unrelated changes
- Secrets
- Debug output
- Placeholder values
- Temporary files
- Generated artifacts
- Commented-out code
- Formatting-only churn
- Public-interface changes
- Documentation consistency

If the diff was not reviewed, the work is not complete.

## 15. Allowed Claim Language

Use evidence-based language.

Acceptable:

- "Parsed successfully under PowerShell 7.4.2."
- "The 18 unit tests passed."
- "PSScriptAnalyzer reported no warnings or errors in changed files."
- "The integration path was not tested because no controlled endpoint was available."
- "Expected to work on Linux, but Linux was not tested."

Avoid without evidence:

- "Fully tested"
- "Production ready"
- "Secure"
- "Works everywhere"
- "Supports all PowerShell 7 versions"
- "Cross-platform"
- "The issue is definitely resolved"

## Completion Template

```markdown
# Completion Summary

## Outcome
Completed / Partially completed / Blocked

## Files Created
- `path/file`: Purpose

## Files Modified
- `path/file`: Purpose

## Files Deleted
- None

## Behavior
- Added:
- Changed:
- Preserved:

## Safety
- Input validation:
- ShouldProcess:
- WhatIf:
- Confirm:
- Idempotency:
- Post-change verification:
- Secret redaction:

## Documentation
- Updated:
- Not required:

## Tests
Command:
```powershell
<command>
```

Result:
- Passed:
- Failed:
- Skipped:
- Not run:

## Static Analysis
Command:
```powershell
<command>
```

Result:
- Errors:
- Warnings:
- Existing findings:

## Syntax and Import Validation
- Parser:
- Manifest:
- Module import:
- Exported commands:

## Runtime
- PowerShell:
- Edition:
- Operating system:
- Pester:
- PSScriptAnalyzer:
- Relevant modules:

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
```

## Definition of Complete

PowerShell work is complete only when:

- Required behavior is implemented.
- Safety requirements are satisfied.
- Documentation is current.
- Tests and static analysis are run where available.
- Validation limitations are explicit.
- The final diff is reviewed.
- Completion evidence is accurate.

## Guiding Rule

> Report what was proven, identify what was not proven, and never replace evidence with confidence.
