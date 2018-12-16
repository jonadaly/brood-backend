import connexion
from brood_backend.database import init_database

from brood_backend.config import init_config
from loguru import logger

from brood_backend.helpers.errors import init_error_handler


def create_app(testing=False):

    connexion_app = connexion.App(__name__, specification_dir="swagger/")
    connexion_app.add_api(
        "swagger.yaml", strict_validation=True, arguments={"title": "API for Brood"}
    )
    app = connexion_app.app

    init_config(app)
    init_error_handler(app)
    init_database(app)

    logger.info("App ready to serve requests")
    return app
