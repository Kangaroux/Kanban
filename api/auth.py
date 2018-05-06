from flaskrouting import page

from api.base import BaseEndpoint
from forms.auth import LoginForm
from models.user import User


class AuthAPI(BaseEndpoint):
  """ Authenticates the user and returns a new session token """

  def post(self):
    """ Validates a user's username and password and returns a new token """
    form = LoginForm()

    if not form.validate():
      return self.form_error(form)

    u = User.query.filter_by(email=form.email.data).first()

    if not u or not u.check_password(form.password.data):
      return self.error(msg="Email or password is incorrect.", code=400)

    return self.ok()


routes = [
  page("", AuthAPI, methods=["POST"])
]