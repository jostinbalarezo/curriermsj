import pytest
from bot.messages import MessageTemplates


class TestMessageTemplates:
    def test_menu_has_text(self):
        menu = MessageTemplates.menu()
        assert len(menu) > 50
        assert "CURRIERMSJ" in menu

    def test_menu_includes_bot_name(self):
        menu = MessageTemplates.menu()
        assert "Rex" in menu

    def test_menu_has_options(self):
        menu = MessageTemplates.menu()
        assert "1." in menu or "Rastrear" in menu

    def test_tracking_card_has_basic_info(self):
        envio = {
            "estado": "pendiente",
            "remitente": "Juan",
            "destinatario": "Maria",
        }
        card = MessageTemplates.tracking_card(envio, "CUR-00001")
        assert "CUR-00001" in card
        assert "Maria" in card

    def test_tracking_card_with_all_steps(self):
        envio = {"estado": "en_transito", "remitente": "A", "destinatario": "B"}
        card = MessageTemplates.tracking_card(envio, "CUR-00002")
        assert "CUR-00002" in card
        assert "[...]" in card or "[OK]" in card

    def test_quote_summary_has_info(self):
        data = {
            "origen": "New York",
            "destino": "Quito",
            "tipo_paquete": "Documentos",
            "peso": "< 1 kg",
            "servicio": "Express 24-48h",
            "precio": 35.0,
        }
        summary = MessageTemplates.quote_summary(data)
        assert "New York" in summary
        assert "Quito" in summary
        assert "Documentos" in summary

    def test_shipment_summary_has_all_fields(self):
        data = {
            "remitente": "Juan Perez",
            "telefono_remitente": "0991234567",
            "destinatario": "Maria Lopez",
            "telefono_destinatario": "0997654321",
            "direccion_destino": "Calle 123",
            "tipo_paquete": "Documentos",
            "instrucciones": "Fragil",
        }
        summary = MessageTemplates.shipment_summary(data)
        assert "Juan Perez" in summary
        assert "Maria Lopez" in summary
        assert "Documentos" in summary

    def test_report_created_has_id(self):
        report = MessageTemplates.report_created(1, "retraso", "CUR-00001")
        assert "1" in report
        assert "retraso" in report

    def test_quote_options_returns_string(self):
        data = {"tipo_paquete": "Documentos", "peso": "< 1 kg"}
        result = MessageTemplates.quote_options(data, {})
        assert isinstance(result, str)
