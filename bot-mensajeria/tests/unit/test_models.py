import pytest
from domain.models import IncomingMessage


class TestIncomingMessage:
    def test_create_text_message(self):
        msg = IncomingMessage(
            phone_number="593991234567",
            text="Hola",
            message_type="text",
        )
        assert msg.phone_number == "593991234567"
        assert msg.text == "Hola"
        assert msg.message_type == "text"
        assert msg.has_location is False
        assert msg.latitude is None
        assert msg.longitude is None

    def test_create_location_message(self):
        msg = IncomingMessage(
            phone_number="593991234567",
            text="",
            message_type="location",
            latitude=-0.22985,
            longitude=-78.52495,
        )
        assert msg.message_type == "location"
        assert msg.has_location is True
        assert msg.latitude == -0.22985
        assert msg.longitude == -78.52495

    def test_create_interactive_message(self):
        msg = IncomingMessage(
            phone_number="593991234567",
            text="cotizar",
            message_type="interactive",
        )
        assert msg.message_type == "interactive"
        assert msg.text == "cotizar"

    def test_default_has_location_false(self):
        msg = IncomingMessage(phone_number="593991234567", text="test", message_type="text")
        assert msg.has_location is False

    def test_empty_text(self):
        msg = IncomingMessage(phone_number="593991234567", text="", message_type="text")
        assert msg.text == ""

    def test_repr(self):
        msg = IncomingMessage(phone_number="593991234567", text="hola", message_type="text")
        r = repr(msg)
        assert "593991234567" in r
        assert "hola" in r
