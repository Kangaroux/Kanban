from datetime import datetime

from config.app import db


class BaseModel:
  """ Base model class which includes some common fields """

  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, onupdate=datetime.now, nullable=True)