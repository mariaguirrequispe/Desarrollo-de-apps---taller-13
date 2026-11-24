# Uso (PowerShell):  .\iniciar-node.ps1 -LicenseKey "tu_license_key"
param([Parameter(Mandatory=$true)][string]$LicenseKey)
Set-Location "$PSScriptRoot\microservicio-node"
if (-not (Test-Path "serviceAccountKey.json")) { Write-Host "Falta serviceAccountKey.json en microservicio-node/ (pidela a Antonela por canal privado)" -ForegroundColor Red; exit 1 }
if (-not (Test-Path "node_modules")) { npm install }
$env:NEW_RELIC_LICENSE_KEY = $LicenseKey
node -r newrelic index.js
