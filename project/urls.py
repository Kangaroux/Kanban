from django.urls import path

from . import api


app_name = "project"

urlpatterns = [
  path("board/", api.BoardAPI.as_view(), name="board"),
  path("board/<int:board_id>/", api.BoardAPI.as_view(), name="board"),
]