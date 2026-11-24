# Sistema distribuido de streaming y telemetría (Taller 13)

Microservicios con persistencia independiente (Database-per-Service):
- `microservicio-node/` – telemetría en Node.js + Express + Firebase (Cloud Firestore) + New Relic APM.
- `microservicio-django/` – catálogo (Album/Track) en Django REST Framework + SQLite.
- `pruebas-carga/` – colección Postman, scripts de carga y evidencias.
- `docs/` – arquitectura, justificación DURS e informe.

## 1. Microservicio Node.js (puerto 3000)
```bash
cd microservicio-node
# Colocar serviceAccountKey.json aquí (NO se sube a Git, ver .gitignore)
npm install
npm start                     # sin APM
export NEW_RELIC_LICENSE_KEY=<tu_license_key>   # región United States
npm run start:apm             # node -r newrelic index.js
```
Endpoints: `GET /health`, `POST /reproducciones` (`{"usuario","trackId","titulo"}`), `GET /reproducciones` (últimas 20).
Reglas de Firestore (consola → Firestore → Reglas): `allow read, write: if false;`

## 2. Microservicio Django (puerto 8000)
```bash
cd microservicio-django
python -m venv venv && source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000
```
Endpoints: `/api/albumes/` y `/api/tracks/` (CRUD completo). Eliminar un álbum elimina sus pistas (CASCADE).

## 3. New Relic (infraestructura / host)
Instalar el agente de infraestructura con el comando que genera New Relic en *Add data → Linux/Windows* (`newrelic-cli`), por ejemplo en Linux:
```bash
curl -Ls https://download.newrelic.com/install/newrelic-cli/scripts/install.sh | bash
sudo NEW_RELIC_API_KEY=<USER_API_KEY> NEW_RELIC_ACCOUNT_ID=<ID> NEW_RELIC_REGION=US /usr/local/bin/newrelic install
```
Verificar en la consola el estado **See your data** y revisar `newrelic_agent.log`.

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
Ver `docs/CHECKLIST-ENTREGA.md` para las evidencias (capturas) por adjuntar.
