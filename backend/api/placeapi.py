import json
import requests


class PlacesApiRequest:
    def __init__(self, longitude, latitude, radius, limit, query):
        self.longitude = longitude
        self.latitude = latitude
        self.radius = radius
        self.limit = limit
        self.query = query
        self.api_key = self.obtain_api_key()
        self.secret = self.obtain_secret()
        self.response = self.make_request()
        self.venues_list = self.make_venue_list()

    def obtain_api_key(self):
        with open("api_keys.json") as api_keys:
            return json.loads(api_keys.read()).get("PLACES_API_KEY")

    def obtain_secret(self):
        with open("secret.json") as secret:
            return json.loads(secret.read()).get("SECRET_KEY_PLACES")

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
        return items

    def make_venue_list(self):
        venues_list = []
        for i in range(self.limit):
            item = {
                "name": self.response["response"]["groups"][0]["items"][i]["venue"][
                    "name"
                ],
                "categories": self.response["response"]["groups"][0]["items"][i][
                    "venue"
                ]["categories"][0]["name"],
                "address": self.response["response"]["groups"][0]["items"][i]["venue"][
                    "location"
                ]["formattedAddress"],
                "lattitude": self.response["response"]["groups"][0]["items"][i][
                    "venue"
                ]["location"]["lat"],
                "longitude": self.response["response"]["groups"][0]["items"][i][
                    "venue"
                ]["location"]["lng"],
                "distance": self.response["response"]["groups"][0]["items"][i]["venue"][
                    "location"
                ]["distance"],
                "id": self.response["response"]["groups"][0]["items"][i]["venue"]["id"],
            }
            venues_list.append(item)
        return venues_list


class VenueApiRequest:
    def __init__(self, venue_id):
        self.api_key = self.obtain_api_key()
        self.secret = self.obtain_secret()
        self.response = self.venue_request(venue_id)
        self.details = self.get_venue_details()
        self.similar_venues = self.get_similar_venues(venue_id)

    def obtain_api_key(self):
        with open("api_keys.json") as api_keys:
            return json.loads(api_keys.read()).get("PLACES_API_KEY")

    def obtain_secret(self):
        with open("secret.json") as secret:
            return json.loads(secret.read()).get("SECRET_KEY_PLACES")

    def venue_request(self, venue_id):
        url = f"https://api.foursquare.com/v2/venues/{venue_id}?client_id={self.api_key}&client_secret={self.secret}&v=20210303"
        resp = requests.get(url=url)
        return json.loads(resp.text)

    def get_venue_details(self):
        categories_length = len(self.response["response"]["venue"]["categories"])
        venue_categories = []
        for i in range(categories_length):
            venue_categories.append(
                self.response["response"]["venue"]["categories"][i]["name"]
            )
        details = {
            "name": self.response["response"]["venue"]["name"],
            "address": self.response["response"]["venue"]["location"][
                "formattedAddress"
            ],
            "lattitude": self.response["response"]["venue"]["location"]["lat"],
            "longitude": self.response["response"]["venue"]["location"]["lng"],
            "categories": venue_categories,
            "rating": self.response["response"]["venue"]["rating"],
            "photo": (
                self.response["response"]["venue"]["bestPhoto"]["prefix"]
                + "original"
                + self.response["response"]["venue"]["bestPhoto"]["suffix"]
            ),
            "attributes": self.response["response"]["venue"]["attributes"]["groups"],
        }
        return details

    def get_similar_venues(self, venue_id):
        url = f"https://api.foursquare.com/v2/venues/{venue_id}/similar?client_id={self.api_key}&client_secret={self.secret}&v=20210303"
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        count = data["response"]["similarVenues"]["count"]
        similar_venues = []
        for i in range(count):
            similar_venue_details = {
                "name": data["response"]["similarVenues"]["items"][i]["name"],
                "address": data["response"]["similarVenues"]["items"][i]["location"][
                    "formattedAddress"
                ],
                "lattitude": data["response"]["similarVenues"]["items"][i]["location"][
                    "lat"
                ],
                "longtitude": data["response"]["similarVenues"]["items"][i]["location"][
                    "lng"
                ],
                "category": data["response"]["similarVenues"]["items"][i]["categories"][
                    0
                ]["name"],
            }
            similar_venues.append(similar_venue_details)
        return similar_venues


# from api.placeapi import PlacesApiRequest
# from api.placeapi import VenueApiRequest
# places = PlacesApiRequest(52.2297700,21.0117800,500,5,"food")
# print(places.venues_list)
# venue = VenueApiRequest("5141be20e4b0d830a88733f4")
# print(venue.details)
# print(venue.similar_venues)
