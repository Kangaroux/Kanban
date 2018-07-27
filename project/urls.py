from django.urls import include, path

from . import api


app_name = "project"

urlpatterns = [
  path("projects/", api.ProjectAPI.as_view(), name="project"),
  path("projects/<int:project_id>", api.ProjectAPI.as_view(), name="project"),

  path("boards/", api.BoardAPI.as_view(), name="board"),
  path("boards/<int:board_id>/", include([
    path("", api.BoardAPI.as_view(), name="board"),
    path("columns/", api.ColumnAPI.as_view(), name="column"),
    path("columns/<int:column_id>/", api.ColumnAPI.as_view(), name="column"),
  ])),
]