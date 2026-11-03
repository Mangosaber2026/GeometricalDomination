#* 📝 This script generates a GitHub URL for a target file within the GeometricalDomination repository.

#* 📝 Imports ShellHelper, containing reusable functions
using module ../universal_shell_functions/shell_helper.psm1

Import-Module (Join-Path $PSScriptRoot "get_target_file.ps1") -Force
Import-Module (Join-Path $PSScriptRoot "convert_to_repository_relative_path.ps1") -Force
Import-Module (Join-Path $PSScriptRoot "convert_to_github_url.ps1") -Force

#* 📝 Discover the repository root.
$GeneratorDirectory = $PSScriptRoot

$RepositoryRoot = [ShellHelper]::GetRepositoryRoot($GeneratorDirectory)

#* 📝 Identify the target file.
$TargetFile = Get-GDTargetFile `
    -RepositoryRoot $RepositoryRoot

#* 📝 Generate the repository-relative path.
$RelativePath = ConvertTo-GDRepositoryRelativePath `
    -RepositoryRoot $RepositoryRoot `
    -TargetFile $TargetFile

#* 📝 Generate the GitHub URL.
$GitHubURL = ConvertTo-GDGitHubURL `
    -RepositoryRelativePath $RelativePath

#* 📝 Display the generated URL.
[ShellHelper]::ShowURL($GitHubURL)