from django.shortcuts import reverse

from project.models import Board, Column
from tests import TestCase


class TestColumnAPI(TestCase):
  def setUp(self):
    self.u = self.create_user()

  def test_create_column(self):
    self.login(self.u)

    board = self.create_board()

    # Missing fields
    resp = self.client.post(reverse("project:column", args=[board.id]))

    self.assertEqual(resp.status_code, 400),
    self.assertEqual(resp.json()["fields"], { "name": "This field is required." })

    # Success
    resp = self.client.post(reverse("project:column", args=[board.id]), {
        "name": "Test Column"
      })

    column = Column.objects.get(id=resp.json()["column"]["id"])
    board.refresh_from_db()

    self.assertEqual(resp.status_code, 201)
    self.assertEqual(resp.json()["column"], column.serialize())
    self.assertEqual(board.get_columns_ordered(), [column])

  def test_get_single_column(self):
    self.login(self.u)
    board = self.create_board()

    # Nonexistent column
    resp = self.client.get(reverse("project:column", args=[board.id, 12345]))

    self.assertEqual(resp.status_code, 404)
    self.assertEqual(resp.json()["msg"], "Column does not exist.")

    # Success
    column = Column.create_column(name="Test Column", board=board)
    resp = self.client.get(reverse("project:column", args=[board.id, column.id]))

    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()["column"], column.serialize())

  def test_get_columns(self):
    self.login(self.u)
    board = self.create_board()
    columns = [
        Column.create_column(name="Col1", board=board),
        Column.create_column(name="Col2", board=board),
        Column.create_column(name="Col3", board=board),
      ]

    for c in columns:
      board.add_column(c)

    board.save()

    resp = self.client.get(reverse("project:column", args=[board.id]))

    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()["columns"], [ c.serialize() for c in columns ])