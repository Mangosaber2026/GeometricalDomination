class ShellHelper {

    static [void] Achieved([string]$Message) {
        Write-Host "☑️ $Message" -ForegroundColor Green
    }

    static [void] Success([string]$Message) {
        Write-Host "🎉 $Message" -ForegroundColor Green
    }

    static [void] Warning([string]$Message) {
        Write-Host "⚠️ $Message" -ForegroundColor Yellow
    }

    static [void] Error([string]$Message) {
        Write-Host "❌ $Message" -ForegroundColor Red
    }

    static [void] Information([string]$Message) {
        Write-Host "ℹ️ $Message" -ForegroundColor Cyan
    }

    static [void] ShowPath([string]$GivenPath) {
        Write-Host "📂 $GivenPath" -ForegroundColor DarkYellow
    }

    static [void] ShowPyInfo([string]$Message) {
        Write-Host "🐍 $Message" -ForegroundColor DarkGreen
    }

    static [bool] TestLastExitCode([string]$Operation) {

        if ($null -ne $LASTEXITCODE -and $LASTEXITCODE -ne 0) {

            [ShellHelper]::Error("$Operation failed!")

            [ShellHelper]::Error("Exit code: $LASTEXITCODE")

            return $false
        }

        return $true
    }

    static [string] GetValidDirectoryPath() {

    while ($true) {

        [string]$Path = (Read-Host "📁 Enter desired path").Trim()

        if (Test-Path -LiteralPath $Path -PathType Container) {

            [ShellHelper]::Achieved("Valid directory path.")

            return (Resolve-Path -LiteralPath $Path).Path
        }

        [ShellHelper]::Warning("Invalid directory path. Please try again.")
    }

    return ""
    }

    static [string] ShellGetStr(
    [string] $Prompt,
    [string[]] $ValidChoices
    ) {

    while ($true) {

        [string]$UserChoice = (Read-Host $Prompt).Trim()

        if ($ValidChoices -contains $UserChoice) {
            return $UserChoice.ToLowerInvariant()
        }

        [ShellHelper]::Warning(
            "Invalid choice. Allowed values: $($ValidChoices -join ', ')"
        )
    }

    return ""
    }
}