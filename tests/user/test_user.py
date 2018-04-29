import pytest
from flask import url_for

from forms.user import CreateUserForm
from models.user import User


def test_add_user(client, user_data):
  d = user_data

  del d["last_name"]
  d["confirm_password"] = d["password"]

  r = client.post(url_for("api.user"), json=d)

  assert r.status_code == 200
  assert r.get_json() == { "status": "ok" }

  u = User.query.first()

  assert u.first_name == d["first_name"]
  assert not u.last_name
  assert u.username == d["username"]
  assert u.email == d["email"]
  assert u.check_password(d["password"])

def test_add_duplicate_user(client, user_data):
  d = user_data
  d["confirm_password"] = d["password"]

  client.post(url_for("api.user"), json=user_data)
  r = client.post(url_for("api.user"), json=user_data)
  assert r.status_code == 400
  assert r.get_json() == {
    "status": "error",
    "fields": {
      "email": "Email is already in use",
      "username": "Username is already taken"
    }
  }

def test_get_existing_user(client, user):
  r = client.get("%s%d" % (url_for("api.user"),  user.id))
  assert r.status_code == 200
  assert r.get_json() == {
    "status": "ok",
    "user": {
      "id": user.id,
      "first_name": user.first_name,
      "last_name": user.last_name,
      "username": user.username,
      "email": user.email,
      "joined": user.created_at.isoformat()
    }
  }

def test_get_invalid_user(client):
  r = client.get("%s%d" % (url_for("api.user"),  1234))
  assert r.status_code == 404
  assert r.get_json() == {
    "status": "error",
    "msg": "User does not exist."
  }