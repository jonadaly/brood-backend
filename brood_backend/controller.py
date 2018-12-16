from uuid import uuid4

from connexion import request

from brood_backend.database import db
from brood_backend.models.peck import Peck

from loguru import logger


def get_brood():
    return "Not implemented", 501


def create_peck():
    _json = request.get_json()
    return _create_peck_from_dict(_json)


def _create_peck_from_dict(data: dict):

    logger.debug(f"Creating Peck from data: {data}")
    peck = Peck()
    peck.uuid = str(uuid4())
    peck.latitude = data["latitude"]
    peck.longitude = data["longitude"]
    peck.status = data["status"]

    logger.debug(f"Saving into database")

    db.session.add(peck)
    db.session.commit()

    logger.debug(f"Responding with data: {peck.to_dict()}")
    return peck.to_dict()
