from wtforms import StringField, validators as v

from forms import filters as f
from forms.user import BaseUserForm, PasswordMixin


class LoginForm(PasswordMixin, BaseUserForm):
  FIELDS = ["email", "password"]

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.set_validators("email", v.DataRequired())
    self.set_validators("password", v.DataRequired())