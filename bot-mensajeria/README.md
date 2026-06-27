# Bot mensajeria - CurrierMsj

Backend Flask para el bot de WhatsApp de CurrierMsj. La ruta comercial documentada es EE.UU. -> Ecuador.

La documentacion completa esta en el README principal del repositorio:

```text
../README.md
```

## Archivos principales

| Archivo | Funcion |
|---|---|
| `app.py` | Punto de entrada: arma dependencias y crea Flask |
| `config.py` | Carga variables de entorno y nombres de tablas |
| `bot/courier_bot.py` | Orquesta estados, cotizacion, rastreo, reportes y registro |
| `bot/messages.py` | Textos tipo tarjeta y botones de WhatsApp |
| `domain/constants.py` | Estados, tarifas, servicios y aliases |
| `domain/models.py` | Modelo `IncomingMessage` |
| `services/supabase_repository.py` | Repositorio REST para Supabase |
| `services/whatsapp_client.py` | Cliente WhatsApp Cloud API |
| `web/routes.py` | Rutas Flask y parser del webhook |
| `whatsapp_db.py` | Fachada legacy para imports antiguos |
| `supabase_schema.sql` | SQL para crear tablas, politicas y FAQ inicial |
| `requirements.txt` | Dependencias Python |

## Ejecutar localmente

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

En otra terminal:

```bash
ngrok http 5000
```

Webhook para Meta Developers:

```text
https://TU-NGROK.ngrok-free.app/webhook
```

## Variables requeridas

Crea `bot-mensajeria/.env`:

```env
WHATSAPP_TOKEN=EAAxxxxxxxxxxxxxxxxxxxxxxxx
PHONE_NUMBER_ID=123456789012345
WEBHOOK_VERIFY_TOKEN=curriermsj_secret
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=eyJxxxxxxxxxxxxxxxxxxxxxxxx
BUSINESS_NAME=CurrierMsj
BOT_NAME=Rex
ROUTE_LABEL=EE.UU. -> Ecuador
PORT=5000

# Legacy temporal, solo si restauras codigo Telegram antiguo.
TELEGRAM_BOT_TOKEN=123456:ABCxxxxxxxxxxxxxxxx
```

Telegram no es el flujo activo del codigo actual. Queda solo como referencia legacy para eliminarlo cuando WhatsApp este estable.
