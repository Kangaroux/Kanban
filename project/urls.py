from django.urls import include, path

from . import api


app_name = "project"

urlpatterns = [
  path("boards/", api.BoardAPI.as_view(), name="board"),
  path("boards/<int:board_id>/", include([
    path("", api.BoardAPI.as_view(), name="board"),
    path("columns/", api.ColumnAPI.as_view(), name="column")
  ])),
]