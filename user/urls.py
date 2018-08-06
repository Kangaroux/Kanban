from django.urls import path

from . import api


app_name = "user"

urlpatterns = [
  path("session/", api.SessionAPI.as_view(), name="session"),
  path("users/", api.UserAPI.as_view(), name="user"),
  path("users/<int:user_id>/", api.UserAPI.as_view(), name="user"),
]