# CurrierMsj Dashboard

Panel administrativo para el bot courier CurrierMsj. Construido con **React 19 + Chakra UI (Horizon UI) + Vite + Recharts**.

## Vistas

| Ruta | Vista | Descripción |
|---|---|---|
| `/admin/default` | Main Dashboard | KPIs de envíos, gráficos por día y tipo, tabla de envíos recientes |
| `/admin/clientes` | Clientes | Todos los clientes con contador de envíos (total/pendientes), buscador |
| `/admin/pendientes` | Envíos | Pestañas: Pendientes / En Ruta / Entregados con KPIs y tabla |
| `/admin/reportes` | Reportes | Reportes e incidencias con pestañas Todos / Abiertos / Cerrados |
| `/admin/observability` | Observabilidad | Latencia p99, throughput, errores, DB pool, servicios, CPU |

## Requisitos

- Node.js 20+
- npm

## Instalar y ejecutar

```bash
cd dashboard
npm install
npm run dev      # Servidor de desarrollo en http://localhost:5173
npm run build    # Build de producción
npm run lint     # Linter (oxlint)
```

## Variables de entorno

Copia `.env.example` como `.env` (opcional, para datos reales):

```env
VITE_BOT_HEALTH_URL=http://localhost:5000/health
```

Sin backend, las tablas se muestran vacías sin errores.

## Stack

- **React 19** + **Vite 8**
- **Chakra UI v2** (tema Horizon UI, modo oscuro forzado)
- **Recharts** (gráficos)
- **react-icons/md** (iconos Material Design)
- **react-router-dom v7** (ruteo)

## Notas

- No se expone el token de WhatsApp en el frontend
- Los datos se obtienen del backend Flask (`/api/envios`, `/api/system-stats`)
- El modo oscuro es permanente (sin toggle a modo claro)
