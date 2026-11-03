# ⚓ Anchor for this module: [[full-release-anchor|full_release.ps1]]
# 📝 This module contains the complete GeometricalDomination release workflow.
# 📝 The release must be initiated from the experimental branch.

# Imports the ShellHelper class containing reusable methods.
using module ../universal_shell_functions/shell_helper.psm1


# -----------------------------------------------------------------------------
# Repository configuration
# -----------------------------------------------------------------------------

$WorkflowDirectory = $PSScriptRoot

$RepositoryRoot = [ShellHelper]::GetRepositoryRoot(
    $WorkflowDirectory
)

$ProjectToml = Join-Path $RepositoryRoot "pyproject.toml"

if (-not (Test-Path -LiteralPath $ProjectToml -PathType Leaf)) {
    [ShellHelper]::ThrowError("Could not locate pyproject.toml: $ProjectToml")
}


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

    # Retrieve published package versions from PyPI.
    $PyPIInfo = & py -m pip index versions geometricaldomination

    # Verify that the command completed successfully.
    if (-not [ShellHelper]::TestLastExitCode("Retrieve published versions from PyPI")) {
        [ShellHelper]::ThrowError("Could not retrieve published versions from PyPI.")
    }

    # Locate the line containing the available versions.
    $VersionLine = $PyPIInfo |
        Where-Object { $_ -match '^Available versions:\s*' } |
        Select-Object -First 1

    if ([string]::IsNullOrWhiteSpace($VersionLine)) {
        [ShellHelper]::ThrowError("Could not locate the available versions in PyPI output.")
    }

    # Extract the individual version numbers.
    $Versions = (
        $VersionLine -replace '^Available versions:\s*', ''
    ) -split ',\s*' |
        ForEach-Object { $_.Trim() } |
        Where-Object { -not [string]::IsNullOrWhiteSpace($_) }

    return $Versions
}


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

    # This release workflow currently accepts numeric X.Y.Z versions.
    if ($ProjectVersion -notmatch '^\d+\.\d+\.\d+$') {
        [ShellHelper]::ThrowError(
            "Invalid project version '$ProjectVersion'. Expected format: X.Y.Z."
        )
    }

    # Check whether the project version has already been published on PyPI.
    if ($PyPIVersions -contains $ProjectVersion) {
        [ShellHelper]::ThrowError(
            "Version $ProjectVersion has already been published on PyPI."
        )
    }

    return $true
}


<#
.SYNOPSIS
Retrieves the version of the project from its pyproject.toml file.

.DESCRIPTION
This function reads the version from the pyproject.toml file and returns it.

.PARAMETER ProjectToml
The path to the pyproject.toml file.

.INPUTS
None.

.OUTPUTS
[string]
Returns the version of the project.
#>
function Get-ProjectVersion {

    param (
        [string]$ProjectToml
    )

    $VersionOutput = & py -c "import tomllib, sys; print(tomllib.load(open(sys.argv[1], 'rb'))['project']['version'])" $ProjectToml

    if (-not [ShellHelper]::TestLastExitCode("Retrieve project version from pyproject.toml")) {
        [ShellHelper]::ThrowError("Could not retrieve the project version.")
    }

    $Version = ($VersionOutput -join "`n").Trim()

    if ([string]::IsNullOrWhiteSpace($Version)) {
        [ShellHelper]::ThrowError("Python returned an empty version.")
    }

    return $Version
}


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

    # Check whether the tag already exists locally.
    & git show-ref --verify --quiet "refs/tags/$Tag"
    $LocalExitCode = $LASTEXITCODE

    if ($LocalExitCode -eq 0) {
        [ShellHelper]::ThrowError("Git tag '$Tag' already exists locally.")
    }

    if ($LocalExitCode -ne 1) {
        [ShellHelper]::ThrowError("Could not check local Git tags.")
    }

    # Check whether the tag already exists remotely.
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

    # Verify that the workflow was started from experimental.
    $CurrentBranch = & git branch --show-current

    if (-not [ShellHelper]::TestLastExitCode("Retrieve current Git branch")) {
        [ShellHelper]::ThrowError("Could not determine the current Git branch.")
    }

    if ($CurrentBranch.Trim() -ne "experimental") {
        [ShellHelper]::ThrowError(
            "Release must be initiated from the experimental branch. Current branch: '$CurrentBranch'."
        )
    }

    # Update remote-tracking information before comparing branches.
    & git fetch origin

    if (-not [ShellHelper]::TestLastExitCode("Fetch remote repository")) {
        [ShellHelper]::ThrowError("Could not fetch the remote repository.")
    }

    # Compare local main with origin/main.
    $MainStatus = & git rev-list --left-right --count main...origin/main

    if (-not [ShellHelper]::TestLastExitCode("Compare main with origin/main")) {
        [ShellHelper]::ThrowError("Could not compare main with origin/main.")
    }

    if ($MainStatus -notmatch '^\s*(\d+)\s+(\d+)\s*$') {
        [ShellHelper]::ThrowError("Could not interpret the main branch comparison.")
    }

    $MainLocalAhead = [int]$Matches[1]
    $MainRemoteAhead = [int]$Matches[2]

    # main and origin/main must be fully synchronized.
    if ($MainLocalAhead -ne 0 -or $MainRemoteAhead -ne 0) {
        $MainBranchMessage = @"
Main and origin/main are not synchronized.

Local commits ahead:  $MainLocalAhead
Remote commits ahead: $MainRemoteAhead

Synchronize main before releasing.
"@

        [ShellHelper]::ThrowError($MainBranchMessage)
    }

    # Compare experimental with origin/experimental.
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

    # A remote-ahead branch could reject the subsequent push.
    # Local-ahead commits are expected and can be pushed by this workflow.
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

    # Stage all repository changes.
    & git add -A

    if (-not [ShellHelper]::TestLastExitCode("Stage repository changes")) {
        [ShellHelper]::ThrowError("Could not stage repository changes.")
    }

    # Verify that there are staged changes.
    & git diff --cached --quiet
    $DiffExitCode = $LASTEXITCODE

    if ($DiffExitCode -eq 0) {
        [ShellHelper]::ThrowError("There are no staged changes to commit.")
    }

    if ($DiffExitCode -ne 1) {
        [ShellHelper]::ThrowError("Could not inspect staged changes.")
    }

    # Collect a non-empty commit message.
    do {
        $CommitMessage = (Read-Host "📦 Enter commit message").Trim()

        if ([string]::IsNullOrWhiteSpace($CommitMessage)) {
            [ShellHelper]::Warning(
                "Commit message cannot be empty. Please try again."
            )
        }

    } while ([string]::IsNullOrWhiteSpace($CommitMessage))

    # Create the commit locally. Publishing is deliberately a separate step.
    & git commit -m $CommitMessage

    if (-not [ShellHelper]::TestLastExitCode("Create experimental commit")) {
        [ShellHelper]::ThrowError("Could not create the experimental commit.")
    }

    [ShellHelper]::Success(
        "Experimental changes committed locally."
    )
}


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

    # Switch to main. The release tag must ultimately be created on this branch.
    & git switch main

    if (-not [ShellHelper]::TestLastExitCode("Switch to main")) {
        [ShellHelper]::ThrowError("Could not switch to main.")
    }

    # Verify that the main working tree is clean before merging.
    $MainStatus = & git status --porcelain

    if (-not [ShellHelper]::TestLastExitCode("Retrieve main working tree status")) {
        [ShellHelper]::ThrowError("Could not retrieve the main working tree status.")
    }

    if ($MainStatus) {
        [ShellHelper]::ThrowError(
            "The main working tree is not clean. No remote branch has been published."
        )
    }

    # Merge experimental into main without opening a commit-message editor.
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

    # Publish the experimental branch only after the local main merge succeeds.
    & git push origin experimental

    if (-not [ShellHelper]::TestLastExitCode("Push experimental to origin")) {
        [ShellHelper]::ThrowError("Could not push experimental to origin.")
    }

    [ShellHelper]::Success(
        "Experimental branch successfully pushed to origin."
    )
}


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

    # Ensure the release commit is being published from main.
    $CurrentBranch = & git branch --show-current

    if (-not [ShellHelper]::TestLastExitCode("Verify current branch before publishing main")) {
        [ShellHelper]::ThrowError("Could not determine the current Git branch.")
    }

    if ($CurrentBranch.Trim() -ne "main") {
        [ShellHelper]::ThrowError(
            "Cannot publish main while checked out on '$CurrentBranch'."
        )
    }

    # Push main after experimental has been pushed successfully.
    & git push origin main

    if (-not [ShellHelper]::TestLastExitCode("Push main to origin")) {
        [ShellHelper]::ThrowError("Could not push main to origin.")
    }

    [ShellHelper]::Success(
        "Main branch successfully pushed to origin."
    )
}


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

    # Confirm that the tag will be created on the released main commit.
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

    # Create the release tag on the current main commit.
    & git tag $Tag

    if (-not [ShellHelper]::TestLastExitCode("Create release tag '$Tag'")) {
        [ShellHelper]::ThrowError("Could not create release tag '$Tag'.")
    }

    # Push the release tag to origin.
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


# -----------------------------------------------------------------------------
# Execute the release workflow
# -----------------------------------------------------------------------------

# Run all Git commands from the repository root, regardless of the caller's
# original working directory. The original location is restored in finally.
Push-Location -LiteralPath $RepositoryRoot

try {

    # -------------------------------------------------------------------------
    # Preflight validation
    # -------------------------------------------------------------------------

    $Version = Get-ProjectVersion `
        -ProjectToml $ProjectToml

    $PyPIVersions = Get-PyPIVersions

    [void](Test-ReleaseVersion `
        -ProjectVersion $Version `
        -PyPIVersions $PyPIVersions)

    [void](Test-ReleaseTag -Version $Version)

    [void](Test-ReleaseBranches)


    # -------------------------------------------------------------------------
    # Release execution
    # -------------------------------------------------------------------------

    # Create the commit locally first. Do not publish anything yet.
    New-ExperimentalCommit

    # Switch to main, verify its working tree, and merge experimental locally.
    Merge-ExperimentalIntoMain

    # Publish experimental first, then publish the merged main branch.
    Publish-ExperimentalBranch
    Publish-MainBranch

    # Create and publish the tag while main is still checked out.
    Publish-ReleaseTag -Version $Version

    # Return to experimental only after the release tag has been published.
    & git switch experimental

    if (-not [ShellHelper]::TestLastExitCode("Return to experimental")) {
        [ShellHelper]::ThrowError(
            "The release was published, but the script could not return to experimental."
        )
    }

    [ShellHelper]::Success(
        "GeometricalDomination $Version release completed successfully!"
    )
}

catch {
    # Display the error through ShellHelper and ensure that execution stops.
    [ShellHelper]::ThrowError($_.Exception.Message)
}

finally {
    Pop-Location
}