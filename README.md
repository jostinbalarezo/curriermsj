# CurrierMsj — Bot courier EE.UU. -> Ecuador + Dashboard Administrativo

Sistema de atención y registro de envíos para paquetes que viajan desde Estados Unidos hacia Ecuador. El canal principal es **WhatsApp Business Cloud API**, el backend es **Flask** y los datos se guardan en **Supabase**. El panel administrativo es una SPA en **React + Chakra UI (Horizon UI)** con **Vite**.

---

## Componentes del Sistema

| Componente | Tecnología | Ubicación |
|---|---|---|
| **WhatsApp Bot** | Python / Flask / httpx | `bot-mensajeria/` |
| **Dashboard Admin** | React 19 / Chakra UI / Recharts / Vite | `dashboard/` |
| **Base de Datos** | Supabase PostgreSQL | Remoto |
| **WhatsApp API** | Meta Cloud API v20.0 | — |

---

## WhatsApp Bot (`bot-mensajeria/`)

### Funcionalidades

- Atiende mensajes entrantes de WhatsApp mediante webhook (`/webhook`)
- Menú interactivo: rastrear, cotizar, ver envíos, reportar problemas, hablar con agente
- Cotización EE.UU. -> Ecuador por tipo de paquete y peso
- Registro de envíos confirmados en Supabase con tracking code auto-generado (`CUR-00001`)
- Estado de conversación persistido por número de teléfono
- FAQ con auto-respuesta por palabra clave
- Reportes e incidencias con formato `#INC-{id:04d}`
- 13-step wizard para registro de nuevos envíos
- Sistema de tracking visual con barra de progreso

### API Endpoints

| Ruta | Método | Propósito |
|---|---|---|
| `/webhook` | GET | Verificación Meta Webhook (challenge) |
| `/webhook` | POST | Recepción de mensajes WhatsApp |
| `/health` | GET | Health check del servicio |
| `/api/envios` | GET | Todos los envíos (orden descendente) |
| `/api/system-stats` | GET | Clientes, estados y reportes |

### Flujo del Bot

```
WhatsApp → Meta Cloud API → ngrok → Flask webhook → CourierBot → Supabase
                                                         ↓
                                                    WhatsAppClient → respuesta
```

### Estado de Envíos

| Paso | Estado | Descripción |
|---|---|---|
| 1 | `pendiente` | Solicitud registrada |
| 2 | `recibido` | Paquete recibido |
| 3 | `en_transito` | En camino al hub |
| 4 | `en_ruta` | En ruta de entrega |
| 5 | `entregado` | Entregado |

---

## Dashboard Administrativo (`dashboard/`)

### Tecnologías

- **React 19** + **Vite 8** (bundler rápido)
- **Chakra UI v2** (diseño Horizon UI — modo oscuro forzado)
- **Recharts** (gráficos de barras, áreas)
- **react-icons/md** (iconos Material Design)

### Vistas

| Ruta | Vista | Descripción |
|---|---|---|
| `/admin/default` | Main Dashboard | KPIs de envíos, gráficos, tabla de envíos recientes |
| `/admin/clientes` | Clientes | Todos los clientes registrados, total/pendientes de envíos, buscador |
| `/admin/pendientes` | Envíos | Pestañas: Pendientes / En Ruta / Entregados, KPIs, tabla detallada |
| `/admin/reportes` | Reportes | Reportes e incidencias con pestañas (Todos / Abiertos / Cerrados) |
| `/admin/observability` | Observabilidad | Latencia p99, throughput, tasa de error, DB pool, servicios, recursos, eventos |

### Datos

Las vistas consumen los endpoints del backend Flask (`/api/envios` y `/api/system-stats`). Si el backend no está corriendo, las tablas se muestran vacías sin errores. Los datos de observabilidad son mock generados en el frontend.

---

## Base de Datos (Supabase)

### Tablas

| Tabla | Propósito |
|---|---|
| `envios` | Registro de envíos con tracking |
| `clientes` | Clientes registrados vía WhatsApp |
| `estado_usuario` | Estado de conversación por teléfono |
| `faq` | Preguntas frecuentes con auto-respuesta |
| `reportes` | Problemas reportados por clientes |

### SQL

El esquema completo está en `bot-mensajeria/supabase_schema.sql`. Incluye:
- Creación de tablas con RLS (Row Level Security)
- Trigger `generar_tracking_code()` para auto-generar códigos `CUR-{id:05d}`
- Políticas de acceso para `service_role`
- Seed data de FAQ

---

## Variables de Entorno

### Backend (`bot-mensajeria/.env`)

```env
WHATSAPP_TOKEN=EAAxxxxxxxxxxxxxxxx
PHONE_NUMBER_ID=123456789012345
WEBHOOK_VERIFY_TOKEN=curriermsj_secret
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=eyJxxxxxxxxxxxxxxxx
URL_GOOGLE_SHEETS=
HOST=0.0.0.0
PORT=5000
DEBUG=true
BUSINESS_NAME=CurrierMsj
BOT_NAME=Rex
ROUTE_LABEL=EE.UU. -> Ecuador
SUPPORT_HOURS=Lunes a Sabado, 8:00 - 18:00
WELCOME_IMAGE_URL=
```

### Dashboard (`dashboard/.env`)

```env
VITE_BOT_HEALTH_URL=http://localhost:5000/health
```

---

## Instalación y Ejecución

### Backend

```bash
cd bot-mensajeria
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
# Crear .env con las variables de Supabase y WhatsApp
python app.py
```

### Dashboard

```bash
cd dashboard
npm install
# Opcional: crear dashboard/.env con VITE_BOT_HEALTH_URL
npm run dev
```

### ngrok (para webhook WhatsApp)

```bash
ngrok http 5000
```

En Meta Developers configurar:
```
Callback URL: https://TU-NGROK.ngrok-free.app/webhook
Verify token: curriermsj_secret
```

---

## Pruebas

### Backend (56 tests)

```bash
cd bot-mensajeria
.venv\Scripts\python -m pytest tests/unit/ -v
```

### Dashboard

```bash
cd dashboard
npm run build     # Build de producción
npm run dev       # Servidor de desarrollo
npm run lint      # Linter (oxlint)
```

---

## Estructura del Proyecto

```
curriermsj/
├── README.md
├── .gitignore
├── registro.txt
│
├── bot-mensajeria/           # Backend Flask + WhatsApp Bot
│   ├── app.py                # Entry point, wiring de dependencias
│   ├── config.py             # Variables de entorno y configuración
│   ├── supabase_schema.sql   # DDL completo de Supabase
│   ├── requirements.txt      # Dependencias Python
│   ├── .env.example          # Template de variables de entorno
│   │
│   ├── bot/
│   │   ├── courier_bot.py    # Máquina de estados del bot (635 líneas)
│   │   └── messages.py       # Plantillas de mensajes WhatsApp
│   │
│   ├── domain/
│   │   ├── constants.py      # Steps, statuses, servicios, precios
│   │   └── models.py         # Data model IncomingMessage
│   │
│   ├── services/
│   │   ├── supabase_repository.py  # CRUD via Supabase REST API
│   │   └── whatsapp_client.py      # Cliente WhatsApp Cloud API
│   │
│   ├── web/
│   │   └── routes.py         # Flask routes + webhook parser
│   │
│   └── tests/unit/           # Tests unitarios (pytest)
│       ├── test_config.py
│       ├── test_constants.py
│       ├── test_models.py
│       └── test_messages.py
│
├── dashboard/                # React SPA (Chakra UI / Vite)
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   │
│   └── src/
│       ├── main.jsx          # Entry point (BrowserRouter + Chakra)
│       ├── App.jsx           # ChakraProvider + Routes
│       ├── routes.jsx        # Definición de rutas
│       │
│       ├── theme/            # Tema Chakra UI (Horizon UI)
│       │   ├── theme.js
│       │   ├── styles.js
│       │   ├── components/
│       │   ├── foundations/
│       │   └── additions/
│       │
│       ├── components/       # Componentes reutilizables
│       │   ├── card/
│       │   ├── sidebar/
│       │   ├── navbar/
│       │   ├── footer/
│       │   ├── icons/
│       │   └── separator/
│       │
│       ├── contexts/
│       │   └── SidebarContext.jsx
│       │
│       ├── layouts/
│       │   └── admin/
│       │       └── index.jsx # Layout admin (Sidebar + Navbar + Content)
│       │
│       ├── views/admin/      # Vistas del dashboard
│       │   ├── default/      # Main dashboard
│       │   ├── clientes/     # Clientes
│       │   ├── pendientes/   # Envíos por estado
│       │   ├── reportes/     # Reportes e incidencias
│       │   └── observability/ # Observabilidad técnica
│       │
│       └── lib/
│           ├── useSupabase.js     # Hooks para datos del backend
│           └── supabaseClient.js  # Cliente Supabase directo
```

---

## Roadmap

| Fase | Objetivo | Estado |
|---|---|---|
| 1 | WhatsApp + Supabase + ngrok para demo | ✅ Completado |
| 2 | Ajustar cotizaciones reales EE.UU. -> Ecuador | ⏳ Pendiente |
| 3 | Panel administrativo para agentes | ✅ Completado |
| 4 | Despliegue estable sin ngrok | ⏳ Pendiente |
| 5 | Integración OpenTelemetry / Sentry | ⏳ Pendiente |
