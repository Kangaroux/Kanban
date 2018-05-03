from config.app import db
from models.base import BaseModel


class Board(BaseModel, db.Model):
  name = db.Column(db.String(20))
  tasks = db.relationship("Task", backref="board")


  def __repr__(self):
    return "<Board id=%r name=%r>" % (self.id, self.name)