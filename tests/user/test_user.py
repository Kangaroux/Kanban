import pytest
from flask import session, url_for

from forms.user import CreateUserForm
from lib import response_codes as http
from models.user import User
from tests.conftest import create_auth_user, create_user


def test_add_user(client, user_data):
  """ Test adding a user """
  d = user_data

  del d["last_name"]
  d["confirm_password"] = d["password"]

  r = client.post(url_for("api.user"), json=d)
  u = User.query.first()

  assert r.get_json() == { "status": "ok", "user_id": u.id }
  assert r.status_code == http.OK

  assert u.first_name == d["first_name"]
  assert not u.last_name
  assert u.username == d["username"]
  assert u.email == d["email"]
  assert u.check_password(d["password"])

def test_add_duplicate_user(client, user_data):
  """ Test adding a user whose username and email are already taken """
  d = user_data
  d["confirm_password"] = d["password"]

  client.post(url_for("api.user"), json=user_data)
  r = client.post(url_for("api.user"), json=user_data)
  assert r.status_code == 400
  assert r.get_json() == {
    "status": "error",
    "fields": {
      "email": "Email is already in use.",
      "username": "Username is already taken."
    }
  }

def test_get_existing_user(client, user_data):
  """ Test getting a user's information """
  user = create_user(user_data)

  r = client.get(url_for("api.user", user_id=user.id))
  assert r.status_code == http.OK
  assert r.get_json() == {
    "status": "ok",
    "user": {
      "id": user.id,
      "first_name": user.first_name,
      "last_name": user.last_name,
      "username": user.username,
      "email": user.email,
      "created": user.created.isoformat()
    }
  }

def test_get_invalid_user(client):
  """ Test trying to get info for a user who does not exist """
  r = client.get(url_for("api.user", user_id=1234))
  assert r.status_code == 404
  assert r.get_json() == {
    "status": "error",
    "msg": "User does not exist."
  }

def test_login_required(client):
  assert client.delete(url_for("api.user", user_id=1234)).status_code == http.NO_AUTH

def test_delete_user(client, user_data):
  """ Test deleting a user """
  user = create_auth_user(client, user_data)
  r = client.delete(url_for("api.user", user_id=user.id))

  # Since we deleted our account we should have been logged out
  assert r.status_code == http.OK
  assert "user_id" not in session
