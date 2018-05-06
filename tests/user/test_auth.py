from flask import url_for

from forms.auth import LoginForm


def test_login(client, user, user_data):
  data = {
    "email": user.email,
    "password": user_data["password"]
  }

  r = client.post(url_for("api.auth"), json=data)

  assert r.status_code == 200