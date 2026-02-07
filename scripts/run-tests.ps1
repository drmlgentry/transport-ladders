$ErrorActionPreference = "Stop"
if (-not (Test-Path ".\.venv\Scripts\Activate.ps1")) {
  throw "Missing venv. Run .\scripts\setup-python.ps1 first."
}
. .\.venv\Scripts\Activate.ps1

python -m unittest discover -s tests -p "test_*.py" -q
Write-Host "Tests: OK" -ForegroundColor Green
