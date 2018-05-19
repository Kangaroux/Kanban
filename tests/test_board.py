from django.shortcuts import reverse

from project.models import Board
from tests import TestCase


class TestBoardAPI(TestCase):
  def setUp(self):
    self.u = self.create_user()

  def test_login_required(self):
    self.assert_not_logged_in(self.client.get(reverse("project:board")))
    self.assert_not_logged_in(self.client.post(reverse("project:board")))
    self.assert_not_logged_in(self.client.delete(reverse("project:board")))

  def test_create_board(self):
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

    board = Board.objects.get(id=resp.json()["board"]["id"])
    self.assertEqual(resp.status_code, 201)
    self.assertEqual(resp.json()["board"], board.serialize())

  def test_get_single_board(self):
    self.login(self.u)

    # Nonexistent board
    resp = self.client.get(reverse("project:board", args=[12345]))

    self.assertEqual(resp.status_code, 404)
    self.assertEqual(resp.json()["msg"], "Board does not exist.")

    # Success
    board = self.create_board()
    resp = self.client.get(reverse("project:board", args=[board.id]))

    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()["board"], board.serialize())

  def test_get_boards(self):
    self.login(self.u)
    boards = [
        self.create_board(),
        self.create_board(),
        self.create_board(),
      ]
    resp = self.client.get(reverse("project:board"))

    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()["boards"], [ b.serialize() for b in boards ])

  def test_delete_board(self):
    self.login(self.u)

    # Success
    board = self.create_board()
    resp = self.client.delete(reverse("project:board", args=[board.id]))

    self.assertEqual(resp.status_code, 200)

    # No longer exists
    resp = self.client.delete(reverse("project:board", args=[board.id]))

    self.assertEqual(resp.status_code, 404)
    self.assertEqual(resp.json()["msg"], "Board does not exist.")