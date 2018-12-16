#!/usr/bin/env bash

export SERVER_PORT=${1-5000}
export FLASK_APP=brood_backend/autoapp.py
export DATABASE_HOST=localhost
export DATABASE_PORT=5432
export DATABASE_USER=brood
export DATABASE_PASSWORD=brood
export DATABASE_NAME=brood
export SQLALCHEMY_TRACK_MODIFICATIONS=False

flask db upgrade
python -m brood_backend
