class Step:
    MENU = "menu"
    TRACKING_CODE = "rastrear_codigo"
    QUOTE_ORIGIN = "cotizar_origen"
    QUOTE_DESTINATION = "cotizar_destino"
    QUOTE_PACKAGE_TYPE = "cotizar_tipo"
    QUOTE_WEIGHT = "cotizar_peso"
    QUOTE_SERVICE = "cotizar_servicio"
    QUOTE_SUMMARY = "cotizar_resumen"
    REPORT_TYPE = "reportar_tipo"
    REPORT_DESCRIPTION = "reportar_descripcion"
    NEW_SHIPMENT_NAME = "nuevo_envio_nombre"
    NEW_SHIPMENT_PHONE = "nuevo_envio_telefono"
    NEW_SHIPMENT_RECIPIENT = "nuevo_envio_destinatario"
    NEW_SHIPMENT_RECIPIENT_PHONE = "nuevo_envio_telefono_dest"
    NEW_SHIPMENT_DESTINATION = "nuevo_envio_dir_destino"
    NEW_SHIPMENT_PACKAGE_TYPE = "nuevo_envio_tipo"
    NEW_SHIPMENT_INSTRUCTIONS = "nuevo_envio_instrucciones"
    NEW_SHIPMENT_CONFIRM = "nuevo_envio_confirmar"


MENU_ACTIONS = {
    "1": "rastrear",
    "2": "cotizar",
    "3": "mis_envios",
    "4": "reportar",
    "5": "agente",
    "menu": "volver_menu",
    "menú": "volver_menu",
    "volver": "volver_menu",
    "volver_menu": "volver_menu",
    "rastrear": "rastrear",
    "cotizar": "cotizar",
    "mis_envios": "mis_envios",
    "reportar": "reportar",
    "agente": "agente",
    "ver_ubicacion": "ver_ubicacion",
    "reagendar": "reagendar",
}

PACKAGE_TYPES = {
    "tipo_documento": "Documentos",
    "tipo_pequeno": "Paquete pequeño",
    "tipo_mediano": "Paquete mediano",
    "tipo_grande": "Paquete grande",
}

PACKAGE_TYPE_ALIASES = {
    "1": "tipo_documento",
    "2": "tipo_pequeno",
    "3": "tipo_mediano",
    "4": "tipo_grande",
    "documentos": "tipo_documento",
    "paquete pequeño": "tipo_pequeno",
    "paquete pequeno": "tipo_pequeno",
    "paquete mediano": "tipo_mediano",
    "paquete grande": "tipo_grande",
}

WEIGHTS = {
    "peso_ligero": "Menos de 1 kg",
    "peso_medio": "1 - 5 kg",
    "peso_pesado": "Más de 5 kg",
}

WEIGHT_ALIASES = {
    "1": "peso_ligero",
    "2": "peso_medio",
    "3": "peso_pesado",
    "menos de 1 kg": "peso_ligero",
    "1 - 5 kg": "peso_medio",
    "mas de 5 kg": "peso_pesado",
    "más de 5 kg": "peso_pesado",
}

INSTRUCTIONS = {
    "inst_fragil": "Frágil",
    "inst_urgente": "Urgente",
    "inst_ninguna": "Ninguna",
}

REPORT_CATEGORIES = {
    "rep_danado": "Paquete dañado",
    "rep_no_llego": "No llegó en fecha",
    "rep_incompleto": "Contenido incompleto",
}

BASE_QUOTES_USD = {
    ("Documentos", "Menos de 1 kg"): 3.50,
    ("Documentos", "1 - 5 kg"): 5.00,
    ("Documentos", "Más de 5 kg"): 8.00,
    ("Paquete pequeño", "Menos de 1 kg"): 5.00,
    ("Paquete pequeño", "1 - 5 kg"): 7.50,
    ("Paquete pequeño", "Más de 5 kg"): 12.00,
    ("Paquete mediano", "Menos de 1 kg"): 7.00,
    ("Paquete mediano", "1 - 5 kg"): 10.00,
    ("Paquete mediano", "Más de 5 kg"): 15.00,
    ("Paquete grande", "Menos de 1 kg"): 10.00,
    ("Paquete grande", "1 - 5 kg"): 15.00,
    ("Paquete grande", "Más de 5 kg"): 22.00,
}

SHIPPING_SERVICES = {
    "servicio_express": {
        "label": "Express 24-48h",
        "multiplier": 2.00,
        "eta": "24 a 48 horas",
        "icon": "⚡",
    },
    "servicio_estandar": {
        "label": "Estándar 3-5 días",
        "multiplier": 1.45,
        "eta": "3 a 5 días",
        "icon": "🚀",
    },
    "servicio_economico": {
        "label": "Económico 5-8 días",
        "multiplier": 1.00,
        "eta": "5 a 8 días",
        "icon": "💼",
    },
}

STATUS_STEPS = [
    ("pendiente", "Solicitud registrada"),
    ("recibido", "Paquete recibido"),
    ("en_transito", "En camino al hub"),
    ("en_ruta", "En ruta de entrega"),
    ("entregado", "Entregado"),
]


def normalize_action(text: str) -> str:
    value = (text or "").strip().lower()
    return MENU_ACTIONS.get(value, value)


def resolve_package_type(text: str) -> str:
    value = (text or "").strip().lower()
    key = PACKAGE_TYPE_ALIASES.get(value, value)
    return PACKAGE_TYPES.get(key, text.strip())


def resolve_weight(text: str) -> str:
    value = (text or "").strip().lower()
    key = WEIGHT_ALIASES.get(value, value)
    return WEIGHTS.get(key, text.strip())
