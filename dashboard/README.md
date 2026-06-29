# CurrierMsj Dashboard

Panel local para revisar el estado del bot courier.

## Abrir

```bash
cd dashboard
npm install
npm start
```

El navegador se abre en:

```text
http://localhost:5173/
```

Si no se abre solo, copia esa URL manualmente en Chrome o Edge.

## Variables opcionales

Copia `.env.example` como `.env` si quieres conectar servicios reales:

```env
VITE_BOT_HEALTH_URL=http://localhost:5000/health
VITE_SUPABASE_URL=
VITE_SUPABASE_ANON_KEY=
```

No pongas el token de WhatsApp en React. Ese token debe vivir solo en el backend Flask.

## Estado de WhatsApp API

El dashboard no llama a Meta Graph API desde el navegador porque eso expondria el token. Si WhatsApp falla, se revisa desde:

- Logs de Flask.
- Variables `WHATSAPP_TOKEN` y `PHONE_NUMBER_ID`.
- Endpoint seguro del backend si se agrega despues.
