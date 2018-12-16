from connexion import request
from flask import jsonify

from brood_backend.controllers import (
    peck_controller,
    chicken_controller,
    brood_controller,
)


def get_brood():
    return "Not implemented", 501


def create_peck():
    _json = request.get_json()
    return jsonify(peck_controller.create_peck(_json))


def create_chicken():
    _json = request.get_json()
    return jsonify(chicken_controller.create_chicken(_json))


def create_brood():
    _json = request.get_json()
    return jsonify(brood_controller.create_brood(_json))
