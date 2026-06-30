import os
import pytest


@pytest.fixture
def mock_env(monkeypatch):
    env_vars = [
        "WHATSAPP_TOKEN", "PHONE_NUMBER_ID", "WEBHOOK_VERIFY_TOKEN",
        "SUPABASE_URL", "SUPABASE_KEY", "URL_GOOGLE_SHEETS",
    ]
    for var in env_vars:
        monkeypatch.delenv(var, raising=False)


def test_config_default_values(mock_env):
    import importlib
    import config
    importlib.reload(config)

    assert config.HOST == "0.0.0.0"
    assert config.PORT == 5000
    assert config.DEBUG is True
    assert config.BUSINESS_NAME == "CurrierMsj"
    assert config.BOT_NAME == "Rex"
    assert config.ROUTE_LABEL == "EE.UU. -> Ecuador"
    assert config.WEBHOOK_VERIFY_TOKEN == "curriermsj_secret"
    assert config.SUPABASE_TABLE_ENVIOS == "envios"
    assert config.SUPABASE_TABLE_ESTADO == "estado_usuario"
    assert config.SUPABASE_TABLE_CLIENTES == "clientes"
    assert config.SUPABASE_TABLE_FAQ == "faq"
    assert config.SUPABASE_TABLE_REPORTES == "reportes"
    assert config.WHATSAPP_API_URL == "https://graph.facebook.com/v20.0"


def test_config_env_variables(monkeypatch):
    import importlib

    monkeypatch.setenv("WHATSAPP_TOKEN", "wa_token_test")
    monkeypatch.setenv("PHONE_NUMBER_ID", "123456789")
    monkeypatch.setenv("WEBHOOK_VERIFY_TOKEN", "custom_token")
    monkeypatch.setenv("SUPABASE_URL", "https://test.supabase.co")
    monkeypatch.setenv("SUPABASE_KEY", "test_key_456")
    monkeypatch.setenv("HOST", "127.0.0.1")
    monkeypatch.setenv("PORT", "8000")
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("BUSINESS_NAME", "TestCorp")

    import config
    importlib.reload(config)

    assert config.WHATSAPP_TOKEN == "wa_token_test"
    assert config.PHONE_NUMBER_ID == "123456789"
    assert config.WEBHOOK_VERIFY_TOKEN == "custom_token"
    assert config.SUPABASE_URL == "https://test.supabase.co"
    assert config.SUPABASE_KEY == "test_key_456"
    assert config.HOST == "127.0.0.1"
    assert config.PORT == 8000
    assert config.DEBUG is False
    assert config.BUSINESS_NAME == "TestCorp"
