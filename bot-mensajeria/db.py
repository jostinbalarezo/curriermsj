"""
CurrierMsj - Módulo de base de datos con Supabase.
Usa la REST API de Supabase para operaciones CRUD.
"""

import logging
from datetime import datetime
from typing import Optional

import httpx

import config

logger = logging.getLogger(__name__)

HEADERS = {
    "apikey": config.SUPABASE_KEY,
    "Authorization": f"Bearer {config.SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}


async def init_db() -> None:
    """Verifica la conexión a Supabase."""
    url = f"{config.SUPABASE_URL}/rest/v1/{config.SUPABASE_TABLE}?select=id&limit=1"
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, headers=HEADERS, timeout=10)
            resp.raise_for_status()
            logger.info("Conexión a Supabase verificada correctamente.")
        except Exception as e:
            logger.error(f"Error al conectar a Supabase: {e}")
            raise


async def guardar_envio(
    remitente: str,
    telefono_remitente: str,
    destinatario: str,
    telefono_destinatario: str,
    direccion_origen: str,
    direccion_destino: str,
    tipo_paquete: str,
    peso: str,
    dimensiones: str,
    fecha_envio: str,
    hora_envio: str,
    instrucciones: str,
    chat_id: int,
) -> int:
    """Guarda un envío en Supabase y retorna su ID."""
    creado_en = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = {
        "remitente": remitente,
        "telefono_remitente": telefono_remitente,
        "destinatario": destinatario,
        "telefono_destinatario": telefono_destinatario,
        "direccion_origen": direccion_origen,
        "direccion_destino": direccion_destino,
        "tipo_paquete": tipo_paquete,
        "peso": peso,
        "dimensiones": dimensiones,
        "fecha_envio": fecha_envio,
        "hora_envio": hora_envio,
        "instrucciones": instrucciones,
        "chat_id": chat_id,
        "creado_en": creado_en,
    }
    url = f"{config.SUPABASE_URL}/rest/v1/{config.SUPABASE_TABLE}"
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=payload, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        envio_id = data[0]["id"] if isinstance(data, list) else data["id"]
        logger.info(f"Envío guardado en Supabase con ID: {envio_id}")
        return envio_id


async def obtener_envios(limit: int = 50) -> list:
    """Obtiene los últimos N envíos de Supabase."""
    url = f"{config.SUPABASE_URL}/rest/v1/{config.SUPABASE_TABLE}?select=*&order=creado_en.desc&limit={limit}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        return resp.json()


async def obtener_envio(envio_id: int) -> Optional[dict]:
    """Obtiene un envío por ID desde Supabase."""
    url = f"{config.SUPABASE_URL}/rest/v1/{config.SUPABASE_TABLE}?select=*&id=eq.{envio_id}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data[0] if data else None


async def eliminar_envio(envio_id: int) -> bool:
    """Elimina un envío por ID en Supabase. Retorna True si existía."""
    url = f"{config.SUPABASE_URL}/rest/v1/{config.SUPABASE_TABLE}?id=eq.{envio_id}"
    async with httpx.AsyncClient() as client:
        resp = await client.delete(url, headers={**HEADERS, "Prefer": "return=representation"}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return len(data) > 0
