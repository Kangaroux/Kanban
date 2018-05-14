from django.http import JsonResponse
from django.views import View

from lib import response_codes as http


__all__ = ["BaseAPIView", "http"]


class BaseAPIView(View):
  @classmethod
  def form_error(cls, form, msg=None, code=http.BAD_REQUEST):
    """ Returns a form error response """
    return cls.error({ "fields": form.get_errors() }, msg, code)

  @staticmethod
  def error(data=None, msg=None, code=http.BAD_REQUEST):
    """ Returns an error response as JSON """
    resp = { "status": "error" }

    if msg:
      resp["msg"] = msg

    if data:
      resp = { **resp, **data }

    return JsonResponse(resp, status_code=code)

  @staticmethod
  def ok(data=None, msg=None, code=http.OK):
    """ Returns an OK response """
    resp = { "status": "ok" }

    if msg:
      resp["msg"] = msg

    if data:
      resp = { **resp, **data }

    return JsonResponse(resp, status_code=code)
