"""Stores serializers."""

from api.models import Places, Route, Venue
from api.placeapi import PlacesApi
from api.routeapi import RouteApiRequest
from api.venueapi import VenueApi
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
    """ Serializer for Places object."""

    class Meta:
        """Serializer based on Places model."""

        model = Places
        fields = [
            "latitude",
            "longitude",
            "radius",
            "query",
            "venues",
        ]
        extra_kwargs = {"venues": {"read_only": True}}

    def create(self, validated_data: dict) -> object:
        """
        Creates Places object.

        Args:
            validated_data (dict): Places object data.

        Returns:
            object: Places object
        """
        if not self.is_valid():
            return None
        api_request = PlacesApi(
            self.validated_data["latitude"],
            self.validated_data["longitude"],
            self.validated_data["radius"],
            self.validated_data["query"],
        )
        response = api_request.make_request()
        venues = api_request.get_venues(response)
        places = Places(
            latitude=self.validated_data["latitude"],
            longitude=self.validated_data["longitude"],
            radius=self.validated_data["radius"],
            query=self.validated_data["query"],
            venues=venues,
        )
        places.save()
        return places


class VenueSerializer(serializers.ModelSerializer):
    """ Serializer for Veune object."""

    class Meta:
        """Serializer based on Venue model."""

        model = Venue
        fields = [
            "venue_id",
            "name",
            "categories",
            "photo",
            "address",
            "longitude",
            "latitude",
            "similar_venues",
        ]
        extra_kwargs = {
            "name": {"read_only": True},
            "categories": {"read_only": True},
            "address": {"read_only": True},
            "photo": {"read_only": True},
            "longitude": {"read_only": True},
            "latitude": {"read_only": True},
            "similar_venues": {"read_only": True},
        }

    def create(self, validated_data: dict) -> object:
        """
        Creates Venue object.

        Args:
            validated_data (dict): Validated venue object data.

        Returns:
            object: Venue object
        """
        if not self.is_valid():
            return None
        api_request = VenueApi(self.validated_data["venue_id"])
        details_response = api_request.make_request()
        details = api_request.get_details(details_response)
        similar_response = api_request.make_request_similar()
        similar_venues = api_request.get_similar_venues(similar_response)
        venue = Venue(
            venue_id=self.validated_data["venue_id"],
            name=details["name"],
            categories=details["categories"],
            address=details["address"],
            longitude=details["longitude"],
            latitude=details["latitude"],
            similar_venues=similar_venues,
        )
        try:
            venue.photo = details["photo"]
        except:
            pass
        venue.save()
        return venue
