from uuid import uuid4

from connexion import request

from brood_backend.database import db
from brood_backend.errors import EntityNotFoundException
from brood_backend.models.brood import Brood
from brood_backend.models.chicken import Chicken
from brood_backend.models.peck import Peck

from loguru import logger

from brood_backend.security import hash_password


def get_brood():
    return "Not implemented", 501


def create_peck():
    _json = request.get_json()
    return _create_peck_from_dict(_json)


def create_chicken():
    _json = request.get_json()
    return _create_chicken_from_dict(_json)


def create_brood():
    _json = request.get_json()
    return _create_brood_from_dict(_json)


def _create_peck_from_dict(data: dict) -> dict:

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


def _create_chicken_from_dict(data: dict) -> dict:

    logger.debug(f"Creating Chicken from data: {data}")
    chicken = Chicken()
    chicken.uuid = str(uuid4())
    chicken.name = data["name"]

    logger.debug(f"Saving into database")

    db.session.add(chicken)
    db.session.commit()

    logger.debug(f"Responding with data: {chicken.to_dict()}")
    return chicken.to_dict()


def _create_brood_from_dict(data: dict) -> dict:

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


def _hash_ascii_with_salt(ascii_string, salt):

    code_bytes = bytes(ascii_string, "ascii")
    salt_bytes = bytes(salt, "ascii")

    return scrypt(code_bytes, salt_bytes, 256, 16384, 8, 1)
