from typing import Optional

from services.supabase_repository import SupabaseRepository


_repository = SupabaseRepository()


def obtener_estado(phone_number: str) -> Optional[dict]:
    return _repository.get_user_state(phone_number)


def crear_estado(phone_number: str, paso: str = "menu", datos: dict = None) -> dict:
    return _repository.create_user_state(phone_number, paso, datos or {})


def actualizar_estado(phone_number: str, paso: str = None, datos: dict = None) -> None:
    _repository.update_user_state(phone_number, paso, datos)


def reset_estado(phone_number: str) -> None:
    _repository.reset_user_state(phone_number)


def obtener_datos_temp(phone_number: str) -> dict:
    return _repository.get_temp_data(phone_number)


def guardar_datos_temp(phone_number: str, datos: dict) -> None:
    _repository.save_temp_data(phone_number, datos)


def buscar_faq(pregunta: str) -> Optional[str]:
    return _repository.search_faq(pregunta)


def guardar_reporte(phone_number: str, desc: str) -> int:
    return _repository.save_report(phone_number, desc)


def guardar_envio(datos: dict) -> int:
    return _repository.save_shipment(datos)


def obtener_envios_por_telefono(phone_number: str, limit: int = 10) -> list:
    return _repository.get_shipments_by_phone(phone_number, limit)


def obtener_envio_por_id(envio_id: int) -> Optional[dict]:
    return _repository.get_shipment_by_id(envio_id)


def obtener_envio_por_tracking(tracking_code: str) -> Optional[dict]:
    return _repository.get_shipment_by_tracking(tracking_code)
