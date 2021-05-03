"""Gets information from Foursquare API."""

import json

import requests

from .utils import get_key


class PlacesApi:
    """
    Class for handling API requests from the Foursquare database.

    Attributes:
        longitude (float): The longitude of the location.
        latitude (float): The latitude of the location.
        radius (int): The maximum distance of a venue from the location.
        query (str): Query about the types of venues.
    """

    def __init__(
        self,
        longitude: float,
        latitude: float,
        radius: int,
        query: str,
    ) -> None:
        """Initializes PlacesApi object."""
        self.longitude = longitude
        self.latitude = latitude
        self.radius = radius
        self.query = query

    def get_venues(self, response: list) -> list:
        """
        Returns list of venues

        Args:
            response (list): Response from the API.

        Returns:
            list: Detailed venues list.
        """
        return [
            {
                "name": el["venue"]["name"],
                "categories": el["venue"]["categories"][0]["name"],
                "address": el["venue"]["location"]["formattedAddress"],
                "latitude": el["venue"]["location"]["lat"],
                "longitude": el["venue"]["location"]["lng"],
                "distance": el["venue"]["location"]["distance"],
                "id": el["venue"]["id"],
            }
            for el in response
        ]

    def make_request(self) -> list:
        """
        Sends requests to the API and returns response.

        Returns:
            list: API response.
        """
        url = "https://api.foursquare.com/v2/venues/explore"
        params = dict(
            client_id=get_key("FOURSQUARE_API_KEY"),
            client_secret=get_key("FOURSQUARE_API_SECRET"),
            v="20210303",
            ll=f"{self.longitude},{self.latitude}",
            radius=self.radius,
            query=f"{self.query}",
        )
        resp = requests.get(url=url, params=params)
        items = json.loads(resp.text)
        return items["response"]["groups"][0]["items"]
