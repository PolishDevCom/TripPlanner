"""Gets information from Foursquare API."""

import json

import requests

from .utils import get_api_key, get_secret_key


class PlacesApi:
    """
    Class for handling API requests from the Foursquare database.

    Attributes:
        longitude (float): The longitude of the location.
        latitude (float): The latitude of the location.
        radius (int): The maximum distance of a venue from the location.
        limit (int): Total of the results returned.
        query (str): Query about the types of venues.
        venues (list): List of venues returned by API.
    """

    def __init__(
        self,
        longitude: float,
        latitude: float,
        radius: int,
        limit: int,
        query: str,
    ) -> None:
        """Initializes PlacesApi object."""
        self.longitude = longitude
        self.latitude = latitude
        self.radius = radius
        self.limit = limit
        self.query = query
        self.venues = None

    def get_venues(self):
        """Sets list of venues"""
        response = self.make_request()
        self.limit = len(response)
        venues = []
        for index, el in enumerate(response):
            item = {
                "name": el["venue"]["name"],
                "categories": el["venue"]["categories"][0]["name"],
                "address": el["venue"]["location"]["formattedAddress"],
                "latitude": el["venue"]["location"]["lat"],
                "longitude": el["venue"]["location"]["lng"],
                "distance": el["venue"]["location"]["distance"],
                "id": el["venue"]["id"],
            }
            venues.append(item)
        self.venues = venues

    def make_request(self) -> list:
        """
        Sends requests to the API and returns response.

        Returns:
            list: API response
        """
        url = "https://api.foursquare.com/v2/venues/explore"
        params = dict(
            client_id=get_api_key("FOURSQUARE_API_KEY"),
            client_secret=get_secret_key("FOURSQUARE_API_SECRET"),
            v="20210303",
            ll=f"{self.longitude},{self.latitude}",
            radius=self.radius,
            query=f"{self.query}",
            limit=self.limit,
        )
        resp = requests.get(url=url, params=params)
        items = json.loads(resp.text)
        return items["response"]["groups"][0]["items"]
