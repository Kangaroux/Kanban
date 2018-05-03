from flask import jsonify, make_response
from flask.views import MethodView

from lib.string import snake_case


class BaseEndpoint(MethodView):
  """ Base API view which helps with routing and error handling """

  def form_error(self, form, msg=None, code=400):
    """ Returns a form error response """
    return self.error({ "fields": form.get_errors() }, msg, code)

  def error(self, data=None, msg=None, code=400):
    """ Returns an error response as JSON """
    resp = { "status": "error" }

    if msg:
      resp["msg"] = msg

    if data:
      resp = { **resp, **data }

    return make_response(jsonify(resp), code)

  def ok(self, data=None, msg=None):
    """ Returns an OK response """
    resp = { "status": "ok" }

    if msg:
      resp["msg"] = msg

    if data:
      resp = { **resp, **data }

    return jsonify(resp)