#* 📝 This module retrieves all uploaded and available versions of this software on PyPI

#* 📝 Imports the ShellHelper class containing reusable methods.
using module ../universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
Retrieves the published versions of the GeometricalDomination package from PyPI.

.DESCRIPTION
This function executes a pip command to query the PyPI index for the GeometricalDomination package. 

It captures the output, extracts the available versions, and returns them as an array of strings.

.INPUTS
None.

.OUTPUTS
[string[]]
An array of strings representing the published versions of the GeometricalDomination package on PyPI.
#>
function Get-PyPIVersions {

    #* 📝 Retrieve published package versions from PyPI.
    $PyPIInfo = & py -m pip index versions geometricaldomination

    #* 📝 Verify that the command completed successfully.
    if (-not [ShellHelper]::TestLastExitCode("Retrieve published versions from PyPI")) {
        [ShellHelper]::ThrowError("Could not retrieve published versions from PyPI.")
    }

    #* 📝 Locate the line containing the available versions.
    $VersionLine = $PyPIInfo |
        Where-Object { $_ -match '^Available versions:\s*' } |
        Select-Object -First 1

    if ([string]::IsNullOrWhiteSpace($VersionLine)) {
        [ShellHelper]::ThrowError("Could not locate the available versions in PyPI output.")
    }

    #* 📝 Extract the individual version numbers.
    $Versions = (
        $VersionLine -replace '^Available versions:\s*', ''
    ) -split ',\s*' |
        ForEach-Object { $_.Trim() } |
        Where-Object { -not [string]::IsNullOrWhiteSpace($_) }

    return $Versions
}