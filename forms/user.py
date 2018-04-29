from sqlalchemy import func
from wtforms import StringField, validators as v

from .base import BaseForm
from config.app import db
from models.user import User


class BaseUserForm(BaseForm):
  """ Base user form which has some common fields """

  first_name = StringField("first_name", validators=[
      v.Length(max=User.first_name.type.length),
    ])

  last_name = StringField("last_name", validators=[
      v.Length(max=User.last_name.type.length),
    ])

  username = StringField("username", validators=[
      v.Length(min=2, max=User.username.type.length),
    ])

  email = StringField("email", validators=[
      v.Email(),
      v.Length(max=User.email.type.length),
    ])


class PasswordMixin:
  """ Mixin for adding password fields to a form """

  password = StringField("password", validators=[
      v.Length(min=8, max=100),
      v.EqualTo("confirm_password", message="Passwords must match"),
    ])

  confirm_password = StringField("confirm_password")


class UniqueMixin:
  """ Mixin for verifying the email and username remain unique """

  def validate_email(self, field):
    """ Fails to validate the email if it's already in use """
    if db.session.query(User.id).filter(
        func.lower(User.email) == field.data.lower()).scalar() is not None:
      raise v.ValidationError("Email is already in use")

  def validate_username(self, field):
    """ Fails to validate the username if it's already in use """
    if db.session.query(User.id).filter(
        func.lower(User.username) == field.data.lower()).scalar() is not None:
      raise v.ValidationError("Username is already taken")


class CreateUserForm(PasswordMixin, UniqueMixin, BaseUserForm):
  """ Form used when creating users. Marks several fields as required """

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.add_validators("first_name", v.DataRequired())
    self.add_validators("last_name", v.Optional())
    self.add_validators("username", v.DataRequired())
    self.add_validators("email", v.DataRequired())
    self.add_validators("password", v.DataRequired())


class UpdateUserForm(UniqueMixin, BaseUserForm):
  """ Form used when updating a user's information. All fields are marked as
  optional, and not every field may be updated
  """

  # Users are not allowed to change their username
  username = None

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    # All of these are optional
    self.add_validators("first_name", v.Optional())
    self.add_validators("last_name", v.Optional())
    self.add_validators("username", v.Optional())
    self.add_validators("email", v.Optional())
    self.add_validators("password", v.Optional())

  def validate_email(self, field):
    """ Only validates the email if it changed """
    if field.data.lower() != self.obj.email.lower():
      super().validate_email(field)

  def validate_username(self, field):
    pass