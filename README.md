# Sistema distribuido de streaming y telemetría (Taller 13)

Microservicios con persistencia independiente (Database-per-Service):
- `microservicio-node/` – telemetría en Node.js + Express + Firebase (Cloud Firestore) + New Relic APM.
- `microservicio-django/` – catálogo (Album/Track) en Django REST Framework + SQLite.
- `pruebas-carga/` – colección Postman, scripts de carga y evidencias.

## 1. Microservicio Node.js (puerto 3000)
```powershell
cd microservicio-node
# Colocar serviceAccountKey.json aquí (NO se sube a Git, ver .gitignore)
npm install
# Sin APM:
npm start
```

Para iniciar con APM, usa otra terminal:
```powershell
$env:NEW_RELIC_LICENSE_KEY = "tu_license_key"
npm run start:apm
```
Endpoints: `GET /health`, `POST /reproducciones` (`{"usuario","trackId","titulo"}`), `GET /reproducciones` (últimas 20).
Reglas de Firestore (consola → Firestore → Reglas): `allow read, write: if false;`

## 2. Microservicio Django (puerto 8000)
```powershell
cd microservicio-django
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py runserver 8000
```
Endpoints: `/api/albumes/` y `/api/tracks/` (CRUD completo). Eliminar un álbum elimina sus pistas (CASCADE).

## 3. New Relic (infraestructura / host)
Instala el agente de infraestructura usando las instrucciones de New Relic para Windows. Verifica en la consola que el host y la aplicación aparezcan reportando datos. Mantén las claves fuera del repositorio.

## 4. Pruebas de carga (≥100 concurrentes)
```bash
node pruebas-carga/scripts/carga.js http://localhost:3000/health 500 100
node pruebas-carga/scripts/carga.js http://localhost:3000/reproducciones 300 100
node pruebas-carga/scripts/carga.js http://localhost:8000/api/albumes/ 500 100
# o: pruebas-carga/scripts/ab_curl.sh <url> 200 100   |   importar postman_collection.json
```

## 5. Inicio rápido en Windows (PowerShell)
```powershell
# Terminal 1 - Django (puerto 8000)
.\iniciar-django.ps1
# Terminal 2 - Node + New Relic (puerto 3000); requiere microservicio-node\serviceAccountKey.json
.\iniciar-node.ps1 -LicenseKey "TU_LICENSE_KEY"
# Terminal 3 - Pruebas de carga (100 concurrentes)
.\pruebas-carga\ejecutar-carga.ps1
```

El informe final se conserva en el documento PDF del equipo; este repositorio contiene el código y las evidencias técnicas.
