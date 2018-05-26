from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .models import User


class CustomUserAdmin(UserAdmin):
  """ Removes the date_joined and username fields """

  fieldsets = (
      (None, {"fields": ("password",)}),
      (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
      (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser",
                                     "groups", "user_permissions")}),
      (_("Important dates"), {"fields": ("last_login",)}),
    )

  list_display = ("email", "first_name", "last_name", "is_staff")
  search_fields = ("first_name", "last_name", "email")
  ordering = ("email",)


admin.site.register(User, CustomUserAdmin)