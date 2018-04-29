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
      "user": u.serialize(exclude=["updated"])
    })

  def post(self):
    """ Adds a new user """
    form = CreateUserForm()

    if not form.validate():
      return self.form_error(form)

    u = User()
    form.populate_obj(u, exclude=["confirm_password", "password"])
    u.set_password(form.data["password"])

    db.session.add(u)
    db.session.commit()

    return self.ok()

  def put(self, user_id):
    """ Updates an existing user """
    u = User.query.get(user_id)

    if not u:
      return self.error(msg="User does not exist.", code=404)

    return self.ok(data={
      "user": {

      }
    })

  def delete(self, user_id):
    """ Deletes an existing user """
    u = User.query.get(user_id)

    if not u:
      return self.error(msg="User does not exist.", code=404)

    db.session.delete(u)
    db.session.commit()

    return self.ok()


view = UserAPI.as_view("user")
blueprint = Blueprint("api", __name__, url_prefix="/user")

blueprint.add_url_rule("/", view_func=view, methods=["POST"])
blueprint.add_url_rule("/<int:user_id>", view_func=view,
  methods=["GET", "PUT", "DELETE"])