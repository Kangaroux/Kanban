from config.app import db
from models.base import BaseModel


class Column(BaseModel, db.Model):
  name = db.Column(db.String(20))
  tasks = db.relationship("Task", backref="column")


  def __repr__(self):
    return "<Column id=%r name=%r>" % (self.id, self.name)