# PowerShell Testing Standard

## Purpose

This standard defines testing and validation requirements for PowerShell 7.x code.

Testing must provide evidence that the implementation behaves as required, fails safely, preserves public contracts, and does not perform unintended operations.

A passing syntax check proves only that PowerShell can parse the code. It does not prove the code is correct.

## Required Tooling

Use:

- PowerShell 7.x through `pwsh`
- Pester 5.x or the repository-defined supported version
- PSScriptAnalyzer
- Repository build or validation tools when available

Record the versions used in completion evidence.

Example:

```powershell
$PSVersionTable
Get-Module -Name Pester -ListAvailable |
    Sort-Object Version -Descending |
    Select-Object -First 1 Name, Version, Path

Get-Module -Name PSScriptAnalyzer -ListAvailable |
    Sort-Object Version -Descending |
    Select-Object -First 1 Name, Version, Path
```

## Testing Scope

Add or update tests for:

- New public behavior
- New reusable private behavior
- Bug fixes
- Parameter validation
- Output contracts
- Error behavior
- State-changing safety controls
- Configuration validation
- Compatibility-sensitive behavior
- Security-sensitive behavior
- Regression-prone paths

Tiny one-off snippets may be exempt when tests provide no meaningful value. The exemption must be reported.

## Test Categories

Use categories appropriate to the repository.

### Unit tests

Unit tests should:

- Test one logical behavior
- Avoid production systems
- Mock external dependencies
- Run quickly
- Be deterministic
- Verify success and failure paths
- Verify safety controls

### Integration tests

Integration tests may verify:

- Module boundaries
- File-system interactions
- External command integration
- Local services or containers
- Controlled test APIs
- Serialization and report generation

Integration tests must use controlled non-production targets.

### End-to-end tests

Use end-to-end tests when workflow behavior cannot be validated adequately through lower-level tests.

They must:

- Use explicit test environments
- Avoid production credentials
- Avoid irreversible operations
- Document cleanup
- Document prerequisites
- Be separable from the default unit-test run when necessary

## Test Organization

Follow repository conventions.

A common structure is:

```text
tests/
├── Unit/
├── Integration/
└── Fixtures/
```

Test files should normally use:

```text
FunctionName.Tests.ps1
ScriptName.Tests.ps1
ModuleName.Tests.ps1
```

Do not reorganize an existing test suite solely to match this example.

## Test Naming

Use descriptive `Describe`, `Context`, and `It` names.

Good:

```powershell
Describe 'Test-ConfigurationFile' {
    Context 'when the required ServerName property is missing' {
        It 'throws a validation error identifying ServerName' {
        }
    }
}
```

Avoid:

```powershell
Describe 'Tests' {
    It 'works' {
    }
}
```

Test names should describe observable behavior.

## Arrange, Act, Assert

Keep test structure understandable.

```powershell
It 'returns Changed as false when the desired state already exists' {
    # Arrange
    Mock Get-CurrentState {
        [PSCustomObject]@{
            Enabled = $true
        }
    }

    # Act
    $Result = Set-DesiredState -Enabled

    # Assert
    $Result.Changed | Should -BeFalse
}
```

Comments are optional when the structure is obvious. Use them when setup is complex.

## Test Isolation

Tests must not depend on:

- Execution order
- Previous test output
- Existing production files
- User profiles
- Current working directory
- Interactive prompts
- Network access unless explicitly integration-tested
- Machine-wide configuration
- Uncontrolled environment variables

Use `BeforeEach`, `AfterEach`, temporary test directories, and mocks to isolate behavior.

Clean up resources created by tests.

## Temporary Files

Use isolated temporary directories.

Do not write test artifacts into source directories.

Example:

```powershell
BeforeEach {
    $TestRoot = Join-Path -Path $TestDrive -ChildPath 'Case'
    New-Item -Path $TestRoot -ItemType Directory | Out-Null
}
```

Do not rely on a hardcoded system temporary path when Pester's `$TestDrive` is sufficient.

## Mocking

Mock external or state-changing dependencies in unit tests, including:

- REST APIs
- Remote sessions
- Services
- Registry operations
- File deletion
- Native executables
- Credential providers
- Cloud modules
- Database commands
- Reboots
- Scheduled tasks

Mocks must preserve the behavior relevant to the test.

Do not over-mock the function being tested.

Do not use mocks to conceal an implementation defect.

Use `Assert-MockCalled` or Pester 5 equivalents where verifying interaction is part of the behavior.

## Production Isolation

Unit tests must never:

- Connect to production servers
- Use production credentials
- Modify production services
- Restart systems
- Delete real files
- Change registry values
- Create real cloud resources
- Send production email
- Modify Active Directory
- Invoke irreversible external actions

If a test requires a live system, it is an integration or end-to-end test and must target a controlled test environment.

## Parameter Validation Tests

Test:

- Mandatory parameters
- Null and empty values
- Invalid sets
- Boundary ranges
- Invalid paths
- Unsupported file types
- Conflicting parameters
- Pipeline binding
- Aliases when part of the public contract
- Platform-specific rejection

Do not test PowerShell's built-in validation implementation redundantly unless the repository depends on a specific error contract.

## Output Contract Tests

Verify:

- Expected object type
- Property names
- Property data types
- Stable status values
- Timestamp type
- `Changed` or equivalent behavior
- Empty-result behavior
- Multiple-input behavior
- Pipeline compatibility

Avoid assertions based solely on formatted text when the public interface is structured output.

## Error Tests

Test expected failures:

- Missing prerequisites
- Invalid configuration
- Access denied
- Dependency unavailable
- External command non-zero exit
- API failure
- Timeout
- Partial failure
- Cleanup failure
- Unsupported operating system

Verify that:

- The error is not hidden
- The message identifies the failed operation
- Sensitive values are redacted
- The function does not report success
- State-changing follow-on steps do not execute

## `ShouldProcess` and `WhatIf` Tests

State-changing commands must test that modifications are suppressed under `-WhatIf`.

Example pattern:

```powershell
Describe 'Remove-ManagedFile' {
    BeforeEach {
        Mock Remove-Item
    }

    It 'does not remove the file when WhatIf is used' {
        Remove-ManagedFile -LiteralPath '/test/file.txt' -WhatIf

        Should -Invoke Remove-Item -Times 0
    }
}
```

Also test that:

- Modification occurs when authorized
- Target and action are meaningful where practical
- Verification is not falsely reported after a suppressed action
- High-risk explicit execution controls work as designed

Do not merely assert that the function accepts a `-WhatIf` parameter.

## Idempotency Tests

For state-changing behavior, test:

- No change when desired state already exists
- One change when current state differs
- Verification after modification
- Correct `Changed` result
- Safe repeated execution

Idempotency tests should prove that repeated execution does not create unintended duplicate changes.

## Regression Tests

A bug fix should include a test that fails before the fix and passes after it when practical.

The test should reproduce the actual defect without relying on production systems.

Document historical context only when the test name and behavior are not self-explanatory.

## Platform Tests

When code supports multiple operating systems:

- Test shared logic on all supported platforms through CI when possible.
- Test guarded platform branches.
- Verify unsupported platforms fail early with actionable errors.
- Do not claim cross-platform support based only on source inspection.

When only one platform is tested, state that limitation.

## Native Command Tests

Test native-command handling for:

- Correct executable path
- Discrete argument passing
- Spaces and quotes
- Non-zero exit codes
- Standard output
- Standard error
- Missing executable
- Platform differences

Do not invoke destructive native commands in unit tests.

## Configuration Tests

Test:

- Required keys
- Optional defaults
- Unknown keys when prohibited
- Invalid types
- Invalid values
- Missing files
- Malformed files
- Secret redaction
- Precedence across configuration sources
- Backward-compatible schema handling

Do not load untrusted PSD1 expressions as if they were inert data.

## Security Tests

Where applicable, test:

- Rejection of dangerous paths
- Rejection of command-injection input
- Rejection of unsupported URI schemes
- Certificate validation remains enabled
- Sensitive values do not enter output or logs
- Privileged operations are not attempted without authorization
- Untrusted script blocks are rejected
- Temporary files use controlled locations and permissions

## Test Data

Test fixtures must:

- Use fictitious values
- Avoid real credentials
- Avoid real production names
- Be deterministic
- Be small enough to understand
- Represent boundary and failure cases

Do not use copied production exports unless they are sanitized and explicitly approved.

## Pester Tags

Use tags when they improve selective execution.

Examples:

```text
Unit
Integration
EndToEnd
Windows
Linux
RequiresAdmin
Slow
```

Do not tag every test unnecessarily.

Default test runs should exclude tests requiring privileged or external environments unless the repository defines otherwise.

## Code Coverage

Use coverage as evidence, not as a vanity number.

A repository may define minimum coverage thresholds.

When no threshold exists:

- Cover critical safety and decision logic.
- Cover public behavior.
- Cover bug fixes.
- Report coverage if collected.
- Do not add meaningless assertions solely to increase percentage.

High coverage does not replace good test design.

## PSScriptAnalyzer

Run static analysis against changed PowerShell files or the repository-defined scope.

Example:

```powershell
Invoke-ScriptAnalyzer -Path . -Recurse -Severity Warning, Error
```

Review:

- New findings
- Existing findings
- Suppressions
- Rule configuration
- Compatibility warnings

Fix findings introduced by the change.

Do not claim unrelated existing findings were resolved.

## Syntax Validation

Parse changed `.ps1`, `.psm1`, and `.psd1` files.

Example:

```powershell
$ParseErrors = @()

Get-ChildItem -Path . -Recurse -File -Include '*.ps1', '*.psm1', '*.psd1' |
    ForEach-Object {
        $Tokens = $null
        $Errors = $null

        [System.Management.Automation.Language.Parser]::ParseFile(
            $_.FullName,
            [ref] $Tokens,
            [ref] $Errors
        ) | Out-Null

        $ParseErrors += $Errors
    }

if ($ParseErrors.Count -gt 0) {
    $ParseErrors | Format-List
    throw "PowerShell parsing failed with $($ParseErrors.Count) error(s)."
}
```

For data-only PSD1 files, also validate loading behavior through the intended safe mechanism.

## Module Validation

For modules, validate as applicable:

- Manifest syntax
- `Test-ModuleManifest`
- Import under `pwsh -NoProfile`
- Explicit exports
- Public command discovery
- Required modules
- Help availability
- No substantial side effects during import

Example:

```powershell
Test-ModuleManifest -Path ./src/ModuleName/ModuleName.psd1
Import-Module ./src/ModuleName/ModuleName.psd1 -Force
Get-Command -Module ModuleName
```

Use `-Force` only in controlled test or development contexts where module reload is intentional.

## Test Execution

Prefer repository-provided commands.

Otherwise:

```powershell
Invoke-Pester -Path ./tests -Output Detailed
```

For configuration-based runs:

```powershell
$PesterConfiguration = New-PesterConfiguration
$PesterConfiguration.Run.Path = './tests'
$PesterConfiguration.Output.Verbosity = 'Detailed'
$PesterConfiguration.Run.PassThru = $true

$Result = Invoke-Pester -Configuration $PesterConfiguration

if ($Result.FailedCount -gt 0) {
    throw "$($Result.FailedCount) Pester test(s) failed."
}
```

## Validation Failures

When validation fails, determine whether the failure is:

- Introduced by the current change
- Pre-existing
- Environmental
- Dependency-related
- Runtime-related
- Platform-related
- Caused by unavailable external services
- Caused by an incorrect test assumption

Fix failures introduced by the change.

Report pre-existing or environmental failures accurately.

Do not weaken or delete tests merely to obtain a passing result.

## Skipped Tests

Skipped tests require a documented reason.

Acceptable reasons may include:

- Unsupported platform
- Controlled integration environment unavailable
- Privileged test explicitly excluded
- External dependency unavailable

Do not skip a failing test because the implementation is inconvenient to fix.

## Completion Evidence

Report:

- PowerShell version
- Operating system
- Pester version
- PSScriptAnalyzer version
- Test commands
- Passed, failed, skipped, and not-run counts
- Static-analysis results
- Coverage when collected
- Environmental limitations
- Remaining risk

Follow `COMPLETION_EVIDENCE.md`.

## Guiding Rule

> Tests must demonstrate required behavior and safe failure, not merely generate a green result.
