from api.models import Places, Route, Venue
from api.placeapi import PlacesApiRequest, VenueApiRequest
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
                    distance=RouteApiRequest.get_distance(
                        api_request.reply, api_request.reply_valid
                    ),
                    coordinates_json=RouteApiRequest.get_coordinates(
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
            "longitude",
            "lattitude",
            "radius",
            "query",
            "limit",
            "venues",
        ]
        extra_kwargs = {"venues": {"read_only": True}}

    def create(self, validated_data):
        if self.is_valid():
            api_request = PlacesApiRequest(
                self.validated_data["longitude"],
                self.validated_data["lattitude"],
                self.validated_data["radius"],
                self.validated_data["limit"],
                self.validated_data["query"],
            )
            venues = api_request.venues_list
            places = Places(
                longitude=self.validated_data["longitude"],
                lattitude=self.validated_data["lattitude"],
                radius=self.validated_data["radius"],
                query=self.validated_data["query"],
                limit=self.validated_data["limit"],
                venues=venues,
            )
            places.save()
            return places
        else:
            return False


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = [
            "venue_id",
            "name",
            "categories",
            "photo",
            "address",
            "rating",
            "longitude",
            "lattitude",
            "similar_venues",
        ]
        extra_kwargs = {
            "name": {"read_only": True},
            "categories": {"read_only": True},
            "address": {"read_only": True},
            "photo": {"read_only": True},
            "rating": {"read_only": True},
            "longitude": {"read_only": True},
            "lattitude": {"read_only": True},
            "similar_venues": {"read_only": True},
        }

    def create(self, validated_data):
        if self.is_valid():
            api_request = VenueApiRequest(self.validated_data["venue_id"])
            details = api_request.get_venue_details()
            venue = Venue(
                venue_id=self.validated_data["venue_id"],
                name=details["name"],
                categories=details["categories"],
                photo=details["photo"],
                address=details["address"],
                longitude=details["longitude"],
                lattitude=details["lattitude"],
                rating=details["rating"],
                similar_venues=api_request.similar_venues,
            )
            venue.save()
            return venue
        else:
            return False
