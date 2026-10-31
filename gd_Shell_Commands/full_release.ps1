# ⚓ Anchor for this module: [[full-release-anchor|full_release.ps1]]
#* 📝 This module contains the full release workflow,
#* 📝 considering the user is on branch experimental.

using module ./universal_shell_functions/shell_helper.psm1
Import-Module (Join-Path $PSScriptRoot "universal_shell_functions\get_project_root.psm1") -Force

function experimental_push {

    git add -A

    while ($true) {
        $message = (Read-Host "📦 Enter commit message").Trim()

        if (-not [string]::IsNullOrWhiteSpace($message)) {
            break
        }

        [ShellHelper]::Warning("Commit message cannot be empty. Please try again.")
    }

    git commit -m $message

    if (-not [ShellHelper]::TestLastExitCode("Commit given message: $message")) { return }

    git push origin experimental

    if (-not [ShellHelper]::TestLastExitCode("Push to git repository: experimental")) { return }

    git switch main

    if (-not [ShellHelper]::TestLastExitCode("Switch to branch: main")) { return }

    #* 📝 Check whether the main working tree is clean.

    $main_status = git status --porcelain

    if (-not [ShellHelper]::TestLastExitCode("Retrieve git status of branch main")) { return }

    if ($main_status) {
        [ShellHelper]::Warning("Main working tree is not clean!")
        return
    }

    #* 📝 Fetch the latest remote information.

    git fetch origin

    if (-not [ShellHelper]::TestLastExitCode("Fetch origin from github")) { return }

    #* 📝 Compare local main with origin/main.

    $status = git rev-list --left-right --count main...origin/main

    if (-not [ShellHelper]::TestLastExitCode("Compare main with origin/main")) { return }

    $counts = $status.Trim() -split '\s+'

    $LocalAhead = [int]$counts[0]
    $RemoteAhead = [int]$counts[1]

    if ($LocalAhead -ne 0 -or $RemoteAhead -ne 0) {
        [ShellHelper]::Warning("Main and origin/main are not synchronized.")
        [ShellHelper]::Information("Local commits ahead: $LocalAhead")
        [ShellHelper]::Information("Remote commits ahead: $RemoteAhead")
        return
    }

    [ShellHelper]::Achieved("Main is synchronized with origin/main.")

    #* 📝 Merge experimental into main.

    git merge experimental

    if (-not [ShellHelper]::TestLastExitCode("Merge with branch experimental")) { return }

    git push origin main

    if (-not [ShellHelper]::TestLastExitCode("Push commits to main repository")) { return }

    #* 📝 Validate and create the version tag.

    while ($true) {
        $version_tag = (Read-Host "🏷️ Enter version release tag").Trim()

        if ($version_tag -match '^\d+\.\d+\.\d+$') {
            [ShellHelper]::Achieved("Valid version tag.")
            break
        }

        [ShellHelper]::Error("Invalid version tag. Expected format: X.Y.Z (e.g. 6.2.0).")
    }

    git tag "v$version_tag"

    if (-not [ShellHelper]::TestLastExitCode("Create release version tag")) { return }

    git push origin "v$version_tag"

    if (-not [ShellHelper]::TestLastExitCode("Publish using created version tag")) { return }

    [ShellHelper]::Success("Release completed successfully!")

    #* 📝 Return to experimental.

    git switch experimental

    if (-not [ShellHelper]::TestLastExitCode("Return to starting branch experimental")) { return }

    [ShellHelper]::Success("Returned to branch experimental!")
}


Set-GDRepositoryPath

$branch = git branch --show-current

if ($branch -eq "experimental") {
    experimental_push
}
else {
    [ShellHelper]::Warning("Current branch is not experimental!")
}