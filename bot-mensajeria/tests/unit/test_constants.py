import pytest
from domain.constants import (
    Step, PACKAGE_TYPES, WEIGHTS, SHIPPING_SERVICES, STATUS_STEPS,
    WEIGHT_ALIASES, PACKAGE_TYPE_ALIASES, WELCOME_ACTIONS, MENU_ACTIONS,
    REPORT_CATEGORIES, INSTRUCTIONS, normalize_action, resolve_package_type,
    resolve_weight,
)


class TestStep:
    def test_menu_enum(self):
        assert Step.MENU == "menu"

    def test_welcome(self):
        assert Step.WELCOME == "bienvenida"

    def test_registration_steps(self):
        assert Step.WELCOME_REGISTER == "bienvenida_registro"
        assert Step.WELCOME_PHONE == "bienvenida_telefono"

    def test_tracking_step(self):
        assert Step.TRACKING_CODE == "rastrear_codigo"

    def test_quote_steps(self):
        assert Step.QUOTE_ORIGIN == "cotizar_origen"
        assert Step.QUOTE_DESTINATION == "cotizar_destino"
        assert Step.QUOTE_PACKAGE_TYPE == "cotizar_tipo"
        assert Step.QUOTE_WEIGHT == "cotizar_peso"
        assert Step.QUOTE_SERVICE == "cotizar_servicio"
        assert Step.QUOTE_SUMMARY == "cotizar_resumen"

    def test_report_steps(self):
        assert Step.REPORT_TYPE == "reportar_tipo"
        assert Step.REPORT_DESCRIPTION == "reportar_descripcion"

    def test_new_shipment_steps(self):
        assert Step.NEW_SHIPMENT_NAME == "nuevo_envio_nombre"
        assert Step.NEW_SHIPMENT_PHONE == "nuevo_envio_telefono"
        assert Step.NEW_SHIPMENT_RECIPIENT == "nuevo_envio_destinatario"
        assert Step.NEW_SHIPMENT_RECIPIENT_PHONE == "nuevo_envio_telefono_dest"
        assert Step.NEW_SHIPMENT_DESTINATION == "nuevo_envio_dir_destino"
        assert Step.NEW_SHIPMENT_PACKAGE_TYPE == "nuevo_envio_tipo"
        assert Step.NEW_SHIPMENT_INSTRUCTIONS == "nuevo_envio_instrucciones"
        assert Step.NEW_SHIPMENT_CONFIRM == "nuevo_envio_confirmar"


class TestPackageTypes:
    def test_has_four_types(self):
        assert len(PACKAGE_TYPES) == 4

    def test_has_documentos(self):
        assert PACKAGE_TYPES["tipo_documento"] == "Documentos"

    def test_has_all_types(self):
        assert "Pequeño" in str(PACKAGE_TYPES.values()) or "pequeno" in str(PACKAGE_TYPES.values())


class TestWeights:
    def test_has_three_weights(self):
        assert len(WEIGHTS) == 3

    def test_has_under_1kg(self):
        assert "1 kg" in WEIGHTS["peso_ligero"]

    def test_weights_have_aliases(self):
        assert len(WEIGHT_ALIASES) >= 3
        assert WEIGHT_ALIASES["1"] == "peso_ligero"


class TestShippingServices:
    def test_has_three_services(self):
        assert len(SHIPPING_SERVICES) == 3

    def test_has_express(self):
        assert "Express" in SHIPPING_SERVICES["servicio_express"]["label"]

    def test_has_estandar(self):
        assert "Estandar" in SHIPPING_SERVICES["servicio_estandar"]["label"]

    def test_has_economico(self):
        assert "Economico" in SHIPPING_SERVICES["servicio_economico"]["label"]

    def test_express_eta(self):
        assert "24" in SHIPPING_SERVICES["servicio_express"]["eta"]


class TestStatusSteps:
    def test_has_five_steps(self):
        assert len(STATUS_STEPS) == 5

    def test_first_step_is_pendiente(self):
        assert STATUS_STEPS[0] == ("pendiente", "Solicitud registrada")

    def test_last_step_is_entregado(self):
        assert STATUS_STEPS[-1] == ("entregado", "Entregado")


class TestNormalizeAction:
    def test_normalize_welcome_action(self):
        assert normalize_action("quiero informacion") == "quiero_info"

    def test_normalize_menu_action(self):
        assert normalize_action("1") == "rastrear"
        assert normalize_action("cotizar") == "cotizar"

    def test_normalize_unknown_returns_same(self):
        assert normalize_action("algo_inesperado") == "algo_inesperado"

    def test_normalize_empty(self):
        assert normalize_action("") == ""


class TestResolvePackageType:
    def test_resolve_by_number(self):
        result = resolve_package_type("1")
        assert result == "Documentos"

    def test_resolve_by_alias(self):
        result = resolve_package_type("documentos")
        assert result == "Documentos"

    def test_resolve_unknown_returns_original(self):
        assert resolve_package_type("Algo Raro") == "Algo Raro"


class TestResolveWeight:
    def test_resolve_by_number(self):
        assert resolve_weight("1") == "Menos de 1 kg"

    def test_resolve_by_alias(self):
        assert resolve_weight("1 - 5 kg") == "1 - 5 kg"

    def test_resolve_unknown_returns_original(self):
        assert resolve_weight("Pesadisimo") == "Pesadisimo"


class TestWelcomeActions:
    def test_has_info(self):
        assert WELCOME_ACTIONS["quiero_informacion"] == "quiero_info"

    def test_has_start_order(self):
        assert WELCOME_ACTIONS["iniciar_pedido"] == "iniciar_pedido"


class TestMenuActions:
    def test_has_tracking(self):
        assert MENU_ACTIONS["1"] == "rastrear"

    def test_has_quote(self):
        assert MENU_ACTIONS["2"] == "cotizar"

    def test_has_agent(self):
        assert MENU_ACTIONS["5"] == "agente"

    def test_has_return(self):
        assert MENU_ACTIONS["volver"] == "volver_menu"


class TestReportCategories:
    def test_has_damaged(self):
        assert "danado" in REPORT_CATEGORIES["rep_danado"]


class TestInstructions:
    def test_has_fragile(self):
        assert INSTRUCTIONS["inst_fragil"] == "Fragil"
