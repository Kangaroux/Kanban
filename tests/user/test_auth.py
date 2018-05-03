from flask import url_for

from forms.auth import LoginForm


def test_login(client):
  data = {
    "email": "test@test.com",
    "password": "password123"
  }
  client.post(url_for("api.auth"), json=data)