param(
  [string]$PaperDir = (Join-Path $PSScriptRoot "..\paper"),
  [string]$OutDir   = (Join-Path $PSScriptRoot "..\output"),
  [switch]$Clean
)
$ErrorActionPreference = "Stop"
New-Item -Force -ItemType Directory $OutDir | Out-Null

Push-Location $PaperDir
if ($Clean) {
  latexmk -C
  Pop-Location
  exit 0
}

latexmk -pdf -interaction=nonstopmode -halt-on-error iiib_main.tex
Copy-Item -Force (Join-Path $PaperDir "iiib_main.pdf") (Join-Path $OutDir "iiib_main.pdf")
Write-Host "Done: $OutDir\iiib_main.pdf" -ForegroundColor Green
Pop-Location
