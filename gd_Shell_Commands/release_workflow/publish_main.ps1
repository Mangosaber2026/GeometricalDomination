#* 📝 This module contains a function to publish the main branch to the remote repository.

#* 📝 Imports the ShellHelper class containing reusable methods.
using module ../universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
Publishes the main branch to the remote repository.

.DESCRIPTION
This function pushes the main branch to the remote repository (origin).

It verifies that the push is successful and provides feedback to the user.

.INPUTS
None.

.OUTPUTS
[bool]
Returns true if the push is successful; otherwise, it throws an error.
#>
function Publish-MainBranch {

    #* 📝 Ensure the release commit is being published from main.
    $CurrentBranch = & git branch --show-current

    if (-not [ShellHelper]::TestLastExitCode("Verify current branch before publishing main")) {
        [ShellHelper]::ThrowError("Could not determine the current Git branch.")
    }

    if ($CurrentBranch.Trim() -ne "main") {
        [ShellHelper]::ThrowError(
            "Cannot publish main while checked out on '$CurrentBranch'."
        )
    }

    #* 📝 Push main after experimental has been pushed successfully.
    & git push origin main

    if (-not [ShellHelper]::TestLastExitCode("Push main to origin")) {
        [ShellHelper]::ThrowError("Could not push main to origin.")
    }

    [ShellHelper]::Success(
        "Main branch successfully pushed to origin."
    )
}