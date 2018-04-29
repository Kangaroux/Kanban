import pytest
from flask import url_for

from forms.user import CreateUserForm
from models.user import User


def test_ok(client):
  r = client.post(url_for("api.create_user"), json={
    "first_name": "jesse",
    "email": "TEST@test.com",
    "password": "mysecretpassword",
    "confirm_password": "mysecretpassword",
    "username": "username123"
  })

  assert r.get_json() == { "status": "ok" }
  assert r.status_code == 200

  u = User.query.first()

  assert u.first_name == "jesse"
  assert not u.last_name
  assert u.username == "username123"
  assert u.email == "TEST@test.com"
  assert u.check_password("mysecretpassword")