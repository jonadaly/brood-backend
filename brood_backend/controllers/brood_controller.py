from uuid import uuid4

from loguru import logger

from brood_backend.database import db
from brood_backend.models.brood import Brood
from brood_backend.helpers.security import hash_password


def create_brood(data: dict) -> dict:

    passcode: str = data.pop("passcode")

    logger.debug(f"Creating Brood from data: {data}")

    brood = Brood()
    brood.uuid = str(uuid4())
    brood.name = data["name"]
    brood.hashed_password = hash_password(passcode)

    logger.debug(f"Saving into database")

    db.session.add(brood)
    db.session.commit()

    logger.debug(f"Responding with data: {brood.to_dict()}")
    return brood.to_dict()
