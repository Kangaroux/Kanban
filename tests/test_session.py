from django.shortcuts import reverse

from . import TestCase


class TestSessionAPI(TestCase):
  def setUp(self):
    self.u = self.create_user()

  def tearDown(self):
    self.u.delete()

  def test_login(self):
    # Missing fields
    resp = self.client.post(reverse("user:session"))

    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()["msg"], "Some fields are missing or incorrect.")
    self.assertTrue("email" in resp.json()["fields"])
    self.assertTrue("password" in resp.json()["fields"])

    # Bad email
    resp = self.client.post(reverse("user:session"), {
      "email": "bad@email.com",
      "password": "password123"
    })

    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()["msg"], "Email or password is incorrect.")

    # Bad password
    resp = self.client.post(reverse("user:session"), {
      "email": self.u.email,
      "password": "badpassword"
    })

    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()["msg"], "Email or password is incorrect.")

    # Success
    resp = self.client.post(reverse("user:session"), {
      "email": self.u.email,
      "password": self.u.raw_password
    })

    self.assertEqual(resp.status_code, 200)
    self.assertTrue("_auth_user_id" in self.client.session)

  def test_logout(self):
    self.login(self.u)
    self.assertTrue("_auth_user_id" in self.client.session)
    self.client.delete(reverse("user:session"))
    self.assertTrue("_auth_user_id" not in self.client.session)
