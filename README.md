# Proyecto Integrador: Sistema Distribuido de Streaming y Telemetría en Tiempo Real

Curso: Desarrollo de Aplicaciones (Taller 13)

Prototipo de arquitectura de microservicios con persistencia independiente
(Database-per-Service), usando Firebase BaaS, Django REST Framework y
observabilidad con New Relic.

## Integrantes y roles

| Integrante | Rol | Carpeta / Rama |
|---|---|---|
| Rosa | Arquitecta y Líder de Integración | `docs/` · `docs/arquitectura` |
| Antonela | Cloud & Backend (Firebase + Node.js) | `microservicio-node/` · `feat/firebase-node` |
| Angie | Microservices Developer (Django REST) | `microservicio-django/` · `feat/django-api` |
| Alex | DevOps / Observability (New Relic) | `microservicio-node/newrelic.js` · `feat/newrelic` |
| Jennifer | QA y Pruebas de Carga | `pruebas-carga/` · `feat/pruebas-carga` |

## Estructura del repositorio

```
├── README.md
├── .gitignore
├── .env.example
├── docs/                    # Diagrama, justificación DURS, informe final
├── microservicio-node/      # Node.js + Firebase + agente New Relic
├── microservicio-django/    # API REST Album / Track
└── pruebas-carga/           # Postman, scripts y evidencias
```

## Flujo de trabajo con Git

1. `main` está protegida: solo se cambia mediante Pull Request, que revisa y fusiona Rosa.
2. Cada integrante trabaja en su propia rama (ver tabla) y solo en su carpeta.
3. Antes de abrir un PR: `git pull origin main`.
4. Commits cortos y descriptivos, por ejemplo `feat: agrega modelo Track`.

## Seguridad

No subir nunca `serviceAccountKey.json`, `.env` ni la License Key de New Relic.
Las credenciales se comparten por un canal privado, no por el repositorio.

## Cómo ejecutar

### Microservicio Node.js
```bash
cd microservicio-node
npm install
node -r newrelic index.js
```

### Microservicio Django
```bash
cd microservicio-django
python -m venv venv
source venv/bin/activate    # En Windows: venv\Scripts\activate
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

## Entregables

- [ ] Diagrama de arquitectura (`docs/arquitectura.png`)
- [ ] Justificación DURS (`docs/justificacion-DURS.md`)
- [ ] Microservicio Node.js + Firebase
- [ ] Microservicio Django REST (`/api/albumes/`, `/api/tracks/`)
- [ ] Instrumentación New Relic (APM + Infraestructura)
- [ ] Pruebas de carga (mínimo 100 peticiones concurrentes) y evidencias
- [ ] Informe final (`docs/informe-final.md`)