from uuid import uuid4

from loguru import logger

from brood_backend.database import db
from brood_backend.helpers.errors import EntityNotFoundException
from brood_backend.models.brood import Brood
from brood_backend.models.chicken import Chicken


def create_chicken(data: dict) -> dict:

    logger.debug(f"Creating Chicken from data: {data}")

    brood_uuid: str = data["brood_uuid"]
    brood = Brood.query.filter_by(uuid=brood_uuid).first()
    if brood is None:
        raise EntityNotFoundException(f"Unknown chicken UUID '{brood_uuid}'")

    chicken = Chicken()
    chicken.uuid = str(uuid4())
    chicken.name = data["name"]
    chicken.brood_uuid = brood_uuid

    logger.debug(f"Saving into database")

    db.session.add(chicken)
    db.session.commit()

    logger.debug(f"Responding with data: {chicken.to_dict()}")
    return chicken.to_dict()
