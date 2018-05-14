from django.http import JsonResponse
from django.views import View


class APIView(View):
  @classmethod
  def form_error(cls, fields, msg=None):
    return cls.error(msg, { "fields": fields })

  @staticmethod
  def error(msg, data=None, code=400):
    resp = {
      "status": "error",
      "msg": msg
    }

    if data:
      resp.update(data)

    return JsonResponse(resp, status_code=400)

  @staticmethod
  def ok(msg=None, data=None, code=200):
    resp = {
      "status": "ok"
    }

    if msg:
      resp["msg"] = msg

    if data:
      resp.update(data)

    return JsonResponse(resp, status_code=code)