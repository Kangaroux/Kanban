from django.db.utils import IntegrityError

from tests import TestCase
from user.models import User


class TestUser(TestCase):
  def setUp(self):
    self.u = self.create_user()

  def tearDown(self):
    self.u.delete()

  def test_serialize(self):
    self.assertEqual(self.u.serialize(), {
      "first_name": self.u.first_name,
      "last_name": self.u.last_name,
      "email": self.u.email,
      "username": self.u.username,
      "date_created": self.u.date_created.isoformat()
    })

  def test_unique_email(self):
    with self.assertRaises(IntegrityError):
      self.create_user()