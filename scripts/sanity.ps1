$ErrorActionPreference = "Stop"
. .\.venv\Scripts\Activate.ps1

Write-Host "Python:" -ForegroundColor Cyan
python --version

Write-Host "`nPackage import:" -ForegroundColor Cyan
python -c "import transport_ladders; print('transport_ladders OK')"

Write-Host "`nTests:" -ForegroundColor Cyan
python -m unittest discover -s tests -p "test_*.py" -q

Write-Host "`nLaTeX:" -ForegroundColor Cyan
latexmk -v
