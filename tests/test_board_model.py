from django.db.utils import IntegrityError

from project.models import Board, Column
from tests import TestCase


class TestBoardModel(TestCase):
  def setUp(self):
    self.u = self.create_user()

  def create_board(self):
    return Board.create_board(
      name="Test board",
      description="My test board",
      created_by=self.u,
      owner=self.u,
    )

  def test_serialize(self):
    board = self.create_board()
    board.column_order = [1, 2, 3]

    self.assertEqual(board.serialize(), {
      "id": board.id,
      "name": board.name,
      "description": board.description,
      "owner": self.u.id,
      "created_by": self.u.id,
      "column_order": [1, 2, 3],
      "date_created": board.date_created.isoformat(),
      "date_updated": board.date_updated.isoformat(),
    })

  def test_adding_columns(self):
    board = self.create_board()
    columns = [
        Column.objects.create(name="Col1", board=board),
        Column.objects.create(name="Col2", board=board),
        Column.objects.create(name="Col3", board=board),
        Column.objects.create(name="Col4", board=board),
      ]

    self.assertEqual(board.column_order, [])

    board.add_column(columns[0])
    self.assertEqual(board.column_order,
      [ columns[0].id ])

    board.add_column(columns[1], index=0)
    self.assertEqual(board.column_order,
      [ columns[1].id, columns[0].id ])

    board.add_column(columns[2], index=1)
    self.assertEqual(board.column_order,
      [ columns[1].id, columns[2].id, columns[0].id ])

    board.add_column(columns[3])
    self.assertEqual(board.column_order,
      [ columns[1].id, columns[2].id, columns[0].id, columns[3].id ])

  def test_ordering_columns(self):
    board = self.create_board()
    columns = [
        Column.objects.create(name="Col1", board=board),
        Column.objects.create(name="Col2", board=board),
        Column.objects.create(name="Col3", board=board),
        Column.objects.create(name="Col4", board=board),
      ]

    board.add_column(columns[0])
    board.add_column(columns[2])
    board.add_column(columns[3])
    board.add_column(columns[1])
    board.save()

    cols = Column.objects.filter(board=board)
