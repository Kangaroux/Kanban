from django.db.utils import IntegrityError

from tests import TestCase
from project.models import Board


class TestBoardModel(TestCase):
  def setUp(self):
    self.u = self.create_user()

  def tearDown(self):
    self.u.delete()

  def test_serialize(self):
    board = Board.objects.create(
        name="Test board",
        description="My test board",
        created_by=self.u,
        owner=self.u
      )

    # self.assertEqual(self.u.serialize(), {
    #   "first_name": self.u.first_name,
    #   "last_name": self.u.last_name,
    #   "email": self.u.email,
    #   "username": self.u.username,
    #   "date_created": self.u.date_created.isoformat()
    # })
