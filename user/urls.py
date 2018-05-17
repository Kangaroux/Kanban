from django.urls import path

from . import api


app_name = "user"

urlpatterns = [
  path("auth/", api.AuthAPI.as_view(), name="auth"),
  path("user/", api.UserAPI.as_view(), name="user")
]