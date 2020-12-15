import json
import requests


class RouteApiRequest():
    def __init__(self, longitude_start, latitude_start, longitude_end, latitude_end):
        self.longitude_start = longitude_start
        self.latitude_start = latitude_start
        self.longitude_end = longitude_end
        self.latitude_end = latitude_end
        self.api_key = self.obtain_api_key()

    def obtain_api_key(self):
        with open("api_keys.json") as api_keys:
            return json.loads(api_keys.read()).get("ROUTE_API_KEY")

    def make_url(self):
        base_url = "https://api.openrouteservice.org/v2/directions/driving-car?api_key="
        return(f"{base_url}{self.api_key}&start={str(self.longitude_start)},{str(self.latitude_start)}&end={str(self.longitude_end)},{str(self.latitude_end)}")

    def request_external_api(self):
        r = requests.get(self.make_url())
        page_source = r.text
        return json.loads(page_source)

    def give_coordinates(self):
        return self.request_external_api()["features"][0]["geometry"]["coordinates"]

    def give_distance(self):
        return self.request_external_api()["features"][0]["properties"]["segments"][0]["distance"]
