from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from django.db.models import fields
from django.utils.html import mark_safe
from . import models


@admin.register(models.Sights)
class SightsAdmin(admin.ModelAdmin):

    """Sights Admin Definition"""

    fieldsets = (
        (
            "Basic Infor",
            {
                "fields": ("name", "address"),
            },
        ),
    )

    list_display = ("name", "address")

    list_filter = ("name", "address")
