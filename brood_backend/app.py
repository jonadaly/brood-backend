import connexion
from brood_backend.database import db

from brood_backend.config import init_config
from flask_migrate import Migrate
from loguru import logger


def create_app(testing=False):

    connexion_app = connexion.App(__name__, specification_dir="swagger/")
    connexion_app.add_api(
        "swagger.yaml", strict_validation=True, arguments={"title": "API for Brood"}
    )

    app = connexion_app.app

    init_config(app)

    db.init_app(app)
    Migrate(app, db)

    # Create database if in-memory
    if testing:
        with app.app_context():
            db.create_all()

    logger.info("App ready to serve requests")

    return app
