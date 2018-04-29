import os
import tempfile
from pytest import fixture

from config.app import create_app, db


@fixture
def app():
  db_fd, db_path = tempfile.mkstemp()

  app = create_app({
    "DATABASE": db_path,
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    "SECRET_KEY": "dev",
    "SERVER_NAME": "localhost",
    "WTF_CSRF_ENABLED": False,
    "TESTING": True,
  })

  db.init_app(app)

  with app.app_context():
    db.create_all()
    yield app
    db.drop_all()

  os.close(db_fd)
  os.unlink(db_path)


@fixture
def client(app):
  """ Creates a flask test client """
  return app.test_client()