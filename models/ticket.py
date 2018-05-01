import enum

from config.app import db
from models.base import BaseModel


class Ticket(BaseModel, db.Model):
  class Type(enum.Enum):
    feature = 0
    bug = 1
    chore = 2

  name = db.Column(db.String(100))
  description = db.Column(db.Text())
  type_ = db.Column("type", db.Enum(Type))

  author = db.relationship("User", uselist=False)
  assigned = db.relationship("User")


  def __repr__(self):
    return "<Ticket id=%r name=%r>" % (self.id, self.name)

  @property
  def type(self):
    return self.type_