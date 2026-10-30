#* 📝 Installs the latest version of GeometricalDomination

param(
    [string]$Version = "5.5.0"
)

py -3.14 -m pip install `
    --force-reinstall `
    --no-cache-dir `
    --index-url https://pypi.org/simple `
    "GeometricalDomination==$Version"

if ($LASTEXITCODE -ne 0) {
    throw "GeometricalDomination installation failed."
}