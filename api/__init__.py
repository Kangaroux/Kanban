from flask import Blueprint

from . import user


bp = Blueprint("api", __name__, url_prefix="/api")

def add_endpoint(prefix, endpoint):
  bp.add_url_rule("%s/%s" % (prefix, endpoint.get_url()), 
    view_func=endpoint.as_view(endpoint.get_name()))

# /api/user/
add_endpoint("/user", user.CreateUser)