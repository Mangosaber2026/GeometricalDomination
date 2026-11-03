# ⚓ Anchor for this module: [[full-release-anchor|full_release.ps1]]
#* 📝 This module contains the complete GeometricalDomination release workflow.
#*📝 The release must be initiated from the experimental branch.

#* 📝 Imports the ShellHelper class containing reusable methods.
using module ../universal_shell_functions/shell_helper.psm1

#* 📝 Imports the function to retrieve the current project version from pyproject.toml
Import-Module (Join-Path $PSScriptRoot "get_project_version.ps1") -Force

#* 📝 Imports the function to retrieve all available versions of this software on PyPI
Import-Module (Join-Path $PSScriptRoot "get_pypi_versions.ps1") -Force

#* 📝 Imports the function to merge experimental branch to main branch, assuming the user is on experimental
Import-Module (Join-Path $PSScriptRoot "merge_experimental_to_main.ps1") -Force

#* 📝 Imports the function to make a new commit on experimental branch
Import-Module (Join-Path $PSScriptRoot "new_experimental_commit.ps1") -Force

#* 📝 Imports the function to publish experimental branch to remote branch
Import-Module (Join-Path $PSScriptRoot "publish_experimental.ps1") -Force

#* 📝 Imports the function to publish main branch to remote branch
Import-Module (Join-Path $PSScriptRoot "publish_main.ps1") -Force

#* 📝 Imports the function to publish the created release tag to [github](https://github.com) 
Import-Module (Join-Path $PSScriptRoot "publish_release_tag.ps1") -Force

#* 📝 Imports the function to test the branch the user is currently releasing from
Import-Module (Join-Path $PSScriptRoot "test_release_branches.ps1") -Force

#* 📝 Imports the function to validate the provided release tag from [pyproject.toml](https://github.com/Mangosaber2026/GeometricalDomination/blob/main/pyproject.toml) 
Import-Module (Join-Path $PSScriptRoot "test_release_tag.ps1") -Force

#* 📝 Imports the function to validate the template of the release tag
Import-Module (Join-Path $PSScriptRoot "test_release_version.ps1") -Force

#* 📝 -----------------------------------------------------------------------------
#* 📝 Repository configuration
#* 📝 -----------------------------------------------------------------------------

$WorkflowDirectory = $PSScriptRoot

$RepositoryRoot = [ShellHelper]::GetRepositoryRoot(
    $WorkflowDirectory
)

$ProjectToml = Join-Path $RepositoryRoot "pyproject.toml"

if (-not (Test-Path -LiteralPath $ProjectToml -PathType Leaf)) {
    [ShellHelper]::ThrowError("Could not locate pyproject.toml: $ProjectToml")
}


#* 📝 -----------------------------------------------------------------------------
#* 📝 Execute the release workflow
#* 📝 -----------------------------------------------------------------------------

#* 📝 Run all Git commands from the repository root, regardless of the caller's
#* 📝 original working directory. The original location is restored in finally.
Push-Location -LiteralPath $RepositoryRoot

try {

    #* 📝 -------------------------------------------------------------------------
    #* 📝 Preflight validation
    #* 📝 -------------------------------------------------------------------------

    $Version = Get-ProjectVersion `
        -ProjectToml $ProjectToml

    $PyPIVersions = Get-PyPIVersions

    [void](Test-ReleaseVersion `
        -ProjectVersion $Version `
        -PyPIVersions $PyPIVersions)

    [void](Test-ReleaseTag -Version $Version)

    [void](Test-ReleaseBranches)


    #* 📝 -------------------------------------------------------------------------
    #* 📝 Release execution
    #* 📝 -------------------------------------------------------------------------

    #* 📝 Create the commit locally first. Do not publish anything yet.
    New-ExperimentalCommit

    #* 📝 Switch to main, verify its working tree, and merge experimental locally.
    Merge-ExperimentalIntoMain

    #* 📝 Publish experimental first, then publish the merged main branch.
    Publish-ExperimentalBranch
    Publish-MainBranch

    #* 📝 Create and publish the tag while main is still checked out.
    Publish-ReleaseTag -Version $Version

    #* 📝 Return to experimental only after the release tag has been published.
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
    #* 📝 Display the error through ShellHelper and ensure that execution stops.
    [ShellHelper]::ThrowError($_.Exception.Message)
}

finally {
    Pop-Location
}