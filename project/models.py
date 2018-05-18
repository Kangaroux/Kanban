from django.db import models

from lib.models import BaseModel, ListField


class Board(BaseModel):  
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=200, blank=True)
  created_by = models.ForeignKey("user.User", on_delete=models.CASCADE)
  owner = models.ForeignKey("user.User", related_name="owner", on_delete=models.CASCADE)

  # JSON array of column ids so they can be ordered
  column_order = ListField()

  def __repr__(self):
    return "<Board id=%r name=%r>" % (self.id, self.name)

  def get_columns_ordered(self):
    """ Returns the columns for this board in the order that they are defined
    in the `column_order` field
    """
    cols = Column.objects.filter(board=self)
    cols = { c.id : c for c in cols }

    return [ cols[i] for i in column_order ]

  def add_column(self, col, index=None):
    """ Adds a column to the board at the specified index. If `index` is None,
    the column is inserted last. This updates the new column but not the board
    """
    if index is None:
      self.column_order.append(col.id)
    elif index < 0 or index > len(self.column_order):
      raise ValueError("Cannot insert column at out of range index %d" % index)
    else:
      self.column_order.insert(index, col.id)

    col.board = self
    col.save()


class Column(BaseModel):
  name = models.CharField(max_length=20)
  board = models.ForeignKey("Board", on_delete=models.CASCADE)

  # JSON array of task ids so they can be ordered
  task_order = ListField()

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
  column = models.ForeignKey("Column", on_delete=models.PROTECT)

  author = models.ForeignKey("user.User", related_name="author", on_delete=models.CASCADE)
  assigned_users = models.ManyToManyField("user.User")

  def __repr__(self):
    return "<Task id=%r name=%r>" % (self.id, self.name)
