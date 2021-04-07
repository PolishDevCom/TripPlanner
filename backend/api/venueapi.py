import json

import requests


class Secrets:
    @classmethod
    def obtain_api_key(self):
        with open("api_keys.json") as api_keys:
            return json.loads(api_keys.read()).get("PLACES_API_KEY")

    @classmethod
    def obtain_secret(self):
        with open("secret.json") as secret:
            return json.loads(secret.read()).get("SECRET_KEY_PLACES")


class VenueApiRequest:
    def __init__(self, venue_id):
        self.api_key = Secrets.obtain_api_key()
        self.secret = Secrets.obtain_secret()
        self.response = self.venue_request(venue_id)
        self.details = self.get_venue_details()
        self.similar_venues = self.get_similar_venues(venue_id)

    def venue_request(self, venue_id):
        url = (
            f"https://api.foursquare.com/v2/venues/{venue_id}?"
            f"client_id={self.api_key}&client_secret={self.secret}&v=20210303"
        )
        resp = requests.get(url=url)
        response = json.loads(resp.text)
        return response["response"]

    def get_venue_details(self):
        categories_length = len(self.response["venue"]["categories"])
        venue_categories = []
        for i in range(categories_length):
            venue_categories.append(
                self.response["venue"]["categories"][i]["name"]
            )
        details = {
            "id": self.response["venue"]["id"],
            "name": self.response["venue"]["name"],
            "address": self.response["venue"]["location"]["formattedAddress"],
            "latitude": self.response["venue"]["location"]["lat"],
            "longitude": self.response["venue"]["location"]["lng"],
            "categories": venue_categories,
            "rating": self.response["venue"]["rating"],
            "photo": (
                self.response["venue"]["bestPhoto"]["prefix"]
                + "original"
                + self.response["venue"]["bestPhoto"]["suffix"]
            ),
            "attributes": self.response["venue"]["attributes"]["groups"],
        }
        return details

    def get_similar_venues(self, venue_id):
        url = (
            f"https://api.foursquare.com/v2/venues/{venue_id}/similar?"
            f"client_id={self.api_key}&client_secret={self.secret}&v=20210303"
        )
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        count = data["response"]["similarVenues"]["count"]
        similar_venues = []
        for i in range(count):
            similar_venue_details = {
                "venue_id": data["response"]["similarVenues"]["items"][i][
                    "id"
                ],
                "name": data["response"]["similarVenues"]["items"][i]["name"],
                "address": data["response"]["similarVenues"]["items"][i][
                    "location"
                ]["formattedAddress"],
                "latitude": data["response"]["similarVenues"]["items"][i][
                    "location"
                ]["lat"],
                "longitude": data["response"]["similarVenues"]["items"][i][
                    "location"
                ]["lng"],
                "category": data["response"]["similarVenues"]["items"][i][
                    "categories"
                ][0]["name"],
            }
            similar_venues.append(similar_venue_details)
        return similar_venues
