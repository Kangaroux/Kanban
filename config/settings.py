import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROD = bool(os.environ.get("PROD", False))
DEVELOPMENT = not PROD
DEBUG = DEVELOPMENT

SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
SERVER_NAME = os.environ.get("HOST")

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = False

SESSION_COOKIE_HTTPONLY = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG