# CurrierMsj - Bot de Mensajería y Envíos

Bot de Telegram para gestionar envíos y mensajería. Permite a los usuarios registrar sus envíos de forma fácil y rápida.

## Características

- Registro de envíos paso a paso
- Captura de datos del remitente y destinatario
- Registro de direcciones de origen y destino
- Información sobre tipo de paquete, peso y dimensiones
- Programación de fecha y hora de envío
- Confirmación con resumen antes de enviar
- Integración con Supabase para almacenamiento
- Integración con Google Sheets para seguimiento

## Instalación

1. Clona el repositorio y navega a la carpeta del proyecto:
```bash
cd bot-mensajeria
```

2. Crea un entorno virtual e instala las dependencias:
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Configura las variables de entorno en el archivo `config.py` o usa variables de entorno:
```bash
export TELEGRAM_BOT_TOKEN="tu_token_de_bot"
export SUPABASE_URL="https://tu-proyecto.supabase.co"
export SUPABASE_KEY="tu_clave_supabase"
```

## Uso

Inicia el bot con:
```bash
python bot.py
```

Escríbele al bot en Telegram con `/start` para comenzar a registrar un envío.

## Estructura del Proyecto

```
bot-mensajeria/
├── bot.py                 # Punto de entrada del bot
├── config.py              # Configuración centralizada
├── db.py                  # Módulo de base de datos (Supabase)
├── requirements.txt       # Dependencias del proyecto
├── handlers/
│   └── envio.py           # Handlers del flujo de envío
└── services/
    └── google_sheets.py   # Servicio de Google Sheets
```

## Contacto

Para soporte o consultas, contacta al equipo de CurrierMsj.
