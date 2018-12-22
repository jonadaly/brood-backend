# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "brood_backend"
VERSION = "0.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "flask",
    "connexion",
    "waitress",
    "Flask-SQLAlchemy",
    "loguru",
    "psycopg2-binary",
    "Flask-Migrate",
    "Flask-Env",
    "requests",
]

setup(
    name=NAME,
    version=VERSION,
    description="Python backend for Brood",
    author_email="jondaly01@gmail.com",
    url="https://jondalybrood.com",
    keywords=["Swagger", "API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={"": ["swagger.yaml"]},
    include_package_data=True,
    long_description="""\
    Python backend for Brood
    """,
)
