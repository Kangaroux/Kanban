import os
import tempfile
from pytest import fixture

from config.app import create_app


@fixture
def app():
  db_fd, db_path = tempfile.mkstemp()

  app = create_app({
    "SQLALCHEMY_DATABASE_URI": db_path,
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    "TESTING": True,
  })

  yield app

  os.close(db_fd)
  os.unlink(db_path)


@fixture
def client(app):
  return app.test_client()