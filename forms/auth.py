from wtforms import StringField, validators as v

from forms import filters as f
from forms.base import BaseForm


class LoginForm(BaseForm):
  email = StringField("email", validators=[v.DataRequired()], filters=[f.strip, f.lower])
  password = StringField("password", validators=[v.DataRequired()])