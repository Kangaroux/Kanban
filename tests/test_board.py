from django.shortcuts import reverse

from tests import TestCase
from project.models import Board


class TestBoardAPI(TestCase):
  def setUp(self):
    self.u = self.create_user()

  def tearDown(self):
    self.u.delete()

  def test_create_board(self):
    # Not logged in
    self.assert_not_logged_in(self.client.post(reverse("project:board")))
    self.login(self.u)

    # Missing field
    resp = self.client.post(reverse("project:board"))

    self.assertEqual(resp.status_code, 400)
    self.assertTrue("name" in resp.json()["fields"])

    # Success
    resp = self.client.post(reverse("project:board"), {
        "name": "Test board",
        "description": "This is a test board.",
      })

    board = Board.objects.get(id=resp.json()["board_id"])
    self.assertEqual(resp.status_code, 201)
    self.assertEqual(board.serialize(exclude=["date_created", "date_updated"]), {
        "id": board.id,
        "name": "Test board",
        "description": "This is a test board.",
        "column_order": [],
        "owner": self.u.id,
        "created_by": self.u.id,
      })