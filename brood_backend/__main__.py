import os
import waitress
from brood_backend.app import create_app

PORT = os.getenv("PORT", 8080)

if __name__ == "__main__":
    app = create_app()
    waitress.serve(app, host="0.0.0.0", port=PORT)
