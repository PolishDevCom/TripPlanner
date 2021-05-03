"""Gets Venue information from Foursquare API."""

import json

import requests

from .utils import get_key


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
        venue_categories = [
            category["name"] for category in response["categories"]
        ]
        details = {
            "name": response["name"],
            "address": response["location"]["formattedAddress"],
            "latitude": response["location"]["lat"],
            "longitude": response["location"]["lng"],
            "categories": venue_categories,
            "contact": response["contact"],
        }
        return details

    def make_request(self) -> dict:
        """
        Sends request to the API and returns venue details response.

        Returns:
            dict: API response
        """
        client_id = get_key("FOURSQUARE_API_KEY")
        client_secret = get_key("FOURSQUARE_API_SECRET")
        url = (
            f"https://api.foursquare.com/v2/venues/{self.venue_id}?"
            f"client_id={client_id}&client_secret={client_secret}&v=20210303"
        )
        resp = requests.get(url=url)
        response = json.loads(resp.text)
        return response["response"]["venue"]
