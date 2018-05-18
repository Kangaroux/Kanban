from django.shortcuts import reverse

from tests import TestCase
from user.models import User


class TestUserAPI(TestCase):
  def setUp(self):
    self.u = self.create_user()

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

    # Success
    resp = self.client.post(reverse("user:user"), {
        "first_name": "First",
        "last_name": "Last",
        "email": "first@last.com",
        "username": "firstlast",
        "password": "qweasd123",
        "confirm_password": "qweasd123",
      })

    user = User.objects.get(id=resp.json()["user_id"])

    self.assertEqual(resp.status_code, 201)
    self.assertTrue(user.check_password("qweasd123"))
    self.assertEqual(user.serialize(exclude=["date_created"]), {
      "id": user.id,
      "first_name": "First",
      "last_name": "Last",
      "email": "first@last.com",
      "username": "firstlast"
    })

  def test_delete_user_invalid(self):
    # Not logged in
    self.assert_not_logged_in(self.client.delete(reverse("user:user", args=[12345])))

    # Delete nonexistent user
    self.login(self.u)
    resp = self.client.delete(reverse("user:user", args=[12345]))

    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()["msg"], "User does not exist.")

  def test_delete_user(self):
    self.login(self.u)
    resp = self.client.delete(reverse("user:user", args=[self.u.id]))

    self.assertEqual(resp.status_code, 200)
    self.assertTrue("_auth_user_id" not in self.client.session)
