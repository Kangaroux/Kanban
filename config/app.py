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
  import api
  
  for bp in api.blueprints:
    app.register_blueprint(bp)

  # Setup the database
  db.init_app(app)

  return app