#* 📝 This module retrieves the project version currently from [pyproject.toml](https://github.com/Mangosaber2026/GeometricalDomination/blob/main/pyproject.toml) 

#* 📝 Imports the ShellHelper class containing reusable methods.
using module ../universal_shell_functions/shell_helper.psm1

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