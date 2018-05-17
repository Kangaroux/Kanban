from django.http import JsonResponse
from django.views import View


class APIView(View):
  @classmethod
  def form_error(cls, form, msg=None):
    if not msg:
      msg = "Some fields are missing or incorrect."

    return cls.error(msg, {
      "fields": { k:v[0] for k, v in form.errors.items() }
    })

  @staticmethod
  def error(msg, data=None, code=400):
    resp = {
      "status": "error",
      "msg": msg
    }

    if data:
      resp.update(data)

    return JsonResponse(resp, status=400)

  @staticmethod
  def ok(msg=None, data=None, code=200):
    resp = {
      "status": "ok"
    }

    if msg:
      resp["msg"] = msg

    if data:
      resp.update(data)

    return JsonResponse(resp, status=code)