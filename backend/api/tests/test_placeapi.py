"""Tests for api/placeapi.py."""

from api.placeapi import PlacesApi


def test_make_request():
    """Tests response given by Foursquare API."""
    test_place = PlacesApi(52.2297700, 21.0117800, 500, 5, "food")
    response = test_place.make_request()[0]["venue"]
    isinstance(response["id"], str)
    isinstance(response["name"], str)
    isinstance(response["categories"][0]["name"], str)
    isinstance(response["location"]["formattedAddress"], list)
    isinstance(response["location"]["lat"], float)
    isinstance(response["location"]["lng"], float)
    isinstance(response["location"]["distance"], int)
