from django.db import models
from django.db.models.fields import DecimalField


class Sights(models.Model):

    """Sights Model Definition"""

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    Latitude = DecimalField(max_digits=13, decimal_places=10, null=True)
    Longitude = DecimalField(max_digits=13, decimal_places=10, null=True)

    class Meta:
        db_table = "sights"
