import pytest

from flask import url_for, g
from forms.user import CreateUserForm


def test_ok(client):
  r = client.post(url_for("api.create_user"), json={
    "first_name": "jesse",
    "email": "test@test.com",
    "password": "mysecretpassword",
    "confirm_password": "mysecretpassword",
    "username": "username123"
  })

  assert r.get_json() == { "status": "ok" }
  assert r.status_code == 200
