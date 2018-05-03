from wtforms import StringField, validators as v

from forms.base import BaseForm


class LoginForm(BaseForm):
  email = StringField("email", validators=[v.DataRequired()])
  password = StringField("password", validators=[v.DataRequired()])