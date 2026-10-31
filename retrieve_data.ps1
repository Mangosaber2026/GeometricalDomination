# Retrieve all Python files recursively
$PythonFiles = Get-ChildItem -Path . -Filter "*.py" -File -Recurse

# Calculate statistics for each file
$FileStats = foreach ($File in $PythonFiles) {

    $LineCount = (Get-Content -LiteralPath $File.FullName |
        Measure-Object -Line).Lines

    [PSCustomObject]@{
        Name      = $File.Name
        FullPath  = $File.FullName
        SizeBytes = $File.Length
        LineCount = $LineCount
    }
}

# Display individual file statistics
$FileStats |
    Format-Table Name, SizeBytes, LineCount -AutoSize

# Calculate total statistics
$TotalLines = $FileStats |
    Measure-Object -Property LineCount -Sum

$TotalSize = $FileStats |
    Measure-Object -Property SizeBytes -Sum

$TotalFiles = $FileStats.Count

# Calculate average lines per file
$AverageLines = if ($TotalFiles -gt 0) {
    [math]::Round($TotalLines.Sum / $TotalFiles, 2)
}
else {
    0
}

# Display summary
Write-Host "`n📊 Codebase Statistics" -ForegroundColor Cyan
Write-Host "🐍 Python files: $TotalFiles"
Write-Host "📝 Total lines: $($TotalLines.Sum)"
Write-Host "💾 Total size: $($TotalSize.Sum) bytes"
Write-Host "📐 Average lines per file: $AverageLines"