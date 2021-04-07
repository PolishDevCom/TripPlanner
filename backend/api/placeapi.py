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


class PlacesApiRequest:
    def __init__(self, longitude, latitude, radius, limit, query):
        self.longitude = longitude
        self.latitude = latitude
        self.radius = radius
        self.limit = limit
        self.query = query
        self.api_key = Secrets.obtain_api_key()
        self.secret = Secrets.obtain_secret()
        self.response = self.make_request()
        self.venues_list = self.make_venue_list()

    def make_request(self):
        url = "https://api.foursquare.com/v2/venues/explore"
        params = dict(
            client_id=f"{self.api_key}",
            client_secret=f"{self.secret}",
            v="20210303",
            ll=f"{self.longitude},{self.latitude}",
            radius=self.radius,
            query=f"{self.query}",
            limit=self.limit,
        )
        resp = requests.get(url=url, params=params)
        items = json.loads(resp.text)
        self.limit = len(items["response"]["groups"][0]["items"])
        return items["response"]

    def make_venue_list(self):
        venues_list = []
        for i in range(self.limit):
            item = {
                "name": self.response["groups"][0]["items"][i]["venue"][
                    "name"
                ],
                "categories": self.response["groups"][0]["items"][i]["venue"][
                    "categories"
                ][0]["name"],
                "address": self.response["groups"][0]["items"][i]["venue"][
                    "location"
                ]["formattedAddress"],
                "latitude": self.response["groups"][0]["items"][i]["venue"][
                    "location"
                ]["lat"],
                "longitude": self.response["groups"][0]["items"][i]["venue"][
                    "location"
                ]["lng"],
                "distance": self.response["groups"][0]["items"][i]["venue"][
                    "location"
                ]["distance"],
                "id": self.response["groups"][0]["items"][i]["venue"]["id"],
            }
            venues_list.append(item)
        return venues_list
