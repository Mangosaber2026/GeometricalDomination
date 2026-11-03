#* 📝 Imports ShellHelper class containing reusable functions
using module ../universal_shell_functions/shell_helper.psm1


<#
.SYNOPSIS
Gets the absolute path of a target file within the GeometricalDomination repository based on user input.

.DESCRIPTION
This function takes the repository root as input and prompts the user to enter a filename. 

It searches for the specified file within the repository, excluding the .git directory. 

If multiple files with the same name are found, it allows the user to select the desired file from a list. 

The function returns the absolute path of the selected file.

.PARAMETER RepositoryRoot
The absolute path to the root directory of the GeometricalDomination repository in a string.

.INPUTS
None.

.OUTPUTS
[string]
The absolute path of the selected target file as a string.
#>
function Get-GDTargetFile {
    param (
        [Parameter(Mandatory)]
        [string]$RepositoryRoot
    )

    #* 📝 Validate the repository directory.
    if (-not (Test-Path -LiteralPath $RepositoryRoot -PathType Container)) {
        [ShellHelper]::ThrowError("Invalid repository directory: $RepositoryRoot")
    }

    while ($true) {

        #* 📝 Request a filename from the user.
        $FileName = (Read-Host "Enter the filename to search for (e.g., 'example.py')").Trim()

        #* 📝 Validate the filename input.
        if ([string]::IsNullOrWhiteSpace($FileName)) {
            [ShellHelper]::Warning("Filename cannot be empty. Please try again.")
            continue
        }

        #* 📝 Search the repository recursively.
        $MatchingFiles = @(
            Get-ChildItem -LiteralPath $RepositoryRoot -File -Recurse -ErrorAction Stop |
                Where-Object {
                    $_.Name -eq $FileName -and
                    $_.FullName -notmatch '[\\/]\.git[\\/]'
                }
        )

        #* 📝 Handle the case where no files were found.
        if ($MatchingFiles.Count -eq 0) {
            [ShellHelper]::Warning("No files found with the name '$FileName'. Please try again.")
            continue
        }

        #* 📝 Return the absolute path if exactly one file was found.
        if ($MatchingFiles.Count -eq 1) {
            return $MatchingFiles[0].FullName
        }

        #* 📝 Display all matching files if multiple files were found.
        [ShellHelper]::Information("`nFound multiple files with the name '$FileName':")

        for (
            $Index = 0; 
            $Index -lt $MatchingFiles.Count; 
            $Index++
            ) {
            [ShellHelper]::Information("[$($Index + 1)] $($MatchingFiles[$Index].FullName)")
        }

        #* 📝 Let the user select the desired file.
        while ($true) {
            $Selection = (Read-Host "Enter the number of your desired file").Trim()

            if ($Selection -match '^\d+$') {
                $SelectionNumber = [int]$Selection

                if ($SelectionNumber -ge 1 -and $SelectionNumber -le $MatchingFiles.Count) {
                    return $MatchingFiles[$SelectionNumber - 1].FullName
                }
            }

            [ShellHelper]::Warning("Invalid selection. Please enter one of the displayed numbers.")
        }
    }
}