from flask import session

from flaskrouting import page

from api.base import *
from forms.auth import LoginForm
from lib import auth
from models.user import User


class AuthAPI(BaseEndpoint):
  """ Authenticates the user and returns a new session token """

  def get(self):
    if "user_id" in session:
      return self.ok()

    return self.error(msg="You are not logged in.", code=http.NO_AUTH)

  def post(self):
    """ Validates a user's username and password and returns a new token """
    form = LoginForm()

    if not form.validate():
      return self.form_error(form)

    u = User.query.filter_by(email=form.email.data).first()

    if not u or not u.check_password(form.password.data):
      return self.error(msg="Email or password is incorrect.", code=http.BAD_REQUEST)

    auth.login(u)

    return self.ok()

  def delete(self):
    was_logged_in = "user_id" in session

    auth.logout()

    return self.ok(data={ "was_logged_in": was_logged_in })


routes = [
  page("", AuthAPI, methods=["GET", "POST", "DELETE"])
]