from django.test import TestCase

from tests import create_user


class TestUserAPI(TestCase):
  def setUp(self):
    self.u = create_user()

  def tearDown(self):
    self.u.delete()

  