from flask import Blueprint, jsonify, make_response, request

from api.base import BaseEndpoint
from config.app import db
from forms.user import CreateUserForm
from models.user import User


class UserAPI(BaseEndpoint):
  def get(self, user_id):
    """ Returns a user's info """
    u = User.query.get(user_id)

    if not u:
      return self.error(msg="User does not exist.", code=404)

    return self.ok(data={
      "user": {
        "id": u.id,
        "first_name": u.first_name,
        "last_name": u.last_name,
        "email": u.email,
        "username": u.username,
        "joined": u.created_at.isoformat()
      }
    })

  def post(self):
    """ Adds a new user """
    form = CreateUserForm()

    if not form.validate():
      return self.form_error(form)

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

    return self.ok()

  def put(self, user_id):
    """ Updates an existing user """
    pass

  def delete(self, user_id):
    """ Deletes an existing user """
    pass


view = UserAPI.as_view("user")
blueprint = Blueprint("api", __name__, url_prefix="/user")

blueprint.add_url_rule("/", view_func=view, methods=["POST"])
blueprint.add_url_rule("/<int:user_id>", view_func=view,
  methods=["GET", "PUT", "DELETE"])