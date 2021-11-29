from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.fields import DecimalField


class Restaurant(models.Model):

    """Restaurant Model Definition"""

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=140, null=True)
    upjong = models.CharField(max_length=30, null=True)
    rating_average = DecimalField(max_digits=2, decimal_places=2, null=True)
    address = models.CharField(max_length=140, null=True)
    category = models.CharField(max_length=100, null=True)
    rating_count = DecimalField(max_digits=10, decimal_places=2, null=True)
    Latitude = DecimalField(max_digits=13, decimal_places=10, null=True)
    Longtitude = DecimalField(max_digits=13, decimal_places=10, null=True)

    class Meta:
        db_table = "restaurant"
