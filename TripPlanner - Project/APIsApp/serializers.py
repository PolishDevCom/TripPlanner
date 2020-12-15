from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Route
from .routeapi import RouteApiRequest


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = [
            "id",
            "longitude_start",
            "latitude_start",
            "longitude_end",
            "latitude_end",
            "distance",
            "coordinates_json",
            "created_at",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "coordinates_json": {"read_only": True},
            "distance": {"read_only": True}
        }

    def create(self, validated_data):
        respond_from_api = RouteApiRequest(
            self.validated_data["longitude_start"],
            self.validated_data["latitude_start"],
            self.validated_data["longitude_end"],
            self.validated_data["latitude_end"]
        )

        route = Route(
            longitude_start=self.validated_data["longitude_start"],
            latitude_start=self.validated_data["latitude_start"],
            longitude_end=self.validated_data["longitude_end"],
            latitude_end=self.validated_data["latitude_end"],
            distance=respond_from_api.give_distance(),
            coordinates_json=respond_from_api.give_coordinates(),
        )

        route.save()

        return route
