# ⚓ Anchor for this module: [[get-project-root-anchor|get_project_root.ps1]] 
#* 📂 Ensures that PowerShell is operating from the Geometrical Domination repository root.

function Set-GDRepositoryPath {
    $RepoRoot = Split-Path -Parent $PSScriptRoot
    $CurrentPath = (Get-Location).Path

    if ($CurrentPath -eq $RepoRoot) {
        Write-Host "✅ Already operating from the correct repository path:"
        Write-Host "📂 $CurrentPath"
    }
    else {
        Set-Location $RepoRoot

        Write-Host "🔀 Working directory changed successfully."
        Write-Host "📂 Current path: $(Get-Location)"
    }
}
