from django import forms

from lib.forms import SimpleEmailField
from user.models import User


class BaseUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ("first_name", "last_name", "email")


class CreateUserForm(BaseUserForm):
  password = forms.CharField(min_length=8, max_length=100, strip=False,
    error_messages={ "min_length": "Password must be at least %(limit_value)d characters." })
  confirm_password = forms.CharField(strip=False)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["first_name"].required = True

  def clean(self):
    d = self.cleaned_data
    password = d.get("password")
    password2 = d.get("confirm_password")

    if password and password != password2:
      self.add_error("confirm_password", "Passwords must match")


class LoginForm(forms.Form):
  email = SimpleEmailField()
  password = forms.CharField(strip=False)