from flask import jsonify, make_response, request

from api.base import BaseEndpoint
from forms.user import CreateUserForm


class CreateUser(BaseEndpoint):
  URL = "create"

  def get(self):
    return "Hi"

  def post(self):
    form = CreateUserForm()

    if not form.validate():
      return make_response(jsonify(form.errors), 400)

    return jsonify({ "status": "ok" })