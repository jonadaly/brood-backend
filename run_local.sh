#!/usr/bin/env bash

export SERVER_PORT=${1-5000}
export FLASK_APP=brood_backend/autoapp.py
export DATABASE_URL=postgres://brood:brood@localhost:5432/brood
export SQLALCHEMY_TRACK_MODIFICATIONS=False

flask db upgrade
python -m brood_backend
