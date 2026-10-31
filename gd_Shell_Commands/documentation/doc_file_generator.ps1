

Import-Module (Join-Path $PSScriptRoot "doc_file_generator.psm1") -Force

[string]$DesiredPath = (Read-Host "Enter desired path").Trim()

New-GDDocumentationStructure -TargetPath $DesiredPath