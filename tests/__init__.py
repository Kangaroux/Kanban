import django.test

from user.models import User


class TestCase(django.test.TransactionTestCase):
  def create_user(self):
    u = User.objects.create_user(
      first_name="John",
      last_name="Smith",
      username="jsmith",
      email="test@test.com",
      password="password123"
    )

    u.raw_password = "password123"

    return u

  def assert_not_logged_in(self, resp):
    self.assertEqual(resp.status_code, 401)
    self.assertEqual(resp.json()["msg"], "You must be logged in to do that.")

  def assert_bad_perms(self, resp):
    self.assertEqual(resp.status_code, 403)
    self.assertEqual(resp.json()["msg"], "You do not have permission to do that.")

  def login(self, user, password=None):
    if password is None:
      password = user.raw_password

    return self.client.login(username=user.email, password=password)