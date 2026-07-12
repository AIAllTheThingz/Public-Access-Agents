#requires -Version 7.4

<#
.SYNOPSIS
    Performs a clearly defined PowerShell operation.

.DESCRIPTION
    Describe the script's purpose, major workflow, prerequisites, external
    dependencies, output, safety controls, and important limitations.

    This template defaults to read-only behavior. When state-changing logic is
    added, keep SupportsShouldProcess enabled and wrap each meaningful change
    in $PSCmdlet.ShouldProcess().

.PARAMETER InputPath
    Specifies the input file or directory. The path must exist.

.PARAMETER OutputPath
    Specifies the optional output path. The script does not overwrite an
    existing file unless the implementation explicitly documents that behavior.

.PARAMETER Credential
    Specifies an optional credential for an external system. The credential is
    never written to output, logs, or reports.

.EXAMPLE
    ./Invoke-Example.ps1 -InputPath './input.json' -Verbose

    Runs the script with detailed operational messages.

.EXAMPLE
    ./Invoke-Example.ps1 `
        -InputPath './input.json' `
        -OutputPath './output/report.json' `
        -WhatIf

    Shows state-changing operations that would be performed without making
    changes. Remove this example if the implemented script remains read-only.

.INPUTS
    System.String

.OUTPUTS
    PSCustomObject

.NOTES
    PowerShell: 7.4 or later
    Edition: Core

    Replace placeholder behavior and documentation before use.
#>

[CmdletBinding(
    SupportsShouldProcess,
    ConfirmImpact = 'Medium'
)]
param (
    [Parameter(
        Mandatory,
        ValueFromPipelineByPropertyName
    )]
    [ValidateScript({
        if (-not (Test-Path -LiteralPath $_)) {
            throw "Input path '$_' does not exist."
        }

        $true
    })]
    [string] $InputPath,

    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string] $OutputPath,

    [Parameter()]
    [PSCredential] $Credential
)

Set-StrictMode -Version Latest

function Test-Prerequisite {
    <#
    .SYNOPSIS
        Validates prerequisites required by the script.

    .DESCRIPTION
        Performs read-only validation before any state-changing operation.

    .OUTPUTS
        System.Boolean
    #>

    [CmdletBinding()]
    [OutputType([bool])]
    param ()

    # Add dependency, privilege, platform, and configuration checks here.
    return $true
}

function Invoke-Main {
    <#
    .SYNOPSIS
        Coordinates the script workflow.

    .DESCRIPTION
        Runs validation, read-only discovery, optional state changes, and
        structured result generation.

    .PARAMETER InputPath
        Specifies the validated input path.

    .PARAMETER OutputPath
        Specifies the optional output path.

    .PARAMETER Credential
        Specifies an optional credential.

    .OUTPUTS
        PSCustomObject
    #>

    [CmdletBinding(
        SupportsShouldProcess,
        ConfirmImpact = 'Medium'
    )]
    [OutputType([PSCustomObject])]
    param (
        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string] $InputPath,

        [Parameter()]
        [ValidateNotNullOrEmpty()]
        [string] $OutputPath,

        [Parameter()]
        [PSCredential] $Credential
    )

    if (-not (Test-Prerequisite)) {
        throw 'One or more required prerequisites are unavailable.'
    }

    $ResolvedInputPath = (Resolve-Path -LiteralPath $InputPath -ErrorAction Stop).Path

    Write-Verbose "Validated input path '$ResolvedInputPath'."

    # Perform read-only discovery before any modification.
    $Changed = $false
    $Status = 'Discovered'
    $Message = 'Replace template discovery logic with the required behavior.'

    if ($PSBoundParameters.ContainsKey('OutputPath')) {
        $OutputDirectory = Split-Path -Path $OutputPath -Parent

        if (-not [string]::IsNullOrWhiteSpace($OutputDirectory)) {
            if (-not (Test-Path -LiteralPath $OutputDirectory -PathType Container)) {
                if ($PSCmdlet.ShouldProcess(
                        $OutputDirectory,
                        'Create output directory'
                    )) {
                    New-Item -Path $OutputDirectory -ItemType Directory -ErrorAction Stop |
                        Out-Null

                    $Changed = $true
                }
            }
        }

        # Add output serialization only after validating that no secrets or
        # credential objects are included in the exported data.
    }

    [PSCustomObject]@{
        InputPath    = $ResolvedInputPath
        OutputPath   = $OutputPath
        Status       = $Status
        Changed      = $Changed
        Message      = $Message
        TimestampUtc = [datetime]::UtcNow
    }
}

try {
    $InvokeMainParameters = @{
        InputPath = $InputPath
    }

    if ($PSBoundParameters.ContainsKey('OutputPath')) {
        $InvokeMainParameters.OutputPath = $OutputPath
    }

    if ($PSBoundParameters.ContainsKey('Credential')) {
        $InvokeMainParameters.Credential = $Credential
    }

    if ($WhatIfPreference) {
        $InvokeMainParameters.WhatIf = $true
    }

    Invoke-Main @InvokeMainParameters
}
catch {
    Write-Error -ErrorRecord $_
    exit 1
}
