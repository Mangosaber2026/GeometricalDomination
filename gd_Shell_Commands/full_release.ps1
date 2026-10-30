

function experimental_push {

    git add -A

    $message = Read-Host "Enter commit message"

    if (-not $message.Trim()) {
        Write-Host "Commit message cannot be empty."
        return
    }

    git commit -m $message

    if ($LASTEXITCODE -ne 0) { return }

    git push origin experimental

    if ($LASTEXITCODE -ne 0) { return }

    git switch main

    if ($LASTEXITCODE -ne 0) { return }

    $main_status = git status --porcelain

    if (-not $main_status) {

        git merge experimental

        if ($LASTEXITCODE -ne 0) { return }

        git push origin main

        if ($LASTEXITCODE -ne 0) { return }

        $version_tag = Read-Host "Enter version release tag: "

        if ($version_tag -match '^\d+\.\d+\.\d+$') {
            Write-Host "Valid version tag."
            }
        else {
            Write-Host "Invalid version tag."
            }

        git tag "v$version_tag"

        if ($LASTEXITCODE -ne 0) { return }

        git push origin "v$version_tag"

        if ($LASTEXITCODE -ne 0) { return }

        Write-Host "Release completed successfully!"

    }
    else {
        Write-Host "Main working tree is not clean."
    }
}


$branch = git branch --show-current

if ($branch -eq "experimental") {
    experimental_push
}
else {
    Write-Host "Not on experimental."
}

