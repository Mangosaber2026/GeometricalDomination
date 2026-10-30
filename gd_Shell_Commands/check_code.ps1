# ⚓ Anchor for this module: [[check-code-anchor|check_code.ps1]] 
#* 📝 Checks Python code using Ruff.

. (Join-Path $PSScriptRoot "get_project_root.ps1")

function Invoke-CodeFixing {
    $fixCode = (Read-Host "Do you want to fix the code too with ruff? (y/n)").Trim()

    if ($fixCode -notin ("y", "n")) {
        Write-Host "⚠️ Invalid input."
        return
    }

    if ($fixCode -eq "y") {
        py -3.14 -m ruff check . --fix
    }

    else {
        py -3.14 -m ruff check .
    }

    if ($LASTEXITCODE -ne 0) {
        throw "❌ Ruff found errors in the code."
    }

    else {
        Write-Host "🎉 Ruff check successful!"
    }
}

Set-GDRepositoryRoot

Invoke-CodeFixing