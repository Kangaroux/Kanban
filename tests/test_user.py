from django.shortcuts import reverse
from django.test import TestCase

from tests import create_user
from user.models import User


class TestUserAPI(TestCase):
  def setUp(self):
    self.u = create_user()

  def tearDown(self):
    self.u.delete()

  def test_get_user(self):
    # Test invalid user
    resp = self.client.get(reverse("user:user", args=[12345]))

    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()["msg"], "User does not exist.")

    # Test good user
    resp = self.client.get(reverse("user:user", args=[self.u.id]))

    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()["user"], self.u.serialize())

  def test_create_user(self):
    # Missing parameters
    resp = self.client.post(reverse("user:user"))

    self.assertEqual(resp.status_code, 400)
    self.assertEqual(set(resp.json()["fields"].keys()),
      set(["first_name", "email", "username", "password", "confirm_password"]))

    # Mismatched passwords
    resp = self.client.post(reverse("user:user"), {
        "first_name": "First",
        "last_name": "Last",
        "email": "first@last.com",
        "username": "firstlast",
        "password": "qweasd123",
        "confirm_password": "asdlkasjdlkajdl",
      })

    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()["fields"], {
      "confirm_password": "Passwords must match"
    })

    # Good create user
    resp = self.client.post(reverse("user:user"), {
        "first_name": "First",
        "last_name": "Last",
        "email": "first@last.com",
        "username": "firstlast",
        "password": "qweasd123",
        "confirm_password": "qweasd123",
      })


    user = User.objects.get(id=resp.json()["user_id"])

    self.assertEqual(resp.status_code, 200)
    self.assertEqual(user.serialize(exclude=["date_created"]), {
      "first_name": "First",
      "last_name": "Last",
      "email": "first@last.com",
      "username": "firstlast"
    })
    self.assertTrue(user.check_password("qweasd123"))

  def test_delete_nonexistent_user(self):
    # Delete nonexistent user
    resp = self.client.delete(reverse("user:user", args=[12345]))

    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()["msg"], "User does not exist.")

  def test_delete_user(self):
    # Delete user
    self.client.login(username=self.u.email, password=self.u.raw_password)

    resp = self.client.delete(reverse("user:user", args=[self.u.id]))
    self.assertEqual(resp.status_code, 200)
    self.assertTrue("_auth_user_id" not in self.client.session)
