#* 📝 This module contains a function to publish a release tag to the remote repository.

#* 📝 Imports the ShellHelper class containing reusable methods.
using module ../universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
Publishes a release tag to the remote repository.

.DESCRIPTION
This function creates a release tag on the current main commit and pushes it to the remote repository (origin).

It verifies that the tag creation and push are successful and provides feedback to the user.

.INPUTS
[string] $Version
    The version number for the release tag.

.OUTPUTS
[bool]
Returns true if the tag is created and pushed successfully; otherwise, it throws an error.
#>
function Publish-ReleaseTag {

    param (
        [string]$Version
    )

    #* 📝 Confirm that the tag will be created on the released main commit.
    $CurrentBranch = & git branch --show-current

    if (-not [ShellHelper]::TestLastExitCode("Verify current branch before creating release tag")) {
        [ShellHelper]::ThrowError("Could not determine the current Git branch.")
    }

    if ($CurrentBranch.Trim() -ne "main") {
        [ShellHelper]::ThrowError(
            "The release tag must be created while main is checked out. Current branch: '$CurrentBranch'."
        )
    }

    $Tag = "v$Version"

    #* 📝 Create the release tag on the current main commit.
    & git tag $Tag

    if (-not [ShellHelper]::TestLastExitCode("Create release tag '$Tag'")) {
        [ShellHelper]::ThrowError("Could not create release tag '$Tag'.")
    }

    #* 📝 Push the release tag to origin.
    & git push origin $Tag

    if (-not [ShellHelper]::TestLastExitCode("Publish release tag '$Tag'")) {
        [ShellHelper]::ThrowError(
            "Could not publish release tag '$Tag'. The tag exists locally on main."
        )
    }

    [ShellHelper]::Success(
        "Release tag '$Tag' successfully published!"
    )
}