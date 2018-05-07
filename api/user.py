from flask import session
from flaskrouting import page, var

from api.base import *
from config.app import db
from forms.user import CreateUserForm
from lib.auth import login_required
from models.user import User


@login_required(["DELETE"])
class UserAPI(BaseEndpoint):
  def get(self, user_id):
    """ Returns a user's info """
    u = User.get_or_404(user_id)

    return self.ok(data={ "user": u.serialize(exclude=["updated"]) })

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

    return self.ok(data={ "user_id": u.id })

  # def patch(self, user_id):
  #   """ Updates an existing user """
  #   u = User.get_or_404(user_id)

  #   return self.ok(data={ "user": u.serialize(exclude=["updated"]) })

  def delete(self, user_id):
    """ Deletes an existing user """
    u = User.get_or_404(user_id)
    delete_self = session["user_id"] == u.id

    db.session.delete(u)
    db.session.commit()

    return self.ok()


routes = [
  page("", UserAPI, methods=["POST"]),
  var("<int:user_id>", [
    page("", UserAPI, methods=["GET", "DELETE"])
  ]),
]