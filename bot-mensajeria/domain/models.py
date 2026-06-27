from dataclasses import dataclass
from typing import Any, Optional


@dataclass(frozen=True)
class IncomingMessage:
    phone_number: str
    text: str
    message_type: str = "text"
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    raw: Optional[dict[str, Any]] = None

    @property
    def has_location(self) -> bool:
        return self.latitude is not None and self.longitude is not None
