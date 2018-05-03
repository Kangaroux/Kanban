from flask import Blueprint, jsonify

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

    # u = User.objects.get(email=form.email.data)

    # if not u or not u.check_password(form.password.data)


view = AuthAPI.as_view("auth")
blueprint = Blueprint("auth", __name__, url_prefix="/auth")

blueprint.add_url_rule("/", view_func=view, methods=["POST"])