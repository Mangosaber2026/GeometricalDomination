# ⚓ Anchor for this module: [[force-install-anchor|force_install.ps1]] 
#* 📝 Installs a selected version of GeometricalDomination

#* 📝 Imports the ShellHelper class containing reusable functions
using module ./universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
Gets a version of GeometricalDomination from the user.

.DESCRIPTION
This function prompts the user to input a desired version of GeometricalDomination to install. 

It validates the input to ensure it matches the expected format (X.Y.Z) and returns the valid version tag.

.INPUTS
None.

.OUTPUTS
[string]
The valid version tag of GeometricalDomination.
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

#* 📝 Throws an error if no valid version is provided
if (-not $Version) {
    [ShellHelper]::ThrowError("Installation cancelled: no valid version provided.")
}

#* 📝 Contains necessary pip arguments to force install a specific version of GeometricalDomination
$PipArgs = @(
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

#* 📝 Checks the exit code of the pip install command and reports success or failure
if ([ShellHelper]::TestLastExitCode("GeometricalDomination version $Version installation")) {
    [ShellHelper]::Success("GeometricalDomination version $Version installation complete!")
}