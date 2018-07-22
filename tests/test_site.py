import logging

from django.shortcuts import reverse
from django.test import Client

from tests import TestCase


class TestSite(TestCase):
  def test_500_error(self):
    # Temporarily disable logging because the dummy view raises an exception
    # and we don't want to clutter the test output
    logging.disable(logging.CRITICAL)
    resp = self.client.get(reverse("dummy_500"))
    logging.disable(logging.NOTSET)

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