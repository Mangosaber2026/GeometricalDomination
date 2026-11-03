# ⚓ Anchor for this module: [[check-code-anchor|check_code.ps1]] 
#* 📝 Checks Python code using Ruff.

#* 📝 Imports the ShellHelper class containing reusable functions
using module ./universal_shell_functions/shell_helper.psm1

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
        py -m ruff check $StartingPath --fix
    }

    else {
        py -m ruff check $StartingPath
    }

    if ([ShellHelper]::TestLastExitCode("Ruff check")) {
        [ShellHelper]::Success("Ruff check successful!")
    }
}

#* 📝 Sets the current path to the GD repository path
[ShellHelper]::SetGDRepositoryPath()

#* 📝 Invokes the code fixing function with the current path
Invoke-CodeFixing -StartingPath (Get-Location).Path