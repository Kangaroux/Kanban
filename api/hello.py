from flask import Blueprint
from flask.views import MethodView


class HelloAPI(MethodView):
  def get(self):
    return "Hello"


bp = Blueprint("hello", __name__, url_prefix="/hello")
bp.add_url_rule("/", view_func=HelloAPI.as_view("hello"))