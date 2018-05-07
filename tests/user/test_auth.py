from flask import session, url_for

from forms.auth import LoginForm
from models.user import User
from lib import response_codes as http
from tests.conftest import create_auth_user, create_user, login, logout


def test_login_and_logout(client, user_data):
  """ Test logging in and logging out """
  create_user(user_data)
  assert login(client, user_data["email"], user_data["password"]).status_code == http.OK
  user = User.query.first()

  assert session["user_id"] == user.id
  assert logout(client).status_code == http.OK
  assert "user_id" not in session
