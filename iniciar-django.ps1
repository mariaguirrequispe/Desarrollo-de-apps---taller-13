# Uso (PowerShell):  .\iniciar-django.ps1
Set-Location "$PSScriptRoot\microservicio-django"
if (-not (Test-Path "venv")) { python -m venv venv }
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py runserver 8000
