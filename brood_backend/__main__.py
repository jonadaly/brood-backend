import connexion
import os


SERVER_PORT = os.getenv("SERVER_PORT", 8080)

if __name__ == "__main__":
    app = connexion.App(__name__, specification_dir="swagger/")
    app.add_api(
        "swagger.yaml",
        strict_validation=True,
        arguments={"title": "API for Brood"},
    )
    app.run(port=SERVER_PORT)
