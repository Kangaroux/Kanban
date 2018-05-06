from flaskrouting import path, page, var

from .user import UserAPI
from .auth import AuthAPI


routes = (
  path("api", [
    path("auth", [
      page("", AuthAPI, methods=["POST"]),
    ]),
    path("user", [
      page("", UserAPI, methods=["POST"]),
      var("<int:user_id>", [
        page("", UserAPI, methods=["GET", "PUT", "DELETE"])
      ]),
    ])
  ])
)