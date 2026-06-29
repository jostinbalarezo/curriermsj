"""
Tests unitarios para el módulo db.py
"""

import pytest
import asyncio
from unittest.mock import AsyncMock, patch, MagicMock
from datetime import datetime


@pytest.fixture(autouse=True)
def mock_config(monkeypatch):
    """Fixture para mockear el módulo config."""
    mock_config_mod = MagicMock()
    mock_config_mod.SUPABASE_URL = "https://test.supabase.co"
    mock_config_mod.SUPABASE_KEY = "test_key"
    mock_config_mod.SUPABASE_TABLE = "envios"
    
    monkeypatch.setattr("db.config", mock_config_mod)
    return mock_config_mod


@pytest.fixture
def sample_envio_data():
    """Fixture con datos de ejemplo para envíos."""
    return {
        "remitente": "Juan Pérez",
        "telefono_remitente": "0991234567",
        "destinatario": "María López",
        "telefono_destinatario": "0997654321",
        "direccion_origen": "Av. Principal 123",
        "direccion_destino": "Calle Secundaria 456",
        "tipo_paquete": "Paquete pequeño",
        "peso": "1 - 3 kg",
        "dimensiones": "Pequeño (20x15x10 cm)",
        "fecha_envio": "27/06/2026",
        "hora_envio": "14:00",
        "instrucciones": "Fragil",
    }


@pytest.mark.asyncio
async def test_init_db_success(mock_config):
    """Test de inicialización exitosa de la base de datos."""
    import db
    
    # Crear mock de respuesta exitosa
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    
    # Mockear el cliente HTTP
    with patch("httpx.AsyncClient") as mock_client_class:
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.get = AsyncMock(return_value=mock_response)
        
        # Ejecutar función
        await db.init_db()
        
        # Verificar que se hizo la petición correcta
        mock_client.get.assert_called_once()
        expected_url = f"{mock_config.SUPABASE_URL}/rest/v1/{mock_config.SUPABASE_TABLE}?select=id&limit=1"
        assert mock_client.get.call_args[0][0] == expected_url
        
        mock_response.raise_for_status.assert_called_once()


@pytest.mark.asyncio
async def test_guardar_envio(mock_config, sample_envio_data):
    """Test de guardado exitoso de un envío."""
    import db
    
    # Crear mock de respuesta exitosa
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": 123}]
    mock_response.raise_for_status = MagicMock()
    
    with patch("httpx.AsyncClient") as mock_client_class:
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.post = AsyncMock(return_value=mock_response)
        
        # Ejecutar función
        data = sample_envio_data
        result = await db.guardar_envio(
            remitente=data["remitente"],
            telefono_remitente=data["telefono_remitente"],
            destinatario=data["destinatario"],
            telefono_destinatario=data["telefono_destinatario"],
            direccion_origen=data["direccion_origen"],
            direccion_destino=data["direccion_destino"],
            tipo_paquete=data["tipo_paquete"],
            peso=data["peso"],
            dimensiones=data["dimensiones"],
            fecha_envio=data["fecha_envio"],
            hora_envio=data["hora_envio"],
            instrucciones=data["instrucciones"],
            chat_id=12345,
        )
        
        # Verificar resultado
        assert result == 123
        mock_client.post.assert_called_once()
        
        # Verificar que se enviaron los datos correctos
        call_kwargs = mock_client.post.call_args[1]
        assert call_kwargs["json"]["remitente"] == data["remitente"]
        assert call_kwargs["json"]["chat_id"] == 12345


@pytest.mark.asyncio
async def test_obtener_envios(mock_config):
    """Test de obtención de envíos."""
    import db
    
    # Crear mock de respuesta
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {"id": 1, "remitente": "Juan"},
        {"id": 2, "remitente": "María"},
    ]
    mock_response.raise_for_status = MagicMock()
    
    with patch("httpx.AsyncClient") as mock_client_class:
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.get = AsyncMock(return_value=mock_response)
        
        # Ejecutar función
        result = await db.obtener_envios(limit=10)
        
        # Verificar resultado
        assert len(result) == 2
        assert result[0]["remitente"] == "Juan"
        assert result[1]["remitente"] == "María"
        mock_client.get.assert_called_once()


@pytest.mark.asyncio
async def test_obtener_envio(mock_config):
    """Test de obtención de un envío específico."""
    import db
    
    # Crear mock de respuesta
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": 1, "remitente": "Juan"}]
    mock_response.raise_for_status = MagicMock()
    
    with patch("httpx.AsyncClient") as mock_client_class:
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.get = AsyncMock(return_value=mock_response)
        
        # Ejecutar función
        result = await db.obtener_envio(1)
        
        # Verificar resultado
        assert result["id"] == 1
        assert result["remitente"] == "Juan"
        mock_client.get.assert_called_once()


@pytest.mark.asyncio
async def test_obtener_envio_no_existente(mock_config):
    """Test de obtención de un envío que no existe."""
    import db
    
    # Crear mock de respuesta vacía
    mock_response = MagicMock()
    mock_response.json.return_value = []
    mock_response.raise_for_status = MagicMock()
    
    with patch("httpx.AsyncClient") as mock_client_class:
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.get = AsyncMock(return_value=mock_response)
        
        # Ejecutar función
        result = await db.obtener_envio(999)
        
        # Verificar resultado
        assert result is None


@pytest.mark.asyncio
async def test_eliminar_envio(mock_config):
    """Test de eliminación de un envío."""
    import db
    
    # Crear mock de respuesta
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": 1}]
    mock_response.raise_for_status = MagicMock()
    
    with patch("httpx.AsyncClient") as mock_client_class:
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.delete = AsyncMock(return_value=mock_response)
        
        # Ejecutar función
        result = await db.eliminar_envio(1)
        
        # Verificar resultado
        assert result is True
        mock_client.delete.assert_called_once()
