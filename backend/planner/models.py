from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Trip(models.Model):
    name = models.CharField(max_length=255)
    budget = models.DecimalField(
        decimal_places=2, max_digits=8, validators=[MinValueValidator(1)]
    )
    no_of_days = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
