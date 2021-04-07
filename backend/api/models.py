from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    longitude_start = models.DecimalField(decimal_places=9, max_digits=12)
    latitude_start = models.DecimalField(decimal_places=9, max_digits=12)
    longitude_end = models.DecimalField(decimal_places=9, max_digits=12)
    latitude_end = models.DecimalField(decimal_places=9, max_digits=12)

    distance = models.DecimalField(decimal_places=4, max_digits=16)
    coordinates_json = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


class Venue(models.Model):
    venue_id = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=64)
    address = models.TextField()
    longitude = models.DecimalField(decimal_places=9, max_digits=12)
    latitude = models.DecimalField(decimal_places=9, max_digits=12)
    rating = models.DecimalField(
        decimal_places=1, max_digits=3, null=True, blank=True
    )
    photo = models.TextField(null=True, blank=True)
    categories = models.TextField()
    similar_venues = ArrayField(JSONField(), null=True, blank=True)

    def __str__(self):
        return self.name + " id:" + self.venue_id
