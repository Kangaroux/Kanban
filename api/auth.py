from flaskrouting import page

from api.base import BaseEndpoint
from forms.auth import LoginForm


class AuthAPI(BaseEndpoint):
  """ Authenticates the user and returns a new session token """

  def post(self):
    """ Validates a user's username and password and returns a new token """
    form = LoginForm()

    if not form.validate():
      return self.form_error(form)

    print("email: %r" % form.email.data)
    print("password: %r" % form.password.data)

    return self.ok()


routes = [
  page("", AuthAPI, methods=["POST"])
]