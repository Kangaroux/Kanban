from api.base import *
from forms.auth import LoginForm
from lib import auth
from models.user import User


class AuthAPI(BaseAPIEndpoint):
  """ Authenticates the user and returns a new session token """

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
