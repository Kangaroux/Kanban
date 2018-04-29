from flask import jsonify, make_response, request

from api.base import BaseEndpoint
from config.app import db
from forms.user import CreateUserForm
from models.user import User


class CreateUser(BaseEndpoint):
  URL = "create"

  def get(self):
    return "Hi"

  def post(self):
    form = CreateUserForm()

    if not form.validate():
      return make_response(jsonify(form.errors), 400)

    data = form.data
    u = User(
      first_name=data.get("first_name"),
      last_name=data.get("last_name"),
      email=data.get("email"),
      username=data.get("username")
    )

    u.set_password(data.get("password"))
    db.session.add(u)
    db.session.commit()

    return jsonify({ "status": "ok" })