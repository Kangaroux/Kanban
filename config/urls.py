from django.contrib import admin
from django.urls import include, path, re_path

import app.views


urlpatterns = [
  path("admin/", admin.site.urls),
  path("api/", include("user.urls")),
  path("api/", include("project.urls")),
  path("", app.views.main),
]