from django.contrib.auth.models import AbstractUser
from django.db import models

from lib.models import BaseModel


class User(BaseModel, AbstractUser):
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username"]
  SERIALIZE_FIELDS = ("first_name", "last_name", "username", "email", "date_created")

  username = models.CharField(max_length=20)
  email = models.EmailField(unique=True)

  # For consistency with other models, this is replaced by BaseModel.date_created
  date_joined = None
