#* 📝 This module contains a function to test the proposed release version
#* 📝 against existing versions on PyPI.

#* 📝 Imports the ShellHelper class containing reusable methods.
using module ../universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
Validates the proposed release version against the existing versions on PyPI.

.DESCRIPTION
This function checks if the provided project version is in the correct format (X.Y.Z) and whether it has already been published on PyPI.

If the version is invalid or already exists, it throws an error. Otherwise, it returns true.

.PARAMETER ProjectVersion
The version of the project to be released, expected in the format X.Y.Z.

.PARAMETER PyPIVersions
An array of strings representing the versions of the GeometricalDomination package that are already published on PyPI.

.INPUTS
None.

.OUTPUTS
[bool]
Returns true if the version is valid and not already published; otherwise, it throws an error.
#>
function Test-ReleaseVersion {

    param (
        [string]$ProjectVersion,
        [string[]]$PyPIVersions
    )

    #* 📝 This release workflow currently accepts numeric X.Y.Z versions.
    if ($ProjectVersion -notmatch '^\d+\.\d+\.\d+$') {
        [ShellHelper]::ThrowError(
            "Invalid project version '$ProjectVersion'. Expected format: X.Y.Z."
        )
    }

    #* 📝 Check whether the project version has already been published on PyPI.
    if ($PyPIVersions -contains $ProjectVersion) {
        [ShellHelper]::ThrowError(
            "Version $ProjectVersion has already been published on PyPI."
        )
    }

    return $true
}