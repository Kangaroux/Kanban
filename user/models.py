from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from lib.models import BaseModel


class CustomUserManager(BaseUserManager):
  """ Custom user manager which removes the username field """

  use_in_migrations = True

  def _create_user(self, email, password, **extra_fields):
    email = self.normalize_email(email)
    user = self.model( email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email=None, password=None, **extra_fields):
    extra_fields.setdefault("is_staff", False)
    extra_fields.setdefault("is_superuser", False)
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault("is_superuser", True)

    if extra_fields.get("is_staff") is not True:
        raise ValueError("Superuser must have is_staff=True.")
    if extra_fields.get("is_superuser") is not True:
        raise ValueError("Superuser must have is_superuser=True.")

    return self._create_user(email, password, **extra_fields)


class User(BaseModel, AbstractUser):
  objects = CustomUserManager()

  # The user logs in using their email
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["first_name"]
  SERIALIZE_FIELDS = ("id", "first_name", "last_name", "email", "date_created", "date_updated")

  # Users have a display name for each project
  username = None
  email = models.EmailField(unique=True)

  # Replace AbstractUser.date_joined with BaseModel.date_created for consistency
  date_joined = None

  def __str__(self):
    return "(%d) %s, %s (%s)" % (self.id, self.last_name, self.first_name, self.email)

  def __repr__(self):
    return "<User id=%r email=%r username=%r>" % (self.id, self.email, self.username)

  def get_display_name(self):
    return self.username