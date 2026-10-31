using module ../universal_shell_functions/shell_helper.psm1

Import-Module (Join-Path $PSScriptRoot "doc_file_generator.psm1") -Force

[string]$DesiredPath = [ShellHelper]::GetValidDirectoryPath()

New-GDDocumentationStructure -TargetPath $DesiredPath