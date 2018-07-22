from django.db.utils import IntegrityError

from . import TestCase
from user.models import User


class TestUserModel(TestCase):
  def setUp(self):
    self.u = self.create_user()

  def test_serialize(self):
    self.assertEqual(self.u.serialize(), {
      "id": self.u.id,
      "first_name": self.u.first_name,
      "last_name": self.u.last_name,
      "email": self.u.email,
      "date_created": self.u.date_created.isoformat(),
      "date_updated": self.u.date_updated.isoformat(),
    })

  def test_unique_email(self):
    with self.assertRaises(IntegrityError):
      self.create_user()