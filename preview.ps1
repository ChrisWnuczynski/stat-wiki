$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
if (-not (Test-Path ".\notes\index.qmd")) {
  python .\build_wiki.py
}
quarto preview --port 4099
