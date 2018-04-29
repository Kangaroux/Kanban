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

@fixture
def user_data(app):
  """ Returns some sample data for a suer """
  return {
    "first_name": "john",
    "last_name": "smith",
    "email": "test@test.com",
    "password": "mysecretpassword",
    "username": "username123"
  }.copy()

@fixture
def user(app, user_data):
  """ Returns a fresh user object created from the sample data """
  u = User(**user_data)
  u.set_password(user_data["password"])

  db.session.add(u)
  db.session.commit()

  return u