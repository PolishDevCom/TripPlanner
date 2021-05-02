"""Stores models"""

from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models


class Route(models.Model):
    """
    Represents route with list of coordinantes.

    Attributes:
        id (int): Route identifier.
        longitude_start (float): Start route's longitude.
        latitude_start (float): Start route's latitude.
        longitude_end (float): End route's longitude.
        latitude_end (float): End route's latitude.
        distance (float): Route's distance.
        coordinates_json (str): List of coordinates of the route.
        created_at (datetime): Date and time of creation.
    """

    id = models.AutoField(primary_key=True)
    longitude_start = models.DecimalField(decimal_places=9, max_digits=12)
    latitude_start = models.DecimalField(decimal_places=9, max_digits=12)
    longitude_end = models.DecimalField(decimal_places=9, max_digits=12)
    latitude_end = models.DecimalField(decimal_places=9, max_digits=12)

    distance = models.DecimalField(decimal_places=4, max_digits=16)
    coordinates_json = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


class Places(models.Model):
    """
    Represents location with queried venues.

    Attributes:
        longitude (float): The longitude of the location.
        latitude (float): The latitude of the location.
        radius (int): The maximum distance of a venue from the location.
        query (str): Query about the types of venues.
        venues (list): List of detailed venues.
    """

    longitude = models.DecimalField(decimal_places=9, max_digits=12)
    latitude = models.DecimalField(decimal_places=9, max_digits=12)
    radius = models.IntegerField()
    query = models.CharField(max_length=56)
    venues = ArrayField(JSONField())


class Venue(models.Model):
    """
    Represents detailed venue.

    Attributes:
        venue_id (str): Venue's id.
        name (str): Venue's name.
        address (list): Venue'a address.
        logitude (float): Venue's longitude.
        latitude (float): Venue's latitude.
        categories (list): Venue's categories.
    """

    venue_id = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=64)
    address = models.TextField()
    longitude = models.DecimalField(decimal_places=9, max_digits=12)
    latitude = models.DecimalField(decimal_places=9, max_digits=12)
    categories = models.TextField()
