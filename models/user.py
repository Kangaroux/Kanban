import os
from argon2 import argon2_hash
from base64 import b64decode, b64encode

from models.base import BaseModel
from config.app import db


class User(BaseModel):
  first_name = db.Column(db.String(20))
  last_name = db.Column(db.String(20), nullable=True)

  username = db.Column(db.String(20), unique=True)
  email = db.Column(db.String(100), unique=True)

  password = db.Column(db.String(100))


  def set_password(self, password):
    """ Sets the user's new password. This generates a new salt and hashes the
    password using argon2. The password is then stored in the format:

    <algorithm>[,arg=value, ...]$<salt>$<hash>

    The salt and hash are base 64 encoded when they are stored. The salt is
    not encoded until after the password has been hashed
    """
    t = 256
    buflen = 40
    salt = os.urandom(32)

    self.password = "argon2,t=%d,buflen=%d$%s$%s" % (t, buflen, 
      b64encode(salt).decode("utf-8"),
      b64encode(argon2_hash(password, salt, t=t, buflen=buflen)).decode("utf-8")
    )

  def check_password(self, password):
    """ Checks the given password against the one stored in the database.
    We're assuming the algorithm is always argon2, though the kwargs may change
    """
    parts = self.password.split("$")
    args = parts[0].split(",")[1:]
    kwargs = {}

    # Extract any keyword arguments
    for arg in args:
      k, v = arg.split("=")
      kwargs[k] = int(v)

    # Hash the password with the same args
    hashed = b64encode(
      argon2_hash(password, b64decode(parts[1]), **kwargs)).decode("utf-8")

    return parts[2] == hashed