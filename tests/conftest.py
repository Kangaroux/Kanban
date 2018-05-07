import os
import tempfile

from flask import url_for
from models.user import User
from lib import response_codes as http
from pytest import fixture

from config.app import create_app, db


def login(client, email, password):
  return client.post(url_for("api.auth"), json={
    "email": email,
    "password": password
  })

def logout(client):
  return client.delete(url_for("api.auth"))

def create_user(user_data):
  """ Creates and returns a new user """
  u = User(**user_data)
  u.set_password(user_data["password"])

  db.session.add(u)
  db.session.commit()

  return u

def create_auth_user(client, user_data):
  """ Creates, logs in, and returns a new user """
  create_user(user_data)
  login(client, user_data["email"], user_data["password"])
  return User.query.filter_by(email=user_data["email"]).first()


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

  with app.app_context():
    yield app

  os.close(db_fd)
  os.unlink(db_path)

@fixture
def client(app):
  """ Creates a flask test client """
  return app.test_client()

@fixture
def user_data():
  """ Returns some sample data for a user """
  return {
    "first_name": "john",
    "last_name": "smith",
    "email": "test@test.com",
    "password": "mysecretpassword",
    "username": "username123"
  }.copy()
