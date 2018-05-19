import django.contrib.auth.mixins
from django.http import JsonResponse
from django.views import View


class APIError(Exception):
  def __init__(self, msg, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.msg = msg

  def as_json(self):
    return APIView.error(self.msg, status=404)


class MissingError(APIError):
  pass


class LoginRequiredMixin(django.contrib.auth.mixins.LoginRequiredMixin):
  def handle_no_permission(self):
    return APIView.not_logged_in()


class APIView(View):
  """ Base API view which includes some common methods for returning responses
  and checking authorization
  """

  def dispatch(self, *args, **kwargs):
    try:
      return super().dispatch(*args, **kwargs)
    except APIError as e:
      return e.as_json()

  @staticmethod
  def get_or_404(model, pk, msg=None):
    """ Returns the matching board instance or raises a 404 """
    try:
      return model.objects.get(pk=pk)
    except model.DoesNotExist:
      if msg is None:
        msg = "%s does not exist." % model.__name__

      raise MissingError(msg)

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
  def ok(data=None, msg=None, status=200):
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