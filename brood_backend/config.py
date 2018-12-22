from flask_env import MetaFlaskEnv


class Configuration(metaclass=MetaFlaskEnv):

    DATABASE_URL: None
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def init_config(app):

    app.config.from_object(Configuration)

    database_vars = [
        "DATABASE_USER",
        "DATABASE_PASSWORD",
        "DATABASE_HOST",
        "DATABASE_PORT",
        "DATABASE_NAME",
    ]

    missing = [d for d in database_vars if app.config[d] is None]
    if missing:
        raise EnvironmentError(
            f"Error starting, missing env vars: {', '.join(missing)}."
        )

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = app.config["DATABASE_URL"]
