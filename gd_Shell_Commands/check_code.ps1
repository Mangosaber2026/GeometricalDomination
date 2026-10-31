# ⚓ Anchor for this module: [[check-code-anchor|check_code.ps1]] 
#* 📝 Checks Python code using Ruff.

using module ./universal_shell_functions/shell_helper.psm1
Import-Module (Join-Path $PSScriptRoot "universal_shell_functions\get_project_root.psm1") -Force

<#
.SYNOPSIS
Checks Python code using Ruff.
#>
function Invoke-CodeFixing([string]$StartingPath) {
    $fixCode = [ShellHelper]::ShellGetStr(
        "Do you want to fix the code too with ruff? (y/n)",
        @("y", "n")
        )

    [ShellHelper]::Information("Current path: $StartingPath")
    [ShellHelper]::Information("Ruff check has started ...")

    if ($fixCode -eq "y") {
        py -3.14 -m ruff check $StartingPath --fix
    }

    else {
        py -3.14 -m ruff check $StartingPath
    }

    if ([ShellHelper]::TestLastExitCode("Ruff check")) {
        [ShellHelper]::Success("Ruff check successful!")
    }
}

Set-GDRepositoryPath

Invoke-CodeFixing -StartingPath (Get-Location).Path