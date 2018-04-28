from flask import request
from flask.views import MethodView


class CreateUser(MethodView):
  def post(self):