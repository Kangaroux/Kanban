from .user import UserAPI
from .auth import AuthAPI
from lib.routing import endpoint, route


urls = route("api", [
  route("auth", [
    endpoint("/", AuthAPI, ["POST"]),
  ]),
  route("user", [
    endpoint("/", UserAPI, ["POST"]),
    endpoint("/<int:user_id>", UserAPI, ["GET", "PUT", "DELETE"]),
  ]),
])
