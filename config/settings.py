import os

PROD = bool(os.environ.get("PROD", False))
DEVELOPMENT = not PROD

SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
SERVER_NAME = os.environ.get("HOST", "localhost")

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///:memory:")
SQLALCHEMY_TRACK_MODIFICATIONS = False

