from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
  USERNAME_FIELD = "email"

  username = models.CharField(max_length=20)
  email = models.EmailField()