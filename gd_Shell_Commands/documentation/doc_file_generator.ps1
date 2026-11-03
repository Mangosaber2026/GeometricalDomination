#* 📝 Imports the class ShellHelper containing reusable functions
using module ../universal_shell_functions/shell_helper.psm1

#* 📝 Imports the module doc_file_generator.psm1 containing the function New-GDDocumentationStructure
Import-Module (Join-Path $PSScriptRoot "doc_file_generator.psm1") -Force

#* 📝 Gets a valid directory path from the user
[string]$DesiredPath = [ShellHelper]::GetValidDirectoryPath()

#* 📝 Generates the documentation structure for the specified directory
New-GDDocumentationStructure -TargetPath $DesiredPath