from django.shortcuts import reverse
from django.test import TestCase

from tests import create_user


class TestAuthAPI(TestCase):
  def setUp(self):
    self.u = create_user()

  def tearDown(self):
    self.u.delete()

  def test_login(self):
    # Bad email
    resp = self.client.post(reverse("user:auth"), {
      "email": "bad@email",
      "password": "password123"
    })

    self.assertEqual(resp.status_code, 400)

    # Bad password
    resp = self.client.post(reverse("user:auth"), {
      "email": self.u.email,
      "password": "badpassword"
    })

    self.assertEqual(resp.status_code, 400)

    # Good login
    resp = self.client.post(reverse("user:auth"), {
      "email": self.u.email,
      "password": self.u.raw_password
    })

    self.assertEqual(resp.status_code, 200)
    self.assertTrue("_auth_user_id" in self.client.session)

  def test_logout(self):
    self.client.login(username=self.u.email, password=self.u.raw_password)
    self.assertTrue("_auth_user_id" in self.client.session)
    self.client.delete(reverse("user:auth"))
    self.assertTrue("_auth_user_id" not in self.client.session)
