from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.users)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets

    list_filter = UserAdmin.list_filter

    list_display = (
        "id",
        "email",
    )
