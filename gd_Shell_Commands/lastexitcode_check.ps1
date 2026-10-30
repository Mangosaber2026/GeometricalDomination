# ⚓ Anchor for this module: [[lastexitcode-check-anchor|lastexitcode_check.ps1]] 

function Test-LastExitCode {
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ The previous command failed (Exit code: $LASTEXITCODE)."
        return $false
    }

    return $true
}