from flaskrouting import path, page, var

from .auth import routes as auth_routes
from .user import routes as user_routes


routes = (
  path("api", [
    path("auth", auth_routes),
    path("user", user_routes),
  ])
)