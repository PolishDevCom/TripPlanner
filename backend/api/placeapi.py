import json

import requests

from .utils import get_api_key, get_secret_key


class PlacesApiRequest:
    """
    Class for handling API requests from the Foursquare database.

    Args:
        longitude (float): The longitude of the desired location.
        latitude (float): The latitude of the desired location.
        radius (int): The maximum distance of a venue from the desired location.
        limit (int): Limit of the results returned.
        query (str): Query about the types of venues.

    Attributes:
        longitude (float): The longitude of the desired location.
        latitude (float): The latitude of the desired location.
        radius (int): The maximum distance of a venue from the desired location.
        limit (int): Limit of the results returned.
        query (str): Query about the types of venues.
        response (list): Response given by Foursquare API.
        venues (list): List of venues returned by API.
    """

    def __init__(self, longitude, latitude, radius, limit, query):
        self.longitude = longitude
        self.latitude = latitude
        self.radius = radius
        self.limit = limit
        self.query = query
        self.response = self.make_request()
        self.venues = self.get_venues()

    def make_request(self) -> dict:
        """
        Function that sends requests to the API.

        Returns:
            dict: Briefer API response.

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
        self.limit = len(items["response"]["groups"][0]["items"])
        items = items["response"]["groups"][0]["items"]
        return items

    def get_venues(self) -> list:
        """
        Method for selecting information about venues and saving
        them to a list variable.

        Returns:
            list: List of objects with desired information.

        """
        venues = []
        for index, el in enumerate(self.response):
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
        return venues
