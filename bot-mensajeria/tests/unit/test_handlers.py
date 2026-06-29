"""
Tests unitarios para los handlers del flujo de envio (envio.py)
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import datetime, timedelta
from telegram import Update, Message
from telegram.ext import ContextTypes, ConversationHandler

from handlers.envio import (
    start, recibir_remitente, recibir_telefono_remitente,
    recibir_destinatario, recibir_telefono_destinatario,
    recibir_direccion_origen, recibir_direccion_destino,
    recibir_tipo_paquete, recibir_peso, recibir_dimensiones,
    recibir_fecha_envio, recibir_hora_envio, recibir_instrucciones,
    confirmar_envio, cancelar,
    REMITENTE, TELEFONO_REMITENTE, DESTINATARIO, TELEFONO_DESTINATARIO,
    DIRECCION_ORIGEN, DIRECCION_DESTINO, TIPO_PAQUETE, PESO,
    DIMENSIONES, FECHA_ENVIO, HORA_ENVIO, INSTRUCCIONES, CONFIRMAR
)


@pytest.fixture
def mock_update():
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.message.text = "Texto de prueba"
    update.message.reply_text = AsyncMock()
    update.effective_chat.id = 12345
    return update


@pytest.fixture
def mock_context():
    context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)
    context.user_data = {}
    return context


@pytest.mark.asyncio
async def test_start(mock_update, mock_context):
    result = await start(mock_update, mock_context)
    assert mock_context.user_data == {}
    mock_update.message.reply_text.assert_called()
    assert result == REMITENTE


@pytest.mark.asyncio
async def test_recibir_remitente(mock_update, mock_context):
    mock_update.message.text = "Juan Perez"
    result = await recibir_remitente(mock_update, mock_context)
    assert mock_context.user_data["remitente"] == "Juan Perez"
    assert result == TELEFONO_REMITENTE


@pytest.mark.asyncio
async def test_recibir_telefono_remitente(mock_update, mock_context):
    mock_update.message.text = "0991234567"
    result = await recibir_telefono_remitente(mock_update, mock_context)
    assert mock_context.user_data["telefono_remitente"] == "0991234567"
    assert result == DESTINATARIO


@pytest.mark.asyncio
async def test_recibir_destinatario(mock_update, mock_context):
    mock_update.message.text = "Maria Lopez"
    result = await recibir_destinatario(mock_update, mock_context)
    assert mock_context.user_data["destinatario"] == "Maria Lopez"
    assert result == TELEFONO_DESTINATARIO


@pytest.mark.asyncio
async def test_recibir_telefono_destinatario(mock_update, mock_context):
    mock_update.message.text = "0997654321"
    result = await recibir_telefono_destinatario(mock_update, mock_context)
    assert mock_context.user_data["telefono_destinatario"] == "0997654321"
    assert result == DIRECCION_ORIGEN


@pytest.mark.asyncio
async def test_recibir_direccion_origen(mock_update, mock_context):
    mock_update.message.text = "Calle Falsa 123"
    result = await recibir_direccion_origen(mock_update, mock_context)
    assert mock_context.user_data["direccion_origen"] == "Calle Falsa 123"
    assert result == DIRECCION_DESTINO


@pytest.mark.asyncio
async def test_recibir_direccion_destino(mock_update, mock_context):
    mock_update.message.text = "Calle Real 456"
    result = await recibir_direccion_destino(mock_update, mock_context)
    assert mock_context.user_data["direccion_destino"] == "Calle Real 456"
    assert result == TIPO_PAQUETE


@pytest.mark.asyncio
async def test_recibir_tipo_paquete(mock_update, mock_context):
    mock_update.message.text = "Documentos"
    result = await recibir_tipo_paquete(mock_update, mock_context)
    assert mock_context.user_data["tipo_paquete"] == "Documentos"
    assert result == PESO


@pytest.mark.asyncio
async def test_recibir_peso(mock_update, mock_context):
    mock_update.message.text = "1 - 3 kg"
    result = await recibir_peso(mock_update, mock_context)
    assert mock_context.user_data["peso"] == "1 - 3 kg"
    assert result == DIMENSIONES


@pytest.mark.asyncio
async def test_recibir_dimensiones(mock_update, mock_context):
    mock_update.message.text = "Mediano (30x20x15 cm)"
    result = await recibir_dimensiones(mock_update, mock_context)
    assert mock_context.user_data["dimensiones"] == "Mediano (30x20x15 cm)"
    assert result == FECHA_ENVIO


@pytest.mark.asyncio
async def test_recibir_fecha_envio_hoy(mock_update, mock_context):
    mock_update.message.text = "Hoy mismo"
    result = await recibir_fecha_envio(mock_update, mock_context)
    hoy_str = datetime.now().strftime("%d/%m/%Y")
    assert mock_context.user_data["fecha_envio"] == hoy_str
    assert result == HORA_ENVIO


@pytest.mark.asyncio
async def test_recibir_fecha_envio_manana(mock_update, mock_context):
    mock_update.message.text = "Mañana"
    result = await recibir_fecha_envio(mock_update, mock_context)
    manana_str = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
    assert mock_context.user_data["fecha_envio"] == manana_str
    assert result == HORA_ENVIO


@pytest.mark.asyncio
async def test_recibir_fecha_envio_dos_dias(mock_update, mock_context):
    mock_update.message.text = "En 2 días"
    result = await recibir_fecha_envio(mock_update, mock_context)
    dos_dias_str = (datetime.now() + timedelta(days=2)).strftime("%d/%m/%Y")
    assert mock_context.user_data["fecha_envio"] == dos_dias_str
    assert result == HORA_ENVIO


@pytest.mark.asyncio
async def test_recibir_fecha_envio_escribir_otra(mock_update, mock_context):
    mock_update.message.text = "Escribir otra fecha"
    result = await recibir_fecha_envio(mock_update, mock_context)
    assert "fecha_envio" not in mock_context.user_data
    assert result == FECHA_ENVIO


@pytest.mark.asyncio
async def test_recibir_fecha_envio_manual(mock_update, mock_context):
    mock_update.message.text = "25/12/2026"
    result = await recibir_fecha_envio(mock_update, mock_context)
    assert mock_context.user_data["fecha_envio"] == "25/12/2026"
    assert result == HORA_ENVIO


@pytest.mark.asyncio
async def test_recibir_hora_envio_escribir_otra(mock_update, mock_context):
    mock_update.message.text = "Escribir otra hora"
    result = await recibir_hora_envio(mock_update, mock_context)
    assert "hora_envio" not in mock_context.user_data
    assert result == HORA_ENVIO


@pytest.mark.asyncio
async def test_recibir_hora_envio_manual(mock_update, mock_context):
    mock_update.message.text = "15:30"
    result = await recibir_hora_envio(mock_update, mock_context)
    assert mock_context.user_data["hora_envio"] == "15:30"
    assert result == INSTRUCCIONES


@pytest.mark.asyncio
async def test_recibir_instrucciones(mock_update, mock_context):
    mock_update.message.text = "Llamar antes de llegar"
    mock_context.user_data = {
        "remitente": "Juan Perez",
        "telefono_remitente": "0991234567",
        "destinatario": "Maria Lopez",
        "telefono_destinatario": "0997654321",
        "direccion_origen": "Av. Principal 123",
        "direccion_destino": "Calle Secundaria 456",
        "tipo_paquete": "Paquete pequeño",
        "peso": "1 - 3 kg",
        "dimensiones": "Pequeño (20x15x10 cm)",
        "fecha_envio": "27/06/2026",
        "hora_envio": "14:00",
    }
    result = await recibir_instrucciones(mock_update, mock_context)
    assert mock_context.user_data["instrucciones"] == "Llamar antes de llegar"
    assert result == CONFIRMAR
    mock_update.message.reply_text.assert_called_once()


@pytest.mark.asyncio
async def test_confirmar_envio_si(mock_update, mock_context):
    mock_update.message.text = "SI, confirmar ✅"
    mock_context.user_data = {
        "remitente": "Juan Perez",
        "telefono_remitente": "0991234567",
        "destinatario": "Maria Lopez",
        "telefono_destinatario": "0997654321",
        "direccion_origen": "Av. Principal 123",
        "direccion_destino": "Calle Secundaria 456",
        "tipo_paquete": "Paquete pequeño",
        "peso": "1 - 3 kg",
        "dimensiones": "Pequeño (20x15x10 cm)",
        "fecha_envio": "27/06/2026",
        "hora_envio": "14:00",
        "instrucciones": "Llamar antes de llegar",
    }

    with patch("handlers.envio.db.guardar_envio", new_callable=AsyncMock) as mock_guardar_envio, \
         patch("handlers.envio.enviar_a_google_sheets") as mock_enviar_sheets:
        
        mock_guardar_envio.return_value = 123
        mock_enviar_sheets.return_value = True
        
        result = await confirmar_envio(mock_update, mock_context)
        
        mock_guardar_envio.assert_called_once()
        mock_enviar_sheets.assert_called_once()
        assert result == ConversationHandler.END
        assert mock_context.user_data == {}  # Debería estar vacío (limpiado)


@pytest.mark.asyncio
async def test_confirmar_envio_no(mock_update, mock_context):
    mock_update.message.text = "NO, cancelar ❌"
    mock_context.user_data = {
        "remitente": "Juan Perez",
    }

    result = await confirmar_envio(mock_update, mock_context)
    assert result == ConversationHandler.END
    assert mock_context.user_data == {}


@pytest.mark.asyncio
async def test_cancelar(mock_update, mock_context):
    mock_context.user_data = {
        "remitente": "Juan Perez",
    }
    result = await cancelar(mock_update, mock_context)
    assert result == ConversationHandler.END
    assert mock_context.user_data == {}
