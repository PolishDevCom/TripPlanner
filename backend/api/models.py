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
