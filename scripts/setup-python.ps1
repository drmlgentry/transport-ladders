param(
  [string]$PythonExe = "python"
)
$ErrorActionPreference = "Stop"

# Create venv
if (-not (Test-Path ".venv")) {
  & $PythonExe -m venv .venv
}

# Activate (PowerShell)
. .\.venv\Scripts\Activate.ps1

# Upgrade pip + install editable package
python -m pip install --upgrade pip setuptools
python -m pip install -e .

Write-Host "Python environment ready. Activate later with:" -ForegroundColor Green
Write-Host "  . .\.venv\Scripts\Activate.ps1" -ForegroundColor Gray
