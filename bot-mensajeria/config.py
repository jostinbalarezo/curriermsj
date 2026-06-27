"""
CurrierMsj - Bot de Mensajería y Envíos
Configuración centralizada del bot.
"""

import os

# Token del bot de Telegram (obtener de @BotFather)
TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN",
    "8666605143:AAGk75K_1t_rp38B-d_5ysAH6Iu8Hu6Fad8",
)

# Configuración de Supabase
SUPABASE_URL = os.getenv(
    "SUPABASE_URL",
    "https://odcgqqbuzpqlgrrsclzg.supabase.co",
)
SUPABASE_KEY = os.getenv(
    "SUPABASE_KEY",
    "sb_publishable_CKcVA-FFAB9lSIt6OQUb6Q_BpkgXeq_",
)
SUPABASE_TABLE = "envios"

# URL del webhook de Google Sheets
URL_GOOGLE_SHEETS = os.getenv(
    "URL_GOOGLE_SHEETS",
    "https://script.google.com/macros/s/AKfycbzMym2lrw_iWKwI2FuxWqW4sPNQvI2k-Z7ukoy5z617rqLpjKJma2oi6bdzMcbdfFMb/exec",
)
