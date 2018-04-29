from flask_wtf import FlaskForm
from sqlalchemy import func
from wtforms import StringField, validators as v

from config.app import db
from models.user import User


class CreateUserForm(FlaskForm):
  first_name = StringField("first_name", validators=[
      v.DataRequired(),
      v.Length(max=User.first_name.type.length),
    ])

  last_name = StringField("last_name", validators=[
      v.Optional(),
      v.Length(max=User.last_name.type.length),
    ])

  username = StringField("username", validators=[
      v.DataRequired(),
      v.Length(min=2, max=User.username.type.length),
    ])

  email = StringField("email", validators=[
      v.DataRequired(),
      v.Email(),
      v.Length(max=User.email.type.length),
    ])

  password = StringField("password", validators=[
      v.DataRequired(),
      v.Length(min=8, max=100),
      v.EqualTo("confirm_password", message="Passwords must match"),
    ])

  confirm_password = StringField("confirm_password")


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