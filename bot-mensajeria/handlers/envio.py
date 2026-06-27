"""
CurrierMsj - Handlers para el flujo de envíos del bot.
Organizados en un ConversationHandler con múltiples estados.
"""

import logging
from datetime import datetime, timedelta

from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ContextTypes, ConversationHandler

import db
from services.google_sheets import enviar_a_google_sheets

logger = logging.getLogger(__name__)

# ─── Estados de la conversación ───
REMITENTE, TELEFONO_REMITENTE, DESTINATARIO, TELEFONO_DESTINATARIO, \
DIRECCION_ORIGEN, DIRECCION_DESTINO, TIPO_PAQUETE, PESO, DIMENSIONES, \
FECHA_ENVIO, HORA_ENVIO, INSTRUCCIONES, CONFIRMAR = range(13)


# ═══════════════════════════════════════════════════════════
# INICIO Y DATOS DEL REMITENTE
# ═══════════════════════════════════════════════════════════

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Inicia la conversación solicitando el nombre del remitente."""
    context.user_data.clear()
    await update.message.reply_text(
        "Hola \U0001F44B Soy el asistente de *CurrierMsj* \U0001F4E6\n"
        "Vamos a registrar tu envío paso a paso.\n\n"
        "Para cancelar en cualquier momento, escribe /cancelar.",
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="Markdown",
    )
    await update.message.reply_text(
        "¿Cuál es tu nombre completo? (Remitente)"
    )
    return REMITENTE


async def recibir_remitente(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Recibe el nombre del remitente y solicita su teléfono."""
    context.user_data["remitente"] = update.message.text
    await update.message.reply_text(
        "¿Cuál es tu número de teléfono? (Remitente)\nEjemplo: 0991234567"
    )
    return TELEFONO_REMITENTE


async def recibir_telefono_remitente(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Recibe el teléfono del remitente y solicita el destinatario."""
    context.user_data["telefono_remitente"] = update.message.text
    await update.message.reply_text(
        "¿Cuál es el nombre completo del destinatario?"
    )
    return DESTINATARIO


# ═══════════════════════════════════════════════════════════
# DATOS DEL DESTINATARIO
# ═══════════════════════════════════════════════════════════

async def recibir_destinatario(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Recibe el nombre del destinatario y solicita su teléfono."""
    context.user_data["destinatario"] = update.message.text
    await update.message.reply_text(
        "¿Cuál es el número de teléfono del destinatario?\nEjemplo: 0991234567"
    )
    return TELEFONO_DESTINATARIO


async def recibir_telefono_destinatario(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Recibe el teléfono del destinatario y solicita dirección de origen."""
    context.user_data["telefono_destinatario"] = update.message.text
    await update.message.reply_text(
        "¿Cuál es la dirección exacta de origen? (De donde se recoge el paquete)\n"
        "Ejemplo: Av. de las Américas y Calle Cuarta, Casa 123"
    )
    return DIRECCION_ORIGEN


# ═══════════════════════════════════════════════════════════
# DIRECCIONES
# ═══════════════════════════════════════════════════════════

async def recibir_direccion_origen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Recibe la dirección de origen y solicita la dirección de destino."""
    context.user_data["direccion_origen"] = update.message.text
    await update.message.reply_text(
        "¿Cuál es la dirección exacta de destino? (A donde se entrega el paquete)\n"
        "Ejemplo: Av. 12 de Octubre y Patria, Edificio Central, Piso 3"
    )
    return DIRECCION_DESTINO


async def recibir_direccion_destino(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Recibe la dirección de destino y solicita tipo de paquete."""
    context.user_data["direccion_destino"] = update.message.text
    teclado = ReplyKeyboardMarkup(
        [
            ["Documentos \U0001F4C4", "Paquete pequeño \U0001F4E6"],
            ["Paquete mediano \U0001F4E6", "Paquete grande \U0001F4E6"],
            ["Sobres / Cartas \U00002709", "Otro"],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await update.message.reply_text(
        "¿Qué tipo de paquete vas a enviar?", reply_markup=teclado
    )
    return TIPO_PAQUETE


# ═══════════════════════════════════════════════════════════
# TIPO DE PAQUETE Y PESO
# ═══════════════════════════════════════════════════════════

async def recibir_tipo_paquete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Recibe el tipo de paquete y solicita el peso."""
    context.user_data["tipo_paquete"] = update.message.text
    teclado = ReplyKeyboardMarkup(
        [
            ["Menos de 1 kg", "1 - 3 kg"],
            ["3 - 5 kg", "5 - 10 kg"],
            ["Más de 10 kg"],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await update.message.reply_text(
        "¿Aproximadamente qué peso tiene el paquete?", reply_markup=teclado
    )
    return PESO


async def recibir_peso(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Recibe el peso y solicita las dimensiones."""
    context.user_data["peso"] = update.message.text
    teclado = ReplyKeyboardMarkup(
        [
            ["Pequeño (20x15x10 cm)", "Mediano (30x20x15 cm)"],
            ["Grande (50x40x30 cm)", "No lo sé / Otro"],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await update.message.reply_text(
        "¿Cuáles son las dimensiones aproximadas del paquete?", reply_markup=teclado
    )
    return DIMENSIONES


async def recibir_dimensiones(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Recibe las dimensiones y solicita la fecha de envío."""
    context.user_data["dimensiones"] = update.message.text
    teclado = ReplyKeyboardMarkup(
        [
            ["Hoy mismo", "Mañana"],
            ["En 2 días", "Escribir otra fecha"],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await update.message.reply_text(
        "¿Cuándo quieres que se realice el envío?", reply_markup=teclado
    )
    return FECHA_ENVIO


# ═══════════════════════════════════════════════════════════
# FECHA Y HORA DE ENVÍO
# ═══════════════════════════════════════════════════════════

async def recibir_fecha_envio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Recibe y procesa la fecha de envío."""
    texto = update.message.text
    hoy = datetime.now()

    if texto == "Hoy mismo":
        context.user_data["fecha_envio"] = hoy.strftime("%d/%m/%Y")
    elif texto == "Mañana":
        context.user_data["fecha_envio"] = (hoy + timedelta(days=1)).strftime("%d/%m/%Y")
    elif texto == "En 2 días":
        context.user_data["fecha_envio"] = (hoy + timedelta(days=2)).strftime("%d/%m/%Y")
    elif texto == "Escribir otra fecha":
        await update.message.reply_text(
            "Por favor, escribe la fecha manualmente (ej: 15/08/2026):"
        )
        return FECHA_ENVIO
    else:
        context.user_data["fecha_envio"] = texto

    teclado = ReplyKeyboardMarkup(
        [["08:00", "10:00", "12:00"], ["14:00", "16:00", "18:00"], ["Escribir otra hora"]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await update.message.reply_text(
        "¿A qué hora prefieres que se realice la recolección?",
        reply_markup=teclado,
    )
    return HORA_ENVIO


async def recibir_hora_envio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Recibe la hora de envío y solicita instrucciones adicionales."""
    texto = update.message.text
    if texto == "Escribir otra hora":
        await update.message.reply_text("Por favor, escribe la hora manualmente (ej: 17:30):")
        return HORA_ENVIO

    context.user_data["hora_envio"] = texto
    teclado = ReplyKeyboardMarkup(
        [
            ["Fragil", "Urgente"],
            ["Contra entrega", "Ninguna"],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await update.message.reply_text(
        "¿Hay alguna instrucción especial? (Selecciona una o escribe)\n"
        "Ejemplo: 'Tocar timbre', 'Llamar antes de llegar', etc.",
        reply_markup=teclado,
    )
    return INSTRUCCIONES


# ═══════════════════════════════════════════════════════════
# INSTRUCCIONES Y CONFIRMACIÓN
# ═══════════════════════════════════════════════════════════

async def recibir_instrucciones(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Recibe las instrucciones y muestra el resumen."""
    context.user_data["instrucciones"] = update.message.text
    return await mostrar_resumen(update, context)


async def mostrar_resumen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Muestra el resumen del envío y solicita confirmación."""
    d = context.user_data
    resumen = (
        "\U0001F4CB *Resumen de tu envío:*\n\n"
        f"\U0001F464 *Remitente:* {d.get('remitente')}\n"
        f"\U0001F4F1 Teléfono remitente: {d.get('telefono_remitente')}\n"
        f"\U0001F464 *Destinatario:* {d.get('destinatario')}\n"
        f"\U0001F4F1 Teléfono destinatario: {d.get('telefono_destinatario')}\n"
        f"\U00002709 Dirección origen: {d.get('direccion_origen')}\n"
        f"\U0001F4CD Dirección destino: {d.get('direccion_destino')}\n"
        f"\U0001F4E6 Tipo de paquete: {d.get('tipo_paquete')}\n"
        f"\U000026A1 Peso: {d.get('peso')}\n"
        f"\U0001F4CF Dimensiones: {d.get('dimensiones')}\n"
        f"\U0001F4C5 Fecha de envío: {d.get('fecha_envio')}\n"
        f"\U000023F0 Hora: {d.get('hora_envio')}\n"
        f"\U0001F4DD Instrucciones: {d.get('instrucciones')}\n\n"
        "¿Confirmas este envío?"
    )
    teclado = ReplyKeyboardMarkup(
        [["SI, confirmar \U00002705", "NO, cancelar \U0000274C"]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await update.message.reply_text(resumen, parse_mode="Markdown", reply_markup=teclado)
    return CONFIRMAR


async def confirmar_envio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Procesa la confirmación o cancelación del envío."""
    respuesta = update.message.text.strip().lower()
    d = context.user_data

    if "si" in respuesta:
        # Guardar en Supabase
        envio_id = await db.guardar_envio(
            remitente=d.get("remitente"),
            telefono_remitente=d.get("telefono_remitente"),
            destinatario=d.get("destinatario"),
            telefono_destinatario=d.get("telefono_destinatario"),
            direccion_origen=d.get("direccion_origen"),
            direccion_destino=d.get("direccion_destino"),
            tipo_paquete=d.get("tipo_paquete"),
            peso=d.get("peso"),
            dimensiones=d.get("dimensiones"),
            fecha_envio=d.get("fecha_envio"),
            hora_envio=d.get("hora_envio"),
            instrucciones=d.get("instrucciones"),
            chat_id=update.effective_chat.id,
        )

        envio = {
            "id": envio_id,
            "remitente": d.get("remitente"),
            "telefono_remitente": d.get("telefono_remitente"),
            "destinatario": d.get("destinatario"),
            "telefono_destinatario": d.get("telefono_destinatario"),
            "direccion_origen": d.get("direccion_origen"),
            "direccion_destino": d.get("direccion_destino"),
            "tipo_paquete": d.get("tipo_paquete"),
            "peso": d.get("peso"),
            "dimensiones": d.get("dimensiones"),
            "fecha_envio": d.get("fecha_envio"),
            "hora_envio": d.get("hora_envio"),
            "instrucciones": d.get("instrucciones"),
            "chat_id": update.effective_chat.id,
        }

        # Enviar a Google Sheets
        enviar_a_google_sheets(envio)

        await update.message.reply_text(
            "\U00002705 ¡Envío confirmado y registrado con éxito!\n"
            "Nuestro equipo de *CurrierMsj* se pondrá en contacto contigo.\n"
            "Gracias por confiar en nosotros \U0001F4E6\U0001F69A",
            reply_markup=ReplyKeyboardRemove(),
            parse_mode="Markdown",
        )

        context.user_data.clear()
        return ConversationHandler.END

    else:
        await update.message.reply_text(
            "\U0000274C Envío cancelado.. Escribe /start para volver a empezar.",
            reply_markup=ReplyKeyboardRemove(),
        )
        context.user_data.clear()
        return ConversationHandler.END


async def cancelar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancela la conversación actual."""
    context.user_data.clear()
    await update.message.reply_text(
        "Proceso cancelado. Escribe /start cuando quieras hacer un nuevo envío.",
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END
