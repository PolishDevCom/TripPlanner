"""Gets Venue information from Foursquare API."""

import json

import requests

from .utils import get_api_key, get_secret_key


class VenueApi:
    """
    Handles API requests for Venues model.

    Attributes:
        id (str): API's id of the venue.
    """

    def __init__(self, venue_id: str) -> None:
        """Initializes VenueApi object."""
        self.venue_id = venue_id

    def get_details(self, response: dict) -> dict:
        """
        Gets and returns details of the venue.

        Args:
            response (dict): Details response from the API.

        Returns:
            dict: Details of the venue.
        """
        categories = response["categories"]
        venue_categories = []
        for category in categories:
            venue_categories.append(category["name"])
        details = {
            "name": response["name"],
            "address": response["location"]["formattedAddress"],
            "latitude": response["location"]["lat"],
            "longitude": response["location"]["lng"],
            "categories": venue_categories,
            "attributes": response["attributes"]["groups"],
            "contact": response["contact"],
        }
        try:
            details["photo"](
                response["bestPhoto"]["prefix"]
                + "original"
                + response["bestPhoto"]["suffix"]
            )
        except:
            pass
        return details

    def get_similar_venues(self, response: list) -> list:
        """
        Gets and returns list of similar venues.

        Args:
            response (dict): Similar venues response from the API.

        Returns:
            list: List of similar venues.
        """
        return [
            {
                "id": el["id"],
                "name": el["name"],
                "address": el["location"]["formattedAddress"],
                "latitude": el["location"]["lat"],
                "longitude": el["location"]["lng"],
                "category": el["categories"][0]["name"],
            }
            for el in response
        ]

    def make_request(self) -> dict:
        """
        Sends request to the API and returns venue details response.

        Returns:
            dict: API response
        """
        client_id = get_api_key("FOURSQUARE_API_KEY")
        client_secret = get_secret_key("FOURSQUARE_API_SECRET")
        url = (
            f"https://api.foursquare.com/v2/venues/{self.venue_id}?"
            f"client_id={client_id}&client_secret={client_secret}&v=20210303"
        )
        resp = requests.get(url=url)
        response = json.loads(resp.text)
        return response["response"]["venue"]

    def make_request_similar(self) -> list:
        """
        Sends requests to the API and returns similar venues response.

        Returns:
            list: API response
        """
        client_id = get_api_key("FOURSQUARE_API_KEY")
        client_secret = get_secret_key("FOURSQUARE_API_SECRET")
        url = (
            f"https://api.foursquare.com/v2/venues/{self.venue_id}/similar?"
            f"client_id={client_id}&client_secret={client_secret}&v=20210303"
        )
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        response = data["response"]["similarVenues"]["items"]
        return response
