# PowerShell Coding Standard

## Purpose

This standard defines the coding conventions for PowerShell 7.x scripts, modules, manifests, and tests.

The objective is not merely to produce code that executes. Code must be understandable, testable, supportable, and safe for administrators and developers who did not write it.

Prefer clear code over clever code.

## General Principles

PowerShell code must be:

- Clear
- Predictable
- Maintainable
- Testable
- Consistent
- Appropriately documented
- Safe by default
- Focused on a defined responsibility

Use these principles:

- Favor readability over brevity.
- Favor explicit behavior over hidden behavior.
- Favor structured objects over formatted text.
- Favor small focused functions over large procedural blocks.
- Favor established PowerShell conventions over patterns imported from unrelated languages.
- Avoid premature optimization.
- Avoid speculative abstraction.
- Avoid unnecessary dependencies.
- Avoid broad refactoring during targeted changes.

## Runtime and Edition

- Target PowerShell 7.x.
- Execute with `pwsh`.
- Use `#requires -Version` when a standalone script needs a defined minimum version.
- Use module manifest metadata for module compatibility requirements.
- Do not add Windows PowerShell 5.1 compatibility unless explicitly required.
- Guard platform-specific code with `$IsWindows`, `$IsLinux`, or `$IsMacOS`.
- Do not claim cross-platform support without testing.

Example:

```powershell
#requires -Version 7.4
```

## Script Structure

Non-trivial scripts should generally use this order:

1. `#requires` statements
2. Comment-based help
3. `[CmdletBinding()]`
4. Parameter block
5. Strict mode, when appropriate
6. Initialization
7. Function definitions
8. Main execution
9. Cleanup and final error handling

Do not place substantial executable logic before the parameter block.

A standalone script should make its orchestration path easy to identify.

## Module Structure

A typical module may use:

```text
ModuleName/
├── ModuleName.psd1
├── ModuleName.psm1
├── Public/
├── Private/
└── Tests/
```

Do not restructure an existing module solely to match this example.

Requirements:

- Export public functions explicitly.
- Do not export private helper functions.
- Avoid wildcard exports.
- Do not execute substantial operational work during module import.
- Do not install dependencies during normal import.
- Keep module-scoped state minimal and documented.

## Function Design

A function should perform one clear responsibility.

A function should not:

- Perform unrelated operations
- Mix data collection with formatting
- Conceal significant side effects
- Modify global state without explicit justification
- Depend on undeclared variables
- Return unrelated object types without a documented reason
- Perform remote or state-changing work merely because the module was imported

Split a function when doing so improves responsibility, readability, testing, or reuse. Do not split solely to satisfy an arbitrary line-count target.

## Function Naming

Use approved PowerShell verbs and the `Verb-Noun` convention.

Examples:

```powershell
Get-SystemStatus
Test-SystemConnection
Set-SystemConfiguration
Invoke-SystemMaintenance
Export-SystemReport
```

Review approved verbs with:

```powershell
Get-Verb
```

Avoid vague names such as:

```text
CheckServer
DoCleanup
ProcessThings
HandleData
RunTask
FixStuff
```

Use singular nouns unless an established PowerShell convention or repository standard requires otherwise.

## Variables and Parameters

Use descriptive PascalCase names.

Prefer:

```powershell
$ComputerName
$ConfigurationPath
$RetryCount
$ConnectionResult
$IsConnected
$HasPermission
$ShouldRetry
```

Avoid:

```powershell
$s
$cfg
$tmp
$res
$flag
```

Short names are acceptable only in extremely narrow, conventional contexts.

Parameter names should align with PowerShell conventions:

- `Path`
- `LiteralPath`
- `Name`
- `ComputerName`
- `Credential`
- `InputObject`
- `OutputPath`
- `ConfigurationPath`

Do not rename existing public parameters merely for stylistic preference.

## Advanced Functions

Public functions should normally be advanced functions.

```powershell
function Get-SystemStatus {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string] $ComputerName
    )

    process {
        # Implementation
    }
}
```

Functions that modify state must use:

```powershell
[CmdletBinding(SupportsShouldProcess)]
```

High-impact operations should set an appropriate `ConfirmImpact`.

## Parameter Design

Parameters should declare:

- Appropriate data type
- Mandatory status
- Validation
- Default value when safe
- Pipeline behavior when supported
- Comment-based help

Avoid untyped parameters unless flexibility is genuinely required.

Prefer:

```powershell
[Parameter(Mandatory)]
[ValidateNotNullOrEmpty()]
[string] $ComputerName
```

Use validation attributes intentionally:

- `ValidateNotNull`
- `ValidateNotNullOrEmpty`
- `ValidateSet`
- `ValidateRange`
- `ValidatePattern`
- `ValidateScript`
- `AllowNull`
- `AllowEmptyString`
- `AllowEmptyCollection`

Do not add decorative validation that does not reflect actual requirements.

Use mandatory parameters when no safe, meaningful default exists.

Never use environment-specific production defaults.

## Switch Parameters

Use `[switch]` for optional true-or-false behavior.

Prefer:

```powershell
[Parameter()]
[switch] $Force
```

Avoid:

```powershell
[bool] $Force = $false
```

Use a Boolean parameter only when callers must explicitly provide both `$true` and `$false`.

Do not redefine common parameters such as `Verbose`, `Debug`, `WhatIf`, or `Confirm`.

## Pipeline Support

Support pipeline input only when it provides meaningful usability.

Use `ValueFromPipeline` for direct object input and `ValueFromPipelineByPropertyName` for named properties.

Pipeline-capable functions must correctly handle multiple inputs through `begin`, `process`, and `end` blocks as appropriate.

Do not declare pipeline support and then process only the final item.

## `ShouldProcess`

Wrap the actual state-changing operation with `$PSCmdlet.ShouldProcess()`.

```powershell
if ($PSCmdlet.ShouldProcess(
        $ComputerName,
        "Restart service '$ServiceName'"
    )) {
    Restart-Service -Name $ServiceName
}
```

The target and action must be understandable.

Do not wrap only a status message while allowing the modification to occur outside the guard.

Do not create a custom `-WhatIf` parameter.

`ShouldContinue` may be used only for exceptionally dangerous operations and must not replace `ShouldProcess`.

## Structured Output

Reusable functions must return structured objects.

Prefer:

```powershell
[PSCustomObject]@{
    ComputerName = $ComputerName
    Status       = $Status
    Changed      = $Changed
    TimestampUtc = [datetime]::UtcNow
}
```

Avoid:

```powershell
"$ComputerName is $Status"
```

Output properties should:

- Use stable descriptive names
- Use appropriate data types
- Remain consistent across success and failure paths
- Be suitable for filtering, exporting, and testing

Custom type names may be used when they add real value for formatting, testing, or discoverability. Do not create custom type names for every temporary object.

## Output Streams

Use PowerShell streams intentionally:

- `Write-Verbose` for detailed operational information
- `Write-Debug` for developer diagnostics
- `Write-Warning` for recoverable concerns
- `Write-Error` for error records
- `Write-Information` for informational messages
- Structured pipeline output for results

Use `Write-Host` only for intentional console presentation when pipeline consumption is not expected.

Do not use `Write-Host` to return data.

## Formatting

Do not use formatting commands inside reusable functions:

```text
Format-Table
Format-List
Format-Wide
Out-String
```

Formatting belongs at the presentation boundary.

Prefer returning objects and allowing the caller to format them.

## Aliases and Positional Parameters

Do not use aliases in committed scripts, modules, or tests.

Avoid:

```powershell
gci
ls
?
%
select
sort
```

Prefer full command names.

Use named parameters by default, especially for:

- Destructive commands
- Remote commands
- Native commands
- Commands with several positional parameters
- Commands where parameter meaning is not immediately obvious

## Splatting

Use splatting when a command has several parameters, parameters are conditionally added, or readability improves.

```powershell
$InvokeCommandParameters = @{
    ComputerName = $ComputerName
    ScriptBlock  = $ScriptBlock
    ErrorAction  = 'Stop'
}

if ($null -ne $Credential) {
    $InvokeCommandParameters.Credential = $Credential
}

Invoke-Command @InvokeCommandParameters
```

Use descriptive splat variable names. Avoid `$params`, `$p`, and `$args`.

## Automatic Variables

Do not overwrite automatic variables, including:

- `$_`
- `$PSItem`
- `$args`
- `$input`
- `$this`
- `$Error`
- `$Matches`
- `$LASTEXITCODE`
- `$PSBoundParameters`
- `$PSScriptRoot`
- `$PSCommandPath`

For longer script blocks, assign `$_` to a descriptive variable when that improves clarity.

## Scope

Avoid global variables.

Prefer:

- Parameters
- Local variables
- Function return values
- Script-scoped module state
- Configuration objects
- Dependency injection

Script-scoped module state must be minimized, initialized clearly, and documented.

Do not modify caller scope unexpectedly.

## Strict Mode

Non-trivial new scripts and modules should normally use:

```powershell
Set-StrictMode -Version Latest
```

Introduce strict mode carefully into existing code because it may expose pre-existing defects.

Strict mode does not replace tests.

## Comparisons

Use PowerShell comparison operators:

```text
-eq -ne -gt -ge -lt -le
-like -notlike
-match -notmatch
-contains -notcontains
-in -notin
```

Use case-sensitive variants only when case materially affects behavior.

Place `$null` on the left:

```powershell
if ($null -eq $Result) {
}
```

Avoid unnecessary Boolean comparisons:

```powershell
if ($IsConnected) {
}

if (-not $IsConnected) {
}
```

Distinguish between `$null`, empty collections, empty strings, and collections containing `$null`.

## Collections and Enumeration

When a collection is required, force array semantics intentionally:

```powershell
$Results = @(
    Get-Something
)
```

Avoid repeated `+=` operations for large arrays.

Prefer:

```powershell
$Results = foreach ($Item in $Items) {
    Get-Result -InputObject $Item
}
```

Use `foreach` statements when control flow, performance, or multi-step logic matters.

Use `ForEach-Object` when pipeline composition is clearer.

Do not use pipelines merely to make code appear idiomatic.

## Hashtables

Use normal hashtables for lookup behavior.

Use ordered hashtables when property order matters.

Validate configuration hashtables before use:

- Required keys
- Expected types
- Allowed values
- Unknown keys when strict schemas are required

## Strings

Use single-quoted strings when interpolation is not required.

Use double-quoted strings when interpolation is required.

Avoid unnecessary concatenation.

Do not use interpolation to construct executable PowerShell code.

Use here-strings for multiline content. Use single-quoted here-strings when interpolation is not required.

## Paths

Use `$PSScriptRoot` for paths relative to the current script.

Use `Join-Path` or `[System.IO.Path]::Combine()` for construction.

Do not depend on the current working directory unless explicitly required.

Use `-LiteralPath` when wildcard behavior is not intended.

Validate paths before destructive operations.

Do not allow an empty, root-level, or unexpectedly expanded path to reach a destructive command.

## File Operations

File operations must:

- Validate paths
- Distinguish files from directories
- Avoid unintended wildcard expansion
- Handle existing targets intentionally
- Use `ShouldProcess` for modification
- Avoid overwrite by default
- Use safe temporary-file handling
- Verify results where appropriate

Do not add `-Force` casually.

## Date and Time

Use `[datetime]` values internally.

Prefer UTC for:

- Logs
- Audit records
- APIs
- Cross-time-zone reports
- Machine comparisons

Serialize machine-consumed timestamps using ISO 8601:

```powershell
[datetime]::UtcNow.ToString('o')
```

Do not compare formatted date strings when actual date comparisons are possible.

## Type Conversion

Use explicit casts when they improve clarity or correctness.

Use parsing methods when input format must be tightly controlled.

Use invariant culture where machine-readable formats require it.

Do not rely on culture-dependent conversion for configuration or protocol data.

## Enums and Classes

Use enums for stable finite internal value sets when they improve correctness.

Use `ValidateSet` when a public string parameter provides better usability and simpler maintenance.

Use PowerShell classes only when they provide clear value, such as strong object models or reusable stateful behavior.

Do not use classes merely to make PowerShell resemble C#.

## Remoting, Jobs, and Parallel Execution

Do not assume local variables, functions, modules, or credentials are automatically available in:

- Remote sessions
- Background jobs
- Thread jobs
- Parallel runspaces

Pass values explicitly.

Use `$using:` only when its behavior is understood and appropriate.

Concurrency must consider:

- Throttling
- Thread safety
- Runspace isolation
- Credential handling
- API limits
- Logging integrity
- Output ordering
- Partial failures

Do not use `ForEach-Object -Parallel` merely because it exists.

State-changing operations should not run concurrently unless the design explicitly supports and tests concurrency.

## Native Commands

Invoke native commands with the call operator and discrete arguments.

```powershell
& $ExecutablePath @ArgumentList
```

Do not build a single command string from untrusted input.

Check `$LASTEXITCODE` when the executable uses process exit codes.

Capture standard output and standard error intentionally when required.

Test arguments containing spaces, quotes, wildcard characters, Unicode, and shell metacharacters.

## Modules and Dependencies

Before using a module, verify:

- PowerShell 7 compatibility
- Operating-system compatibility
- Minimum version
- Required assemblies
- Required modules
- Repository source and trust
- Licensing or redistribution constraints when applicable

Do not install modules automatically during normal execution unless explicitly required and documented.

Do not use `-Force` for imports or installation without a defined reason.

Module manifests should declare explicit exports and compatibility metadata.

## Error Handling

Use `try`, `catch`, and `finally` around meaningful operation boundaries.

Use `-ErrorAction Stop` when a command failure must be caught.

Do not wrap every statement in its own `try` block.

Do not use empty catches.

When adding context, include:

- Failed operation
- Relevant target
- Underlying exception message
- Corrective action when known

Do not include secrets.

Use `throw` when execution cannot safely continue.

Use `throw` without an expression when rethrowing unchanged so the original error context is preserved.

Use typed catches when different exception categories require different handling.

## Preference Variables

Do not modify global preference variables for convenience.

Prefer command-level parameters such as `-ErrorAction`.

When a temporary preference change is necessary, scope it narrowly and restore the original value.

## Idempotency

State-changing functions should be idempotent where practical.

The expected flow is:

1. Inspect current state.
2. Compare current state with desired state.
3. Modify only what differs.
4. Verify resulting state.
5. Return whether a change occurred.

Do not report a change when no modification occurred.

## Exit Behavior

Reusable functions and modules must not call `exit`.

Return objects or throw errors.

Standalone scripts may use documented exit codes for automation.

Do not terminate the entire host from a reusable function.

## Main Execution

Keep reusable functions separate from orchestration.

A standalone script should make the main execution path easy to identify and test.

Do not execute substantial work merely by dot-sourcing a helper or importing a module.

## Dynamic Code

Avoid dynamically generated PowerShell code.

Prohibited by default:

- `Invoke-Expression`
- Runtime-generated function bodies
- Self-modifying scripts
- Temporary scripts created solely for execution
- Executing user-supplied script text

Use parameters, functions, objects, and source-controlled script blocks instead.

## Source Encoding and Formatting

- Use UTF-8 source encoding.
- Preserve repository line-ending conventions.
- Use four spaces for indentation unless the repository defines another standard.
- Use consistent brace placement.
- Keep lines near or below 120 characters where practical.
- Use blank lines between logical sections.
- Do not place multiple statements on one line.
- Avoid backticks for line continuation when natural PowerShell continuation or splatting is available.
- Do not reformat unrelated code during a targeted change.

## PSScriptAnalyzer

Committed PowerShell code must pass the repository's configured rules or document existing findings.

Do not add broad suppressions.

Any suppression must:

- Name a specific rule
- Apply to the narrowest scope
- Include a clear justification
- Be reviewed as part of the change

Disabling useful rules is not equivalent to resolving findings.

## Backward Compatibility

Treat public behavior as a contract.

Preserve unless explicitly changed:

- Function names
- Parameter names and aliases
- Defaults
- Pipeline input
- Output property names and types
- Exit codes
- Configuration keys
- Report schemas
- Module exports

Document breaking changes and update callers, tests, and documentation.

## Guiding Rule

> Write PowerShell that another qualified administrator can understand, test, troubleshoot, and safely modify without the original author present.
