"""
CurrierMsj - Bot de Mensajería y Envíos
Punto de entrada principal del bot.
"""

import asyncio
import logging

from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters

import config
import db
from handlers.envio import (
    cancelar,
    confirmar_envio,
    REMITENTE,
    TELEFONO_REMITENTE,
    DESTINATARIO,
    TELEFONO_DESTINATARIO,
    DIRECCION_ORIGEN,
    DIRECCION_DESTINO,
    TIPO_PAQUETE,
    PESO,
    DIMENSIONES,
    FECHA_ENVIO,
    HORA_ENVIO,
    INSTRUCCIONES,
    CONFIRMAR,
    recibir_remitente,
    recibir_telefono_remitente,
    recibir_destinatario,
    recibir_telefono_destinatario,
    recibir_direccion_origen,
    recibir_direccion_destino,
    recibir_tipo_paquete,
    recibir_peso,
    recibir_dimensiones,
    recibir_fecha_envio,
    recibir_hora_envio,
    recibir_instrucciones,
    start,
)

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def post_init(application: Application) -> None:
    """Inicializa la base de datos al arrancar el bot."""
    await db.init_db()
    logger.info("Base de datos inicializada correctamente.")


def main() -> None:
    """Configura y ejecuta el bot."""
    application = (
        Application.builder()
        .token(config.TOKEN)
        .post_init(post_init)
        .build()
    )

    # Configurar ConversationHandler para el flujo de envío
    conversacion_envio = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            REMITENTE: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_remitente)],
            TELEFONO_REMITENTE: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_telefono_remitente)],
            DESTINATARIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_destinatario)],
            TELEFONO_DESTINATARIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_telefono_destinatario)],
            DIRECCION_ORIGEN: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_direccion_origen)],
            DIRECCION_DESTINO: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_direccion_destino)],
            TIPO_PAQUETE: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_tipo_paquete)],
            PESO: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_peso)],
            DIMENSIONES: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_dimensiones)],
            FECHA_ENVIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_fecha_envio)],
            HORA_ENVIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_hora_envio)],
            INSTRUCCIONES: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_instrucciones)],
            CONFIRMAR: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirmar_envio)],
        },
        fallbacks=[CommandHandler("cancelar", cancelar)],
    )

    application.add_handler(conversacion_envio)

    logger.info("\U0001F916 Bot CurrierMsj iniciado. Presiona Ctrl+C para detener.")
    application.run_polling()


if __name__ == "__main__":
    main()
