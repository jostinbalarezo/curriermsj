"""
Script de conexion y verificacion con Supabase
"""

import asyncio
import logging
from datetime import datetime

import config
import db

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def verificar_conexion():
    """Verifica la conexion a Supabase."""
    try:
        logger.info("Verificando conexion a Supabase...")
        await db.init_db()
        logger.info("✅ Conexion a Supabase exitosa!")
        return True
    except Exception as e:
        logger.error(f"❌ Error de conexion: {e}")
        return False


async def probar_crud():
    """Prueba operaciones CRUD basicas."""
    logger.info("Probando operaciones CRUD...")
    
    try:
        # Crear un envio de prueba
        envio_id = await db.guardar_envio(
            remitente="Usuario Prueba",
            telefono_remitente="0999999999",
            destinatario="Destinatario Prueba",
            telefono_destinatario="0998888888",
            direccion_origen="Av. Prueba 123",
            direccion_destino="Calle Prueba 456",
            tipo_paquete="Paquete pequeno",
            peso="1 - 3 kg",
            dimensiones="Pequeno (20x15x10 cm)",
            fecha_envio=datetime.now().strftime("%d/%m/%Y"),
            hora_envio="14:00",
            instrucciones="Envio de prueba",
            chat_id=99999,
        )
        logger.info(f"✅ Envio creado con ID: {envio_id}")
        
        # Obtener envio
        envio = await db.obtener_envio(envio_id)
        if envio:
            logger.info(f"✅ Envio obtenido: {envio['remitente']}")
        
        # Obtener lista de envios
        envios = await db.obtener_envios(limit=10)
        logger.info(f"✅ Total de envios en base de datos: {len(envios)}")
        
        # Eliminar envio de prueba
        eliminado = await db.eliminar_envio(envio_id)
        if eliminado:
            logger.info(f"✅ Envio de prueba eliminado")
        
        return True
    except Exception as e:
        logger.error(f"❌ Error en prueba CRUD: {e}")
        return False


async def main():
    """Funcion principal de verificacion."""
    logger.info("=" * 50)
    logger.info("Verificacion de conexion a Supabase - CurrierMsj")
    logger.info("=" * 50)
    
    # Verificar conexion
    if not await verificar_conexion():
        logger.error("No se puede continuar sin conexion a Supabase")
        return
    
    # Probar CRUD
    if not await probar_crud():
        logger.error("Fallo en pruebas CRUD")
        return
    
    logger.info("=" * 50)
    logger.info("✅ Todas las verificaciones pasaron correctamente!")
    logger.info("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())
