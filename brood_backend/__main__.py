import os
import waitress
from brood_backend.app import create_app

SERVER_PORT = os.getenv("SERVER_PORT", 8080)

if __name__ == "__main__":
    app = create_app()
    waitress.serve(app, host="0.0.0.0", port=SERVER_PORT)
