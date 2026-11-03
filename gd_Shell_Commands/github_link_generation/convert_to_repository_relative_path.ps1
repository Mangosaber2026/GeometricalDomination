#* 📝 Imports ShellHelper class containing reusable functions
using module ../universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
📝 Converts an absolute file path to a repository-relative path within the GeometricalDomination repository.

.DESCRIPTION
Takes an absolute file path and a repository root path.

Both inputs are validated to ensure they exist and that the target file is located within the repository root. 
The function then computes and returns the relative path of the target file with respect to the repository root.

.PARAMETER RepositoryRoot
The absolute repository path of GeometricalDomination in a string.

.PARAMETER TargetFile
The absolute path of the target file within the GeometricalDomination repository in a string.

.INPUTS
None.

.OUTPUTS
[string]
The repository-relative path of the target file.
#>
function ConvertTo-GDRepositoryRelativePath {
    param (
        [Parameter(Mandatory)]
        [string]$RepositoryRoot,

        [Parameter(Mandatory)]
        [string]$TargetFile
    )

    #* 📝 Validate the repository directory.
    if (-not (Test-Path -LiteralPath $RepositoryRoot -PathType Container)) {
        [ShellHelper]::ThrowError("Invalid repository directory: $RepositoryRoot")
    }

    #* 📝 Validate the target file.
    if (-not (Test-Path -LiteralPath $TargetFile -PathType Leaf)) {
        [ShellHelper]::ThrowError("Invalid target file: $TargetFile")
    }

    #* 📝 Normalize both paths to their absolute representations.
    $NormalizedRoot = [System.IO.Path]::GetFullPath($RepositoryRoot)
    $NormalizedTarget = [System.IO.Path]::GetFullPath($TargetFile)

    #* 📝 Establish the repository directory boundary.
    $RepositoryPrefix = $NormalizedRoot.TrimEnd('\', '/') + '\'

    #* 📝 Ensure the target file resides within the repository directory.
    if (-not $NormalizedTarget.StartsWith($RepositoryPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        [ShellHelper]::ThrowError("The target file '$TargetFile' is not located within the repository root '$RepositoryRoot'.")
    }

    #* 📝 Convert the target file path into a repository-relative path.
    return [System.IO.Path]::GetRelativePath(
        $NormalizedRoot,
        $NormalizedTarget
    )
}
