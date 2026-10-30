# ⚓ Anchor for this module: [[full-release-anchor|full_release.ps1]]
#* 📝 This module contains the full release workflow,
#* 📝 considering the user is on branch experimental.

. (Join-Path $PSScriptRoot "get_project_root.ps1")
. (Join-Path $PSScriptRoot "lastexitcode_check.ps1")

function experimental_push {

    git add -A

    $message = (Read-Host "📦 Enter commit message").Trim()

    if (-not $message) {
        Write-Host "⚠️ Commit message cannot be empty."
        return
    }

    git commit -m $message

    if (-not (Test-LastExitCode)) { return }

    git push origin experimental

    if (-not (Test-LastExitCode)) { return }

    git switch main

    if (-not (Test-LastExitCode)) { return }

    #* 📝 Check whether the main working tree is clean.

    $main_status = git status --porcelain

    if (-not (Test-LastExitCode)) { return }

    if ($main_status) {
        Write-Host "⚠️ Main working tree is not clean!"
        return
    }

    #* 📝 Fetch the latest remote information.

    git fetch origin

    if (-not (Test-LastExitCode)) {
        throw "❌ Failed to fetch origin."
    }

    #* 📝 Compare local main with origin/main.

    $status = git rev-list --left-right --count main...origin/main

    if (-not (Test-LastExitCode)) {
        throw "❌ Failed to compare main with origin/main."
    }

    $counts = $status.Trim() -split '\s+'

    $LocalAhead = [int]$counts[0]
    $RemoteAhead = [int]$counts[1]

    if ($LocalAhead -ne 0 -or $RemoteAhead -ne 0) {
        Write-Host "⚠️ Main and origin/main are not synchronized."
        Write-Host "Local commits ahead: $LocalAhead"
        Write-Host "Remote commits ahead: $RemoteAhead"
        return
    }

    Write-Host "☑️ Main is synchronized with origin/main."

    #* 📝 Merge experimental into main.

    git merge experimental

    if (-not (Test-LastExitCode)) { return }

    git push origin main

    if (-not (Test-LastExitCode)) { return }

    #* 📝 Validate and create the version tag.

    $version_tag = (Read-Host "🏷️ Enter version release tag").Trim()

    if ($version_tag -match '^\d+\.\d+\.\d+$') {
        Write-Host "☑️ Valid version tag."
    }
    else {
        Write-Host "❌ Invalid version tag."
        return
    }

    git tag "v$version_tag"

    if (-not (Test-LastExitCode)) { return }

    git push origin "v$version_tag"

    if (-not (Test-LastExitCode)) { return }

    Write-Host "🎉 Release completed successfully!"

    #* 📝 Return to experimental.

    git switch experimental

    if (-not (Test-LastExitCode)) {
        Write-Host "❌ Return to branch experimental failed."
        return
    }

    Write-Host "🎉 Returned to branch experimental!"
}


Set-GDRepositoryPath

$branch = git branch --show-current

if ($branch -eq "experimental") {
    experimental_push
}
else {
    Write-Host "⚠️ Current branch is not experimental!"
}
