from flask import session, url_for

from forms.auth import LoginForm
from models.user import User
from lib import response_codes as http
from tests.conftest import create_auth_user, create_user, login, logout


def test_login_and_logout(client, user_data):
  create_user(user_data)
  assert login(client, user_data["email"], user_data["password"]).status_code == http.OK
  user = User.query.first()

  assert session["user_id"] == user.id
  assert logout(client).status_code == http.OK
  assert "user_id" not in session

def test_auth_check(client, user_data):
  user = create_auth_user(client, user_data)
  r = client.get(url_for("api.auth"))

  assert r.status_code == http.OK

  logout(client)
  r = client.get(url_for("api.auth"))

  assert r.status_code == http.NO_AUTH