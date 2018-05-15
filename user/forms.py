from django import forms

from user.models import User


class BaseUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ("first_name", "last_name", "username", "email")


class CreateUserForm(BaseUserForm):
  password = forms.CharField(min_length=8, max_length=100, strip=False)
  confirm_password = forms.CharField(strip=False)

  def clean(self):
    d = self.cleaned_data

    if d.get("password") != d.get("confirm_password"):
      self.add_error("confirm_password", "Passwords must match")


class LoginForm(forms.ModelForm):
  email = forms.EmailField()
  password = forms.CharField()