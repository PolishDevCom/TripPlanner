from api.models import Places, Route
from api.placeapi import PlacesApiRequest
from api.routeapi import RouteApiRequest
from rest_framework import serializers


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
            "distance": {"read_only": True},
        }

    def create(self, validated_data):

        if self.is_valid():
            api_request = RouteApiRequest(
                self.validated_data["longitude_start"],
                self.validated_data["latitude_start"],
                self.validated_data["longitude_end"],
                self.validated_data["latitude_end"],
            )

            if api_request.reply_valid:
                route = Route(
                    longitude_start=self.validated_data["longitude_start"],
                    latitude_start=self.validated_data["latitude_start"],
                    longitude_end=self.validated_data["longitude_end"],
                    latitude_end=self.validated_data["latitude_end"],
                    distance=RouteApiRequest.give_distance(
                        api_request.reply, api_request.reply_valid
                    ),
                    coordinates_json=RouteApiRequest.give_coordinates(
                        api_request.reply, api_request.reply_valid
                    ),
                )

                route.save()
                return route

            else:
                return False


class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = [
            "latitude",
            "longitude",
            "radius",
            "query",
            "limit",
            "venues",
        ]
        extra_kwargs = {"venues": {"read_only": True}}

    def create(self, validated_data):
        if self.is_valid():
            api_request = PlacesApiRequest(
                self.validated_data["latitude"],
                self.validated_data["longitude"],
                self.validated_data["radius"],
                self.validated_data["limit"],
                self.validated_data["query"],
            )
            venues = api_request.venues_list
            places = Places(
                latitude=self.validated_data["latitude"],
                longitude=self.validated_data["longitude"],
                radius=self.validated_data["radius"],
                query=self.validated_data["query"],
                limit=self.validated_data["limit"],
                venues=venues,
            )
            places.save()
            return places
        else:
            return False
