from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .models import User


class CustomUserAdmin(UserAdmin):
  """ Removes `date_joined` time """

  fieldsets = (
      (None, {"fields": ("username", "password")}),
      (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
      (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser",
                                     "groups", "user_permissions")}),
      (_("Important dates"), {"fields": ("last_login",)}),
    )


admin.site.register(User, CustomUserAdmin)