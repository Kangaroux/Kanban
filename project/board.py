from config.app import db
from models.base import BaseModel


class Board(BaseModel, db.Model):
  columns = db.relationship("Column", backref="board")
  name = db.Column(db.String(50))
  owner = db.relationship("User", uselist=False)


  def __repr__(self):
    return "<Board id=%r name=%r>" % (self.id, self.name)