"""
Tests unitarios para el módulo config.py
"""

import os
import pytest

# Simulación de variables de entorno para pruebas
@pytest.fixture
def mock_env(monkeypatch):
    """Fixture para limpiar variables de entorno antes de cada test."""
    # Eliminar variables existentes
    env_vars = [
        "TELEGRAM_BOT_TOKEN", "SUPABASE_URL", "SUPABASE_KEY",
        "URL_GOOGLE_SHEETS"
    ]
    for var in env_vars:
        monkeypatch.delenv(var, raising=False)


def test_config_default_values(mock_env):
    """Verifica que las variables de configuración por defecto estén definidas."""
    import importlib
    import config
    importlib.reload(config)
    
    assert config.TOKEN is not None
    assert config.SUPABASE_URL is not None
    assert config.SUPABASE_KEY is not None
    assert config.SUPABASE_TABLE == "envios"
    assert config.URL_GOOGLE_SHEETS is not None


def test_config_env_variables(monkeypatch):
    """Verifica que se carguen variables de entorno correctamente."""
    import importlib
    
    # Establecer variables de entorno de prueba
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "test_token_123")
    monkeypatch.setenv("SUPABASE_URL", "https://test.supabase.co")
    monkeypatch.setenv("SUPABASE_KEY", "test_key_456")
    monkeypatch.setenv("URL_GOOGLE_SHEETS", "https://test.sheets.com")
    
    # Recargar módulo para que lea las nuevas variables
    import config
    importlib.reload(config)
    
    assert config.TOKEN == "test_token_123"
    assert config.SUPABASE_URL == "https://test.supabase.co"
    assert config.SUPABASE_KEY == "test_key_456"
    assert config.URL_GOOGLE_SHEETS == "https://test.sheets.com"
