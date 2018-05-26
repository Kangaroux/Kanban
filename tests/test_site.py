from django.shortcuts import reverse
from django.test import Client

from tests import TestCase


class TestSite(TestCase):
  def test_500_error(self):
    resp = self.client.get(reverse("dummy_500"))

    self.assertEqual(resp.status_code, 500)
    self.assertEqual(resp.json(), {
      "status": "error",
      "msg": "An unexpected error occurred."
    })

  def test_missing_csrf(self):
    # Using a client not configured for CSRF
    csrf_client = Client(enforce_csrf_checks=True)
    resp = csrf_client.post(reverse("dummy_csrf"))

    self.assertEqual(resp.status_code, 403)
    self.assertEqual(resp.json(), {
      "status": "error",
      "msg": "CSRF token is missing or invalid."
    })

    # Success
    resp = self.client.post(reverse("dummy_csrf"))

    self.assertEqual(resp.status_code, 200)