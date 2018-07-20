import re

from django.core.exceptions import ValidationError
from django.forms import EmailField


class SimpleEmailValidator:
  message = "Enter a valid email address."
  regex_email_simple = re.compile(r'[^\s@]+@[^\s\.]+\.[\S]+')

  def __call__(self, value):
    if not value or not self.regex_email_simple.fullmatch(value):
      raise ValidationError(self.message)


class SimpleEmailField(EmailField):
  """ An email field with a simple check to see if an email looks good enough.
  While not as comprehensive as the builtin EmailField, it serves the same purpose
  and allows for quick debugging by using emails like "a@a.a"
  """

  default_validators = [SimpleEmailValidator()]