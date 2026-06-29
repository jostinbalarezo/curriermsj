import logging
from datetime import datetime
from typing import Any

from flask import Flask, jsonify, request

import config
from bot.courier_bot import CourierBot
from domain.models import IncomingMessage


logger = logging.getLogger(__name__)


class WhatsAppWebhookParser:
    @staticmethod
    def parse(payload: dict[str, Any]) -> list[IncomingMessage]:
        events: list[IncomingMessage] = []

        for entry in payload.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                for message in value.get("messages", []):
                    event = WhatsAppWebhookParser._parse_message(message)
                    if event:
                        events.append(event)

        return events

    @staticmethod
    def _parse_message(message: dict[str, Any]) -> IncomingMessage | None:
        phone_number = message.get("from")
        if not phone_number:
            return None

        message_type = message.get("type", "text")
        if message_type == "text":
            return IncomingMessage(
                phone_number=phone_number,
                text=message.get("text", {}).get("body", ""),
                message_type="text",
                raw=message,
            )

        if message_type == "interactive":
            interactive = message.get("interactive", {})
            if interactive.get("type") == "button_reply":
                reply = interactive.get("button_reply", {})
                return IncomingMessage(
                    phone_number=phone_number,
                    text=reply.get("id") or reply.get("title", ""),
                    message_type="interactive_button",
                    raw=message,
                )
            if interactive.get("type") == "list_reply":
                reply = interactive.get("list_reply", {})
                return IncomingMessage(
                    phone_number=phone_number,
                    text=reply.get("id") or reply.get("title", ""),
                    message_type="interactive_list",
                    raw=message,
                )

        if message_type == "location":
            location = message.get("location", {})
            return IncomingMessage(
                phone_number=phone_number,
                text="ubicacion_recibida",
                message_type="location",
                latitude=location.get("latitude"),
                longitude=location.get("longitude"),
                raw=message,
            )

        if message_type == "reaction":
            reaction = message.get("reaction", {})
            return IncomingMessage(
                phone_number=phone_number,
                text=f"Reacción: {reaction.get('emoji', '')}",
                message_type="reaction",
                raw=message,
            )

        return IncomingMessage(
            phone_number=phone_number,
            text="",
            message_type=message_type,
            raw=message,
        )


def create_app(bot: CourierBot) -> Flask:
    app = Flask(__name__)

    @app.get("/webhook")
    def verify_webhook():
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == config.WEBHOOK_VERIFY_TOKEN:
            logger.info("Webhook verificado correctamente")
            return challenge or "", 200

        logger.warning("Intento de verificación fallido")
        return "Forbidden", 403

    @app.post("/webhook")
    def receive_message():
        payload = request.get_json(silent=True) or {}
        if payload.get("object") != "whatsapp_business_account":
            return "Not Found", 404

        try:
            for event in WhatsAppWebhookParser.parse(payload):
                bot.process(event)
        except Exception as exc:
            logger.exception("Error procesando webhook: %s", exc)

        return "OK", 200

    @app.get("/health")
    def health():
        return jsonify(
            {
                "status": "ok",
                "service": "currier_bot",
                "time": datetime.now().isoformat(),
            }
        ), 200

    @app.get("/api/envios")
    def get_all_envios():
        try:
            url = f"{bot.repository._table(bot.repository.table_envios)}?select=*&order=creado_en.desc"
            data = bot.repository._request("GET", url)
            return jsonify(data), 200
        except Exception as e:
            logger.exception("Error al obtener envíos: %s", e)
            return jsonify({"error": str(e)}), 500

    @app.get("/api/system-stats")
    def get_system_stats():
        try:
            clientes_url = f"{bot.repository._table(bot.repository.table_clientes)}?select=*"
            estados_url = f"{bot.repository._table(bot.repository.table_estado)}?select=*"
            reportes_url = f"{bot.repository._table(bot.repository.table_reportes)}?select=*&order=creado_en.desc"
            
            clientes = bot.repository._request("GET", clientes_url)
            estados = bot.repository._request("GET", estados_url)
            reportes = bot.repository._request("GET", reportes_url)
            
            return jsonify({
                "clientes": clientes,
                "estados": estados,
                "reportes": reportes
            }), 200
        except Exception as e:
            logger.exception("Error al obtener estadísticas del sistema: %s", e)
            return jsonify({"error": str(e)}), 500

    @app.after_request
    def add_cors_headers(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
        response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        return response

    return app
