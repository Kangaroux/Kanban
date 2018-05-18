import django.contrib.auth.mixins
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
  def error(msg, data=None, status=400):
    resp = {
      "status": "error",
      "msg": msg
    }

    if data:
      resp.update(data)

    return JsonResponse(resp, status=status)

  @staticmethod
  def ok(msg=None, data=None, status=200):
    resp = {
      "status": "ok"
    }

    if msg:
      resp["msg"] = msg

    if data:
      resp.update(data)

    return JsonResponse(resp, status=status)

  @classmethod
  def not_logged_in(cls):
    return cls.error("You must be logged in to do that.", status=401)

  @classmethod
  def lacks_permission(cls):
    return cls.error("You do not have permission to do that.", status=403)


class LoginRequiredMixin(django.contrib.auth.mixins.LoginRequiredMixin):
  def handle_no_permission(self):
    return APIView.not_logged_in()