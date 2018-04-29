from flask import jsonify, make_response
from flask.views import MethodView

from lib.string import snake_case


class BaseEndpoint(MethodView):
  """ Base API view which helps with routing and error handling """

  URL = "myendpoint"
  NAME = None

  @classmethod
  def get_url(cls):
    return cls.URL

  @classmethod
  def get_name(cls):
    return cls.NAME or snake_case(cls.__name__)

  def form_error(self, form, message=None, status_code=400):
    """ Returns a form error response """
    return self.error({ "fields": form.get_errors() }, message, status_code)

  def error(self, data=None, message=None, status_code=400):
    """ Returns an error response as JSON """
    resp = { "status": "error" }

    if message:
      resp["message"] = message

    if data:
      resp = { **resp, **data }

    return make_response(jsonify(resp), status_code)

  def ok(self, message=None):
    """ Returns an OK response """
    resp = { "status": "ok" }

    if message:
      resp["msg"] = message

    return jsonify(resp)