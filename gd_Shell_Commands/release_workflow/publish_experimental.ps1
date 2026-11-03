#* 📝 This module provides a function to publish the experimental branch to the remote repository.

#* 📝 Imports the ShellHelper class containing reusable methods.
using module ../universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
Publishes the experimental branch to the remote repository.

.DESCRIPTION
This function pushes the experimental branch to the remote repository (origin).

It verifies that the push is successful and provides feedback to the user.

.INPUTS
None.

.OUTPUTS
[bool]
Returns true if the push is successful; otherwise, it throws an error.
#>
function Publish-ExperimentalBranch {

    #* 📝 Publish the experimental branch only after the local main merge succeeds.
    & git push origin experimental

    if (-not [ShellHelper]::TestLastExitCode("Push experimental to origin")) {
        [ShellHelper]::ThrowError("Could not push experimental to origin.")
    }

    [ShellHelper]::Success(
        "Experimental branch successfully pushed to origin."
    )
}