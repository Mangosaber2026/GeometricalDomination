# ⚓ Anchor for this module: [[force-install-anchor|force_install.ps1]] 
#* 📝 Installs a selected version of GeometricalDomination

using module ./universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
Gets a version of GeometricalDomination from the user.
#>
function install_version {
    while ($true) {
        $version_tag = (Read-Host "📦 Enter desired installation version").Trim()

        if ($version_tag -match '^\d+\.\d+\.\d+$') {
            [ShellHelper]::Achieved("Valid version tag.")
            return $version_tag
        }

        [ShellHelper]::Error("Invalid version tag. Expected format: X.Y.Z (e.g. 6.2.0).")
    }
}

$Version = install_version

if (-not $Version) {
    throw "❌ Installation cancelled: no valid version provided."
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

if ([ShellHelper]::TestLastExitCode("GeometricalDomination version $Version installation")) {
    [ShellHelper]::Success("GeometricalDomination version $Version installation complete!")
}