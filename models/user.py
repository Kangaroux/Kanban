import os
from argon2 import PasswordHasher

from models.base import BaseModel
from config.app import db


ph = PasswordHasher(time_cost=32, hash_len=32)


class User(BaseModel, db.Model):
  first_name = db.Column(db.String(20))
  last_name = db.Column(db.String(20), nullable=True)

  username = db.Column(db.String(20), unique=True)
  email = db.Column(db.String(100), unique=True)

  password = db.Column(db.String(150))

  def __repr__(self):
    return "<User id=%r username=%r email=%r>" % (self.id, self.username, self.email)

  def set_password(self, password):
    """ Hashes the user's password and sets it """
    self.password = ph.hash(password)

  def check_password(self, password):
    """ Returns True if the given password matches the one in the database """
    try:
      ph.verify(self.password, password)
    except:
      return False

    return True
