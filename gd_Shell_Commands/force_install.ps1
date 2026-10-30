# ⚓ Anchor for this module: [[force-install-anchor|force_install.ps1]] 
#* 📝 Installs a selected version of GeometricalDomination

function install_version {
    $Version = (Read-Host "📦 Enter desired installation version").Trim()

    if ($Version -notmatch '^\d+\.\d+\.\d+$') {
        Write-Host "❌ Invalid version tag."
        return
    }

    Write-Host "☑️ Valid version tag."
    return $Version
}

$Version = install_version

if (-not $Version) {
    throw "Installation cancelled: no valid version provided."
}

$PipArgs = @(
    "-3.14"
    "-m"
    "pip"
    "install"
    "--force-reinstall"
    "--no-cache-dir"
    "--index-url"
    "https://pypi.org/simple"
    "GeometricalDomination==$Version"
)

& py @PipArgs

if ($LASTEXITCODE -ne 0) {
    throw "❌ GeometricalDomination installation failed."
}

Write-Host "🎉 GeometricalDomination version $Version installation complete!"
