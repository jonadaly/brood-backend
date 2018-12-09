import connexion


def create_app(testing=False):

    connexion_app = connexion.App(__name__, specification_dir="swagger/")
    connexion_app.add_api(
        "swagger.yaml",
        strict_validation=True,
        arguments={"title": "API for Brood"},
    )

    app = connexion_app.app

    # # # Create database if in-memory
    # if testing:
    #     with app.app_context():
            # db.create_all()

    # Done!
    app.logger.info("App ready to serve requests")

    return app
