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
    """ Sets the user's new password. This generates a new salt and hashes the
    password using argon2. The password is then stored in the format:

    <algorithm>[,arg=value, ...]$<salt>$<hash>

    The salt and hash are base 64 encoded when they are stored. The salt is
    not encoded until after the password has been hashed
    """
    self.password = ph.hash(password)

  def check_password(self, password):
    """ Checks the given password against the one stored in the database.
    We're assuming the algorithm is always argon2, though the kwargs may change
    """
    try:
      ph.verify(self.password, password)
    except:
      return False

    return True