#* Checks Python code using Ruff.

param (
    [bool]$FixCode = $false
)

if ($FixCode) {
    py -3.14 -m ruff check . --fix
}

else {
    py -3.14 -m ruff check .
}

if ($LASTEXITCODE -ne 0) {
    throw "Ruff found errors in the code."
}