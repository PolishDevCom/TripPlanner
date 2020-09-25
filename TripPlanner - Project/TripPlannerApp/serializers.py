from rest_framework import serializers
from TripPlannerApp.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            "id",
            "name",
            "budget",
            "no_of_days",
            "created_at",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True}
        }
