from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Route
from api.routeapi import RouteApiRequest


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

        if self.is_valid():
            api_request = RouteApiRequest(
                self.validated_data["longitude_start"],
                self.validated_data["latitude_start"],
                self.validated_data["longitude_end"],
                self.validated_data["latitude_end"]
            )

            if api_request.reply_valid:
                route = Route(
                    longitude_start=self.validated_data["longitude_start"],
                    latitude_start=self.validated_data["latitude_start"],
                    longitude_end=self.validated_data["longitude_end"],
                    latitude_end=self.validated_data["latitude_end"],
                    distance=RouteApiRequest.give_distance(
                        api_request.reply, api_request.reply_valid),
                    coordinates_json=RouteApiRequest.give_coordinates(
                        api_request.reply, api_request.reply_valid),
                )

                route.save()
                return route

            else:
                return False

