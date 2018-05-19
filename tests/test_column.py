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

    column = Column.objects.get(id=resp.json()["column_id"])
    board.refresh_from_db()

    self.assertEqual(resp.status_code, 201)
    self.assertEqual(column.board, board)
    self.assertEqual(board.get_columns_ordered(), [column])