from wtforms import StringField, validators as v

from forms import filters as f
from forms.user import BaseUserForm, PasswordMixin


class LoginForm(PasswordMixin, BaseUserForm):
  FIELDS = ["email", "password"]