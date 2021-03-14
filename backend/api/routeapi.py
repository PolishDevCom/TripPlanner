import json
import requests


class RouteApiRequest():
    def __init__(self, longitude_start, latitude_start, longitude_end, latitude_end):
        self.longitude_start = longitude_start
        self.latitude_start = latitude_start
        self.longitude_end = longitude_end
        self.latitude_end = latitude_end

        self.api_key = self.obtain_api_key()
        self.api_key_valid = bool(self.api_key)

        self.reply = self.request_external_api()
        self.reply_valid = self.is_reply_success()

    def obtain_api_key(self):
        try:
            with open("api_keys.json") as api_keys:
                return json.loads(api_keys.read()).get("ROUTE_API_KEY")
        except:
            return False

    def request_external_api(self):
        if self.api_key_valid:
            base_url = "https://api.openrouteservice.org/v2/directions/driving-car?api_key="
            url = f"{base_url}{self.api_key}&start={str(self.longitude_start)},{str(self.latitude_start)}&end={str(self.longitude_end)},{str(self.latitude_end)}"
            return json.loads(requests.get(url).text)
        else:
            return {"error": True}

    def is_reply_success(self):
        if "error" in self.reply or self.api_key_valid == False:
            return False
        else:
            return True

    @staticmethod
    def get_coordinates(reply, reply_valid):
        if reply_valid:
            return reply["features"][0]["geometry"]["coordinates"]
        else:
            return False

    @staticmethod
    def get_distance(reply, reply_valid):
        if reply_valid:
            return reply["features"][0]["properties"]["segments"][0]["distance"]
        else:
            return False
