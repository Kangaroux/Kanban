from functools import wraps

from flask import request, session

from lib import response_codes as http
from lib.response import ErrorResponse


def login(user):
  session["user_id"] = user.id

def logout():
  session.clear()

def login_required(methods=None):
  """ Decorator which is applied to a View class. Accepts an optional list of
  HTTP methods to only check against (by default it checks all of them)
  """
  if methods is None:
    methods = ["get", "post", "put", "patch", "delete"]

  def decorator(cls):
    """ Decorates each HTTP method with a wrapper that checks if the user is
    logged in, and if they aren't it raises an ErrorResponse
    """
    for m in methods:
      m = m.lower()
      func = getattr(cls, m, None)

      if func:
        @wraps(func)
        def wrapper(*args, **kwargs):
          if "user_id" not in session and request.method.upper() in methods:
            raise ErrorResponse(msg="You must be logged in to perform this action.",
              code=http.NO_AUTH)
          else:
            return func(*args, **kwargs)
        
        setattr(cls, m, wrapper)
  
    return cls
  return decorator