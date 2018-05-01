from config.app import db
from models.base import BaseModel


class Project(BaseModel, db.Model):
  boards = db.relationship("Board", backref="project")
  name = db.Column(db.String(50))
  owner = db.relationship("User", uselist=False)


  def __repr__(self):
    return "<Project id=%r name=%r>" % (self.id, self.name)