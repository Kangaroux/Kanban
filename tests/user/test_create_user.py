import pytest
from flask import url_for

from forms.user import CreateUserForm
from models.user import User


def test_ok(client, user_data):
  d = user_data

  del d["last_name"]
  d["confirm_password"] = d["password"]

  r = client.post(url_for("api.create_user"), json=d)

  assert r.get_json() == { "status": "ok" }
  assert r.status_code == 200

  u = User.query.first()

  assert u.first_name == d["first_name"]
  assert not u.last_name
  assert u.username == d["username"]
  assert u.email == d["email"]
  assert u.check_password(d["password"])

def test_duplicate_info(client, user_data):
  d = user_data
  d["confirm_password"] = d["password"]

  client.post(url_for("api.create_user"), json=user_data)
  r = client.post(url_for("api.create_user"), json=user_data)
  assert r.status_code == 400
  assert r.get_json() == {
    "status": "error",
    "fields": {
      "email": "Email is already in use",
      "username": "Username is already taken"
    }
  }