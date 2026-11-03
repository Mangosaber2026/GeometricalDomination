<#
.SYNOPSIS
📝 Provides reusable helper methods for PowerShell scripts.

.DESCRIPTION
This class contains general-purpose static methods for
input validation, user feedback, path management and
repository navigation.

.NOTES
Part of the ShellHelper utility collection.
#>
class ShellHelper {


    <#
    .SYNOPSIS
    📝 Indicates a successful operation and writes the given message to the user with a ☑️ emoji.

    .PARAMETER Message
    [string] The success message to be displayed.

    .INPUTS
    None.

    .OUTPUTS
    None.
    #>
    static [void] Achieved([string]$Message) {
        Write-Host "☑️ $Message" -ForegroundColor Green
    }


    <#
    .SYNOPSIS
    📝 Indicates a successful operation and writes the given message to the user with a 🎉 emoji.

    .PARAMETER Message
    [string] The success message to be displayed.

    .INPUTS
    None.

    .OUTPUTS
    None.
    #>
    static [void] Success([string]$Message) {
        Write-Host "🎉 $Message" -ForegroundColor Green
    }


    <#
    .SYNOPSIS
    📝 Indicates a warning and writes the given message to the user with a ⚠️ emoji.

    .PARAMETER Message
    [string] The warning message to be displayed.

    .INPUTS
    None.

    .OUTPUTS
    None.
    #>
    static [void] Warning([string]$Message) {
        Write-Host "⚠️ $Message" -ForegroundColor Yellow
    }


    <#
    .SYNOPSIS
    📝 Indicates an error and writes the given message to the user with a ❌ emoji.

    .PARAMETER Message
    [string] The error message to be displayed.

    .INPUTS
    None.

    .OUTPUTS
    None.
    #>
    static [void] Error([string]$Message) {
        Write-Host "❌ $Message" -ForegroundColor Red
    }


    <#
    .SYNOPSIS
    📝 Throws an error with the given message.

    .PARAMETER Message
    [string] The error message to be displayed.

    .INPUTS
    None.

    .OUTPUTS
    None.
    #>
    static [void] ThrowError([string]$Message) {
        throw "🚨 $Message"
    }


    <#
    .SYNOPSIS
    📝 Displays the given information to the user with a ℹ️ emoji.

    .PARAMETER Message
    [string] The information message to be displayed.

    .INPUTS
    None.

    .OUTPUTS
    None.
    #>
    static [void] Information([string]$Message) {
        Write-Host "ℹ️ $Message" -ForegroundColor Cyan
    }


    <#
    .SYNOPSIS
    📝 Displays the given path to the user with a 📂 emoji.

    .PARAMETER GivenPath
    [string] The path to be displayed.

    .INPUTS
    None.

    .OUTPUTS
    None.
    #>
    static [void] ShowPath([string]$GivenPath) {
        Write-Host "📂 $GivenPath" -ForegroundColor DarkYellow
    }


    <#
    .SYNOPSIS
    📝 Displays Python-related information to the user with a 🐍 emoji.

    .PARAMETER Message
    [string] The Python-related message to be displayed.

    .INPUTS
    None.

    .OUTPUTS
    None.
    #>
    static [void] ShowPyInfo([string]$Message) {
        Write-Host "🐍 $Message" -ForegroundColor DarkGreen
    }


    <#
    .SYNOPSIS
    📝 Displays a URL to the user with 🌐 🔗 emojis.

    .PARAMETER URL
    [string] The URL to be displayed.

    .INPUTS
    None.

    .OUTPUTS
    None.
    #>
    static [void] ShowURL([string]$URL) {
        Write-Host "🌐 🔗 URL: $URL" -ForegroundColor DarkMagenta
    }


    <#
    .SYNOPSIS
    📝 Tests the exit code of the last executed command.

    .DESCRIPTION
    This function checks the exit code of the last executed command, if the exit code is non-zero, it indicates a failure and displays an error message with the operation name and exit code.

    .PARAMETER Operation
    [string] The name of the operation that was executed, used for error reporting.

    .INPUTS
    None.

    .OUTPUTS
    [bool] Returns $true if the last exit code was zero (indicating success), otherwise returns $false.
    #>
    static [bool] TestLastExitCode([string]$Operation) {

        if ($null -ne $LASTEXITCODE -and $LASTEXITCODE -ne 0) {

            [ShellHelper]::Error("$Operation failed!")

            [ShellHelper]::Error("Exit code: $LASTEXITCODE")

            return $false
        }

        return $true
    }


    <#
    .SYNOPSIS
    📝 Gets a valid directory path from the user.

    .DESCRIPTION
    This function prompts the user to enter a directory path and checks if it exists.

    If the path is valid, it returns the absolute path. 
    
    Otherwise, it continues to prompt the user until a valid path is provided.

    .INPUTS
    None.

    .OUTPUTS
    [string] The absolute path of the valid directory.
    #>
    static [string] GetValidDirectoryPath() {

        while ($true) {

            [string]$Path = (Read-Host "📁 Enter desired path").Trim()

            if (Test-Path -LiteralPath $Path -PathType Container) {

                [ShellHelper]::Achieved("Valid directory path.")

                return (Resolve-Path -LiteralPath $Path).Path
            }

            [ShellHelper]::Warning("Invalid directory path. Please try again.")
        }

    return ""
    }


    <#
    .SYNOPSIS
    📝 Gets a valid string input from the user.

    .DESCRIPTION
    This function takes an input string and a list of valid choices. 
    
    It prompts the user to enter a string and checks if it matches any of the valid choices. 
    
    If it does, the function returns the input string, otherwise, it continues to prompt the user until a valid input is provided.

    .PARAMETER Prompt
    [string] The prompt message to display to the user.

    .PARAMETER ValidChoices
    [string[]] The list of strings of valid choices to validate against.
    #>
    static [string] ShellGetStr(
    [string] $Prompt,
    [string[]] $ValidChoices
    ) {

    while ($true) {

        [string]$UserChoice = (Read-Host $Prompt).Trim()

        if ($ValidChoices -contains $UserChoice) {
            return $UserChoice.ToLowerInvariant()
        }

        [ShellHelper]::Warning(
            "Invalid choice. Allowed values: $($ValidChoices -join ', ')"
        )
    }

    return ""
    }


    <#
    .SYNOPSIS
    📝 Ensures that the current working directory is set to the root of the repository.
    
    .DESCRIPTION
    This function calculates the repository root based on the script's location and compares it with the current working directory. 
    
    If they differ, it changes the working directory to the repository root and informs the user.

    .INPUTS
    None.

    .OUTPUTS
    None.
    #>
    static [void] SetGDRepositoryPath() {
        $RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)

        $CurrentPath = (Get-Location).Path
        
        [ShellHelper]::ShowPath("Module directory: $PSScriptRoot")
        [ShellHelper]::ShowPath("Calculated repository root: $RepoRoot")
        [ShellHelper]::ShowPath("Current directory: $CurrentPath")

        if ($CurrentPath -eq $RepoRoot) {
            [ShellHelper]::Achieved("Already operating from the correct repository path:")
            [ShellHelper]::ShowPath("$CurrentPath")
        }
        else {
            Set-Location $RepoRoot

            [ShellHelper]::Achieved("🔀 Working directory changed successfully.")
            [ShellHelper]::ShowPath("Current path: $(Get-Location)")
        }
    }

    <#
    .SYNOPSIS
    📝 Gets the root directory of the parent repository.

    .DESCRIPTION
    This function takes a starting path as input and uses Git to determine the root directory of the repository in the path.

    .PARAMETER StartPath
    [string] The starting path from which to search for the repository root.

    .INPUTS
    None.

    .OUTPUTS
    [string]
    The absolute path of the repository root as a string.
    #>
    static [string] GetRepositoryRoot([string]$StartPath) {

        # 📝 Validate the starting directory.
        if (-not (Test-Path -LiteralPath $StartPath -PathType Container)) {
            [ShellHelper]::ThrowError("The specified start path does not exist or is not a directory: $StartPath")
        }

        # 📝 Ask Git to locate the repository root.
        [string]$RepositoryRoot = & git -C $StartPath rev-parse --show-toplevel

        # 📝 Check whether Git successfully located the repository.
        if (-not [ShellHelper]::TestLastExitCode("Git repository root detection")) {
            [ShellHelper]::ThrowError("Could not determine the Git repository root.")
        }

        # 📝 Resolve and return the absolute directory path.
        return (Resolve-Path -LiteralPath $RepositoryRoot.Trim()).Path
    }
}