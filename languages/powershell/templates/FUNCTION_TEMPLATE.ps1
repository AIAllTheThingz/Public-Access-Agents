function Get-ExampleItem {
    <#
    .SYNOPSIS
        Returns one or more example items.

    .DESCRIPTION
        Demonstrates a PowerShell 7.x public advanced function with typed
        parameters, validation, pipeline support, structured output, and
        administrator-friendly comments.

        Rename the function with an approved PowerShell verb and a descriptive
        singular noun.

    .PARAMETER Name
        Specifies the item name. The parameter accepts pipeline input and
        property-name binding through the Name alias.

    .PARAMETER IncludeDetails
        Includes optional detail properties in the returned object.

    .EXAMPLE
        Get-ExampleItem -Name 'example'

        Returns the named item.

    .EXAMPLE
        'example1', 'example2' | Get-ExampleItem -IncludeDetails

        Returns multiple items from pipeline input with optional details.

    .INPUTS
        System.String

    .OUTPUTS
        PSCustomObject

    .NOTES
        PowerShell: 7.x
        Replace placeholder behavior before use.
    #>

    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param (
        [Parameter(
            Mandatory,
            ValueFromPipeline,
            ValueFromPipelineByPropertyName
        )]
        [Alias('ItemName')]
        [ValidateNotNullOrEmpty()]
        [string] $Name,

        [Parameter()]
        [switch] $IncludeDetails
    )

    begin {
        # Perform one-time prerequisite validation or initialization here.
    }

    process {
        try {
            Write-Verbose "Retrieving item '$Name'."

            # Replace with the actual read-only operation.
            $Properties = [ordered]@{
                Name         = $Name
                Status       = 'Available'
                TimestampUtc = [datetime]::UtcNow
            }

            if ($IncludeDetails) {
                $Properties.Details = 'Replace with actual detail data.'
            }

            [PSCustomObject] $Properties
        }
        catch {
            throw "Failed to retrieve item '$Name': $($_.Exception.Message)"
        }
    }

    end {
        # Dispose one-time resources here when required.
    }
}

<#
State-changing variant:

1. Change the verb to an approved modifying verb such as Set, New, Remove,
   Enable, Disable, or Invoke.
2. Add SupportsShouldProcess:

    [CmdletBinding(
        SupportsShouldProcess,
        ConfirmImpact = 'Medium'
    )]

3. Validate current state before modification.
4. Wrap the actual change:

    if ($PSCmdlet.ShouldProcess(
            $Name,
            'Describe the exact state-changing action'
        )) {
        # Perform the modification.
    }

5. Verify resulting state.
6. Return structured output including Changed, previous state, desired state,
   outcome, and TimestampUtc.
7. Add examples demonstrating -WhatIf.
#>
