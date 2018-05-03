import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)

  # Load the config
  if test_config:
    app.config.from_mapping(test_config)
  else:
    app.config.from_object("config.settings")

  os.makedirs(app.instance_path, exist_ok=True)

  # Register the API routes
  from api.urls import urls
  urls.register(app)

  # Setup the database
  db.init_app(app)

  return app