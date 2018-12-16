from uuid import uuid4

from loguru import logger

from brood_backend.database import db
from brood_backend.helpers.errors import EntityNotFoundException
from brood_backend.models.chicken import Chicken
from brood_backend.models.peck import Peck


def create_peck(data: dict) -> dict:

    logger.debug(f"Creating Peck from data: {data}")

    chicken_uuid: str = data["chicken_uuid"]
    chicken = Chicken.query.filter_by(uuid=chicken_uuid).first()
    if chicken is None:
        raise EntityNotFoundException(f"Unknown chicken UUID '{chicken_uuid}'")

    peck = Peck()
    peck.uuid = str(uuid4())
    peck.latitude = data["latitude"]
    peck.longitude = data["longitude"]
    peck.status = data["status"]
    peck.chicken_uuid = chicken_uuid

    logger.debug(f"Saving into database")

    db.session.add(peck)
    db.session.commit()

    logger.debug(f"Responding with data: {peck.to_dict()}")
    return peck.to_dict()
