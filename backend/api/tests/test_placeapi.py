from api.placeapi import PlacesApiRequest


def test_places_response():
    test_places = PlacesApiRequest(52.2297700, 21.0117800, 500, 5, "food")
    response = test_places.response["groups"][0]["items"][0]["venue"]
    isinstance(response["id"], str)
    isinstance(response["name"], str)
    isinstance(response["categories"][0]["name"], str)
    isinstance(response["location"]["formattedAddress"], list)
    isinstance(response["location"]["lat"], float)
    isinstance(response["location"]["lng"], float)
    isinstance(response["location"]["distance"], int)
