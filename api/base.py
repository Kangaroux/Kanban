from flask.views import MethodView

from lib.string import snake_case


class BaseEndpoint(MethodView):
  """ Base API view which helps with routing and error handling """

  URL = "myendpoint"
  NAME = None

  @classmethod
  def get_url(cls):
    return cls.URL

  @classmethod
  def get_name(cls):
    return cls.NAME or snake_case(cls.__name__)
