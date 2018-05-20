from django.contrib.auth.models import AbstractUser
from django.db import models

from lib.models import BaseModel


class User(BaseModel, AbstractUser):
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username"]
  SERIALIZE_FIELDS = ("id", "first_name", "last_name", "username", "email", "date_created")

  username = models.CharField(max_length=20)
  email = models.EmailField(unique=True)

  # Replace AbstractUser.date_joined with BaseModel.date_created for consistency
  date_joined = None

  def __str__(self):
    return "%s (%s)" % (self.username, self.email)

  def __repr__(self):
    return "<User id=%r email=%r username=%r>" % (self.id, self.email, self.username)