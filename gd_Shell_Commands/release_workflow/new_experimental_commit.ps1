#* 📝 This module provides a function to create a local commit for experimental changes in the repository.

#* 📝 Imports the ShellHelper class containing reusable methods.
using module ../universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
Creates a local commit for the experimental changes.

.DESCRIPTION
This function stages all changes in the repository and prompts the user for a commit message.

It verifies that there are staged changes before creating the commit locally.

The commit is not published to the remote repository; publishing is handled in a separate step.

.INPUTS
None.

.OUTPUTS
[bool]
Returns true if the commit is created successfully; otherwise, it throws an error.
#>
function New-ExperimentalCommit {

    #* 📝 Stage all repository changes.
    & git add -A

    if (-not [ShellHelper]::TestLastExitCode("Stage repository changes")) {
        [ShellHelper]::ThrowError("Could not stage repository changes.")
    }

    #* 📝 Verify that there are staged changes.
    & git diff --cached --quiet
    $DiffExitCode = $LASTEXITCODE

    if ($DiffExitCode -eq 0) {
        [ShellHelper]::ThrowError("There are no staged changes to commit.")
    }

    if ($DiffExitCode -ne 1) {
        [ShellHelper]::ThrowError("Could not inspect staged changes.")
    }

    #* 📝 Collect a non-empty commit message.
    do {
        $CommitMessage = (Read-Host "📦 Enter commit message").Trim()

        if ([string]::IsNullOrWhiteSpace($CommitMessage)) {
            [ShellHelper]::Warning(
                "Commit message cannot be empty. Please try again."
            )
        }

    } while ([string]::IsNullOrWhiteSpace($CommitMessage))

    #* 📝 Create the commit locally. Publishing is deliberately a separate step.
    & git commit -m $CommitMessage

    if (-not [ShellHelper]::TestLastExitCode("Create experimental commit")) {
        [ShellHelper]::ThrowError("Could not create the experimental commit.")
    }

    [ShellHelper]::Success(
        "Experimental changes committed locally."
    )
}