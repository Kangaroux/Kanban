import os

from flask import Flask


def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)

  if test_config:
    app.config.from_mapping(test_config)
  else:
    app.config.from_pyfile("config.py", silent=True)

  os.makedirs(app.instance_path, exist_ok=True)

  import api

  for bp in api.blueprints:
    app.register_blueprint(bp)

  return app