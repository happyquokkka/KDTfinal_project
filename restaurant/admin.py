from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from django.db.models import fields
from django.utils.html import mark_safe
from . import models

import csv


@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    """Restaurant Admin Definition"""

    fieldsets = (
        (
            "Basic Infor",
            {
                "fields": ("name", "upjong", "category","rating_count","rating_average", "address","Latitude","Longtitude"),
            },
        ),
    )

    list_display = ("name", "upjong", "category","rating_count","rating_average", "address","Latitude","Longtitude")
