#* 📝 This module contains a function to test the created release tag against
#* 📝 already available and created tags.

#* 📝 Imports the ShellHelper class containing reusable methods.
using module ../universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
Validates the Git tag for the release.

.DESCRIPTION
This function checks if the Git tag for the release already exists locally or remotely.

.PARAMETER Version
The version of the release.

.INPUTS
None.

.OUTPUTS
[bool]
Returns true if the tag is valid and not already exists; otherwise, it throws an error.
#>
function Test-ReleaseTag {

    param (
        [string]$Version
    )

    $Tag = "v$Version"

    #* 📝 Check whether the tag already exists locally.
    & git show-ref --verify --quiet "refs/tags/$Tag"
    $LocalExitCode = $LASTEXITCODE

    if ($LocalExitCode -eq 0) {
        [ShellHelper]::ThrowError("Git tag '$Tag' already exists locally.")
    }

    if ($LocalExitCode -ne 1) {
        [ShellHelper]::ThrowError("Could not check local Git tags.")
    }

    #* 📝 Check whether the tag already exists remotely.
    & git ls-remote --exit-code --tags origin "refs/tags/$Tag"
    $RemoteExitCode = $LASTEXITCODE

    if ($RemoteExitCode -eq 0) {
        [ShellHelper]::ThrowError("Git tag '$Tag' already exists on origin.")
    }

    if ($RemoteExitCode -ne 2) {
        [ShellHelper]::ThrowError("Could not check remote Git tags.")
    }

    return $true
}