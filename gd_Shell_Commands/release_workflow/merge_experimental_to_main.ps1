#* 📝 This module merges the branch experimental to the branch main of this software, 
#* 📝 assuming the user is currently on experimental and not on main yet

#* 📝 Imports the ShellHelper class containing reusable methods.
using module ../universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
Merges the experimental branch into the main branch.

.DESCRIPTION
This function switches to the main branch and merges the experimental branch into it without opening a commit-message editor.

.INPUTS
None.

.OUTPUTS
[bool]
Returns true if the merge is successful; otherwise, it throws an error.
#>
function Merge-ExperimentalIntoMain {

    #* 📝 Switch to main. The release tag must ultimately be created on this branch.
    & git switch main

    if (-not [ShellHelper]::TestLastExitCode("Switch to main")) {
        [ShellHelper]::ThrowError("Could not switch to main.")
    }

    #* 📝 Verify that the main working tree is clean before merging.
    $MainStatus = & git status --porcelain

    if (-not [ShellHelper]::TestLastExitCode("Retrieve main working tree status")) {
        [ShellHelper]::ThrowError("Could not retrieve the main working tree status.")
    }

    if ($MainStatus) {
        [ShellHelper]::ThrowError(
            "The main working tree is not clean. No remote branch has been published."
        )
    }

    #* 📝 Merge experimental into main without opening a commit-message editor.
    & git merge --no-edit experimental

    if (-not [ShellHelper]::TestLastExitCode("Merge experimental into main")) {
        [ShellHelper]::ThrowError(
            "Could not merge experimental into main. Resolve any merge conflicts before continuing."
        )
    }

    [ShellHelper]::Success(
        "Experimental has been merged into main locally."
    )
}