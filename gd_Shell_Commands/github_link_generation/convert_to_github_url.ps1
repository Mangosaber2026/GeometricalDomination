<#
.SYNOPSIS
📝 Converts a repository-relative file path to a full GitHub URL for the GeometricalDomination repository.

.DESCRIPTION
This function takes a relative file path within the GeometricalDomination repository and constructs a full GitHub URL pointing to that file in the main branch of the repository.

.PARAMETER RepositoryRelativePath
[string] The relative path of the target file within the GeometricalDomination repository.

.INPUTS
None.

.OUTPUTS
[string]
The full GitHub URL corresponding to the provided repository-relative path.
#>
function ConvertTo-GDGitHubURL {
    param (
        [Parameter(Mandatory)]
        [string]$RepositoryRelativePath
    )

    #* 📝 Define the GitHub repository base URL.
    $GitHubBaseURL = "https://github.com/Mangosaber2026/GeometricalDomination/blob/main/"

    #* 📝 Convert Windows path separators into URL path separators.
    $GitHubRelativePath = $RepositoryRelativePath.Replace('\', '/')

    #* 📝 Combine the base URL with the relative path.
    $FullGitHubURL = $GitHubBaseURL + $GitHubRelativePath

    #* 📝 Output the full GitHub URL.
    return $FullGitHubURL
}