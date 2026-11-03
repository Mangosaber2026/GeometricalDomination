#* 📝 Documentation Generator for GeometricalDomination

#* 📝 Imports ShellHelper class containing reusable functions
using module ../universal_shell_functions/shell_helper.psm1

<#
.SYNOPSIS
📝 Generates a documentation directory in a specified path with Markdown files for each Python module, and an images directory.

.DESCRIPTION
This function takes a target directory path as input and generates a documentation structure for the Python modules found directly inside that directory.

It creates a new directory named after the target directory with a "_docs" suffix, containing Markdown files for each Python module and an "images" subdirectory.

.PARAMETER TargetPath
[string] The absolute or relative path to the target directory where the documentation structure will be generated.

.INPUTS
None.

.OUTPUTS
None.
#>
function New-GDDocumentationStructure {
    param (
        [Parameter(Mandatory)]
        [string]$TargetPath
    )

    try {
        #* 📝 Resolve relative paths
        if (-not [System.IO.Path]::IsPathRooted($TargetPath)) {
            $TargetPath = Join-Path (Get-Location).Path $TargetPath
        }

        #* 📝 Validate target directory
        if (-not (Test-Path -LiteralPath $TargetPath -PathType Container)) {
            [ShellHelper]::ThrowError("Target directory does not exist: $TargetPath")
        }

        #* 📝 Resolve absolute path
        $TargetPath = (Resolve-Path -LiteralPath $TargetPath -ErrorAction Stop).Path

        #* 📝 Discover Python files directly inside the directory
        $PythonFiles = @(
            Get-ChildItem -LiteralPath $TargetPath -Filter "*.py" -File -ErrorAction Stop
        )

        $FileCount = $PythonFiles.Count

        [ShellHelper]::ShowPath("Target directory: $TargetPath")
        [ShellHelper]::ShowPyInfo("Python files found: $FileCount")

        if ($FileCount -eq 0) {
            [ShellHelper]::Warning("No Python files found. Documentation templates will not be generated.")
        }

        #* 📝 Define documentation directory paths
        $DirectoryName = Split-Path $TargetPath -Leaf
        $DocsDirectoryName = "${DirectoryName}_docs"

        $DocsPath = Join-Path $TargetPath $DocsDirectoryName
        $ImagesPath = Join-Path $DocsPath "images"

        #* 📝 Create directories
        New-Item -Path $DocsPath -ItemType Directory -Force -ErrorAction Stop | Out-Null
        New-Item -Path $ImagesPath -ItemType Directory -Force -ErrorAction Stop | Out-Null

        [ShellHelper]::Achieved("📁 Documentation directory prepared.")
        [ShellHelper]::Achieved("🖼️ Images directory prepared.")

        #* 📝 Generate Markdown documentation files
        foreach ($PythonFile in $PythonFiles) {

            $ModuleName = $PythonFile.BaseName
            $DocumentationFileName = "$ModuleName.md"
            $DocumentationFilePath = Join-Path $DocsPath $DocumentationFileName

            #* 📝 Preserve existing documentation
            if (Test-Path -LiteralPath $DocumentationFilePath -PathType Leaf) {
                [ShellHelper]::Information("Documentation already exists: $DocumentationFileName")
                continue
            }

            #* 📝 Construct readable module title
            $Title = [System.Globalization.CultureInfo]::InvariantCulture.TextInfo.ToTitleCase(
                ($ModuleName -replace '[\_-]+', ' ').Trim().ToLowerInvariant()
            )

            #* 📝 Define Markdown template
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

            #* 📝 Create Markdown file
            Set-Content -LiteralPath $DocumentationFilePath `
                -Value $DocumentationContent `
                -Encoding utf8 `
                -ErrorAction Stop

            [ShellHelper]::Information("📝 Created documentation: $DocumentationFileName")
        }

        [ShellHelper]::Success("Documentation structure generated successfully!")
    }
    catch {
        [ShellHelper]::ThrowError("Documentation generation failed: $($_.Exception.Message)")
    }
}
