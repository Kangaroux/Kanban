from django.urls import path

from . import api


app_name = "user"

urlpatterns = [
  path("session/", api.SessionAPI.as_view(), name="session"),
  path("user/", api.UserAPI.as_view(), name="user"),
  path("user/<int:user_id>", api.UserAPI.as_view(), name="user"),
]