from uuid import uuid4

from loguru import logger

from brood_backend.database import db
from brood_backend.helpers.errors import EntityNotFoundException
from brood_backend.models.brood import Brood
from brood_backend.helpers.security import hash_password


def create_brood(data: dict) -> dict:

    pass_code: str = data.pop("pass_code")

    logger.debug(f"Creating Brood from data: {data}")

    brood = Brood()
    brood.uuid = str(uuid4())
    brood.name = data["name"]
    brood.hashed_password = hash_password(pass_code)

    logger.debug(f"Saving into database")

    db.session.add(brood)
    db.session.commit()

    logger.debug(f"Responding with data: {brood.to_dict()}")
    return brood.to_dict()


def get_brood_by_uuid(brood_uuid: str):

    logger.debug(f"Getting brood with uuid {brood_uuid}")

    brood: Brood = Brood.query.filter_by(uuid=brood_uuid).first()
    if brood is None:
        raise EntityNotFoundException(f"Couldn't find brood with UUID {brood_uuid}")

    return brood.to_dict()
