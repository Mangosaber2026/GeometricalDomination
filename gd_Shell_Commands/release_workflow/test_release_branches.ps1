#* 📝 This module contains a function to test the branch the user currently is in.

#* 📝 Imports the ShellHelper class containing reusable methods.
using module ../universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
Validates the Git branches for the release.

.DESCRIPTION
This function checks if the release can be initiated from the correct Git branch and if the branches are synchronized.

.PARAMETER Version
The version of the release.

.INPUTS
None.

.OUTPUTS
[bool]
Returns true if the branches are valid and synchronized; otherwise, it throws an error.
#>
function Test-ReleaseBranches {

    #* 📝 Verify that the workflow was started from experimental.
    $CurrentBranch = & git branch --show-current

    if (-not [ShellHelper]::TestLastExitCode("Retrieve current Git branch")) {
        [ShellHelper]::ThrowError("Could not determine the current Git branch.")
    }

    if ($CurrentBranch.Trim() -ne "experimental") {
        [ShellHelper]::ThrowError(
            "Release must be initiated from the experimental branch. Current branch: '$CurrentBranch'."
        )
    }

    #* 📝 Update remote-tracking information before comparing branches.
    & git fetch origin

    if (-not [ShellHelper]::TestLastExitCode("Fetch remote repository")) {
        [ShellHelper]::ThrowError("Could not fetch the remote repository.")
    }

    #* 📝 Compare local main with origin/main.
    $MainStatus = & git rev-list --left-right --count main...origin/main

    if (-not [ShellHelper]::TestLastExitCode("Compare main with origin/main")) {
        [ShellHelper]::ThrowError("Could not compare main with origin/main.")
    }

    if ($MainStatus -notmatch '^\s*(\d+)\s+(\d+)\s*$') {
        [ShellHelper]::ThrowError("Could not interpret the main branch comparison.")
    }

    $MainLocalAhead = [int]$Matches[1]
    $MainRemoteAhead = [int]$Matches[2]

    #* 📝 main and origin/main must be fully synchronized.
    if ($MainLocalAhead -ne 0 -or $MainRemoteAhead -ne 0) {
        $MainBranchMessage = @"
Main and origin/main are not synchronized.

Local commits ahead:  $MainLocalAhead
Remote commits ahead: $MainRemoteAhead

Synchronize main before releasing.
"@

        [ShellHelper]::ThrowError($MainBranchMessage)
    }

    #* 📝 Compare experimental with origin/experimental.
    $ExperimentalStatus = & git rev-list --left-right --count experimental...origin/experimental

    if (-not [ShellHelper]::TestLastExitCode("Compare experimental with origin/experimental")) {
        [ShellHelper]::ThrowError(
            "Could not compare experimental with origin/experimental."
        )
    }

    if ($ExperimentalStatus -notmatch '^\s*(\d+)\s+(\d+)\s*$') {
        [ShellHelper]::ThrowError(
            "Could not interpret the experimental branch comparison."
        )
    }

    $ExperimentalLocalAhead = [int]$Matches[1]
    $ExperimentalRemoteAhead = [int]$Matches[2]

    #* 📝 A remote-ahead branch could reject the subsequent push.
    #* 📝 Local-ahead commits are expected and can be pushed by this workflow.
    if ($ExperimentalRemoteAhead -ne 0) {
        $ExperimentalBranchMessage = @"
Experimental cannot be safely pushed.

Local commits ahead:  $ExperimentalLocalAhead
Remote commits ahead: $ExperimentalRemoteAhead

Synchronize experimental before releasing.
"@

        [ShellHelper]::ThrowError($ExperimentalBranchMessage)
    }

    [ShellHelper]::Achieved(
        "Main is synchronized and experimental is ready for a fast-forward push."
    )

    return $true
}