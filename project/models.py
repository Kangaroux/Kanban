from django.db import models


class Board(models.Model):
  name = models.CharField(max_length=50)
  owner = models.ForeignKey("user.User", on_delete=models.CASCADE)

  def __repr__(self):
    return "<Board id=%r name=%r>" % (self.id, self.name)


class Column(models.Model):
  name = models.CharField(max_length=20)
  board = models.ForeignKey("Board", on_delete=models.CASCADE)

  def __repr__(self):
    return "<Column id=%r name=%r>" % (self.id, self.name)


class Task(models.Model):
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

  author = models.ForeignKey("user.User", related_name="author", on_delete=models.CASCADE)
  assigned = models.ManyToManyField("user.User")

  def __repr__(self):
    return "<Task id=%r name=%r>" % (self.id, self.name)