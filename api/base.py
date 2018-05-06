from flask import jsonify, make_response
from flask.views import MethodView

from lib.response import ErrorResponse
from lib.string import snake_case


class BaseEndpoint(MethodView):
  """ Base API view which helps with routing and error handling """

  def dispatch_request(self, *args, **kwargs):
    """ Allow for views to raise an ErrorResponse exception which is caught by
    this and then returned. This makes it easy to create methods like 
    `get_object_or_404()` which raise an error response if the object doesn't
    exist. The caller doesn't have to worry about handling the error response
    as it's caught here
    """
    try:
      return super().dispatch_request(*args, **kwargs)
    except ErrorResponse as e:
      return self.error(msg=e.msg, data=e.data, code=e.code)

  @classmethod
  def form_error(cls, form, msg=None, code=400):
    """ Returns a form error response """
    return cls.error({ "fields": form.get_errors() }, msg, code)

  @staticmethod
  def error(data=None, msg=None, code=400):
    """ Returns an error response as JSON """
    resp = { "status": "error" }

    if msg:
      resp["msg"] = msg

    if data:
      resp = { **resp, **data }

    return make_response(jsonify(resp), code)

  @staticmethod
  def ok(data=None, msg=None, code=200):
    """ Returns an OK response """
    resp = { "status": "ok" }

    if msg:
      resp["msg"] = msg

    if data:
      resp = { **resp, **data }

    return make_response(jsonify(resp), code)
