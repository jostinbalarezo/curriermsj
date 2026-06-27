"""
CurrierMsj - Servicio para enviar datos de envíos a Google Sheets.
"""

import logging
from typing import Dict, Any

import requests

import config

logger = logging.getLogger(__name__)


def enviar_a_google_sheets(envio: Dict[str, Any]) -> bool:
    """
    Envía los datos de un envío al endpoint de Google Sheets.
    Retorna True si fue exitoso, False en caso contrario.
    """
    try:
        logger.info("Enviando datos a Google Sheets...")
        response = requests.post(
            config.URL_GOOGLE_SHEETS,
            json=envio,
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        logger.info(f"Respuesta Google Sheets: {response.status_code} - {response.text}")
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Error al enviar datos a Google Sheets: {e}")
        return False
