
Import-Module (
    Join-Path (
        Split-Path $PSScriptRoot -Parent
    ) "universal_shell_functions\lastexitcode_check.psm1"
) -Force

function New-GDDocumentationStructure {
    param (
        [Parameter(Mandatory)]
        [string]$TargetPath
    )

    # Resolve relative paths
    if (-not [System.IO.Path]::IsPathRooted($TargetPath)) {
        $TargetPath = Join-Path (Get-Location).Path $TargetPath
    }

    # Validate target directory
    if (-not (Test-Path -LiteralPath $TargetPath -PathType Container)) {
        throw "❌ Target directory does not exist: $TargetPath"
    }

    # Resolve the absolute path
    $TargetPath = (Resolve-Path -LiteralPath $TargetPath).Path

    # Discover Python files directly inside the directory
    $PythonFiles = Get-ChildItem -Path $TargetPath -Filter "*.py" -File

    # Count discovered files
    $FileCount = $PythonFiles.Count

    Write-Host "📂 Target directory: $TargetPath"
    Write-Host "🐍 Python files found: $FileCount"

    # Define documentation directory paths
    $DirectoryName = Split-Path $TargetPath -Leaf
    $DocsDirectoryName = "${DirectoryName}_docs"

    $DocsPath = Join-Path $TargetPath $DocsDirectoryName
    $ImagesPath = Join-Path $DocsPath "images"

    # Create directories if they do not already exist
    New-Item -Path $DocsPath -ItemType Directory -Force | Out-Null
    New-Item -Path $ImagesPath -ItemType Directory -Force | Out-Null

    Write-Host "📁 Documentation directory prepared."
    Write-Host "🖼️ Images directory prepared."

    # Generate Markdown documentation files
    foreach ($PythonFile in $PythonFiles) {

    # Extract module name and construct documentation filename
    $ModuleName = $PythonFile.BaseName
    $DocumentationFileName = "$ModuleName.md"
    $DocumentationFilePath = Join-Path $DocsPath $DocumentationFileName

    # Only generate files that do not already exist
    if (-not (Test-Path -LiteralPath $DocumentationFilePath)) {

        # Construct a readable module title
        $Title = [System.Globalization.CultureInfo]::InvariantCulture.TextInfo.ToTitleCase(
            ($ModuleName -replace '[_-]+', ' ').Trim().ToLowerInvariant()
        )

        # Define Markdown template
        $DocumentationContent = @"
# $Title

## Preview

![${Title}](images/${ModuleName}.png)

## Overview

## Classes

## Functions

## Source Code

[View source code](../$($PythonFile.Name))
"@

        # Create Markdown file with its template
        Set-Content -LiteralPath $DocumentationFilePath `
            -Value $DocumentationContent -Encoding utf8

        Write-Host "📝 Created documentation: $DocumentationFileName"
    }
    else {
        Write-Host "⏭️ Documentation already exists: $DocumentationFileName"
    }
    }
}