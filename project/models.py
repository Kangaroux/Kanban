from django.db import models

from lib.models import BaseModel


class Board(BaseModel):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=200, null=True)
  created_by = models.ForeignKey("user.User", on_delete=models.CASCADE)
  owner = models.ForeignKey("user.User", related_name="owner", on_delete=models.CASCADE)

  def __repr__(self):
    return "<Board id=%r name=%r>" % (self.id, self.name)


class Column(BaseModel):
  name = models.CharField(max_length=20)
  board = models.ForeignKey("Board", on_delete=models.CASCADE)
  tasks = models.ManyToManyField("Task")

  def __repr__(self):
    return "<Column id=%r name=%r>" % (self.id, self.name)


class Task(BaseModel):
  TYPE_FEATURE = "F"
  TYPE_BUG = "B"
  TYPE_CHORE = "C"

  TYPES = (
    (TYPE_FEATURE, "Feature"),
    (TYPE_BUG, "Bug"),
    (TYPE_CHORE, "Chore"),
  )

  name = models.CharField(max_length=100)
  description = models.TextField()
  type = models.CharField(max_length=1, choices=TYPES)

  # The next task in the list
  next_task = models.ForeignKey("self", null=True,  on_delete=models.PROTECT)

  author = models.ForeignKey("user.User", related_name="author", on_delete=models.CASCADE)
  assigned_users = models.ManyToManyField("user.User")

  def __repr__(self):
    return "<Task id=%r name=%r>" % (self.id, self.name)
