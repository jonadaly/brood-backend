from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


TESTING_DB_URL = "sqlite://"

db = SQLAlchemy()


def init_database(app, testing=False):
    db.init_app(app)
    Migrate(app, db)

    # Create database if in-memory
    if testing:
        with app.app_context():
            db.create_all()
