from datetime import datetime

import requests
from loguru import logger

from brood_backend.database import db
from brood_backend.helpers.errors import ServiceUnavailableException


class Chicken(db.Model):

    uuid = db.Column(db.String(length=36), primary_key=True)
    created = db.Column(
        db.DateTime, unique=False, nullable=False, default=datetime.utcnow
    )
    name = db.Column(db.String(), unique=False, nullable=False)
    pecks = db.relationship("Peck", back_populates="chicken")
    brood_uuid = db.Column(db.String, db.ForeignKey("brood.uuid"), nullable=False)
    brood = db.relationship("Brood", back_populates="chickens")

    def to_dict(self) -> dict:
        pecks = sorted(self.pecks, key=lambda x: x.created, reverse=True)
        if len(pecks) > 0:
            latest_peck = pecks[0]
            weather: dict = self._get_weather_at(
                latitude=latest_peck.latitude, longitude=latest_peck.longitude
            )
            temperature = weather["main"]["temp"]
            openweather_icon_id = weather["weather"][0]["icon"]
            status = latest_peck.status
        else:
            temperature = None
            openweather_icon_id = None
            status = None
        return {
            "uuid": self.uuid,
            "created": self.created,
            "brood_uuid": self.brood_uuid,
            "name": self.name,
            "status": status,
            "temperature": temperature,
            "openweather_icon_id": openweather_icon_id,
        }

    @staticmethod
    def _get_weather_at(latitude: float, longitude: float) -> dict:

        OPENWEATHER_API_KEY = "1794ea6b8378ae4c6ce97a5a7a9d5d95"

        try:
            logger.debug(f"Getting weather at lat={latitude}, lon={longitude}")
            url: str = f"http://api.openweathermap.org/data/2.5/weather" f"?lat={latitude}" f"&lon={longitude}" f"&units=metric" f"&appid={OPENWEATHER_API_KEY}"
            logger.debug(f"Url: {url}")
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except (requests.ConnectionError, requests.HTTPError):
            raise ServiceUnavailableException(f"Couldn't contact openweather API")
