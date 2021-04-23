"""Tests for api/placeapi.py."""

from api.placeapi import PlacesApi

successful_response = [
    {
        "reasons": {
            "count": 0,
            "items": [
                {
                    "summary": "This spot is popular",
                    "type": "general",
                    "reasonName": "globalInteractionReason",
                }
            ],
        },
        "venue": {
            "id": "5c4231f5d3cce8002c16adad",
            "name": "Żebra i Kości",
            "location": {
                "address": "38 Poznańska",
                "lat": 52.228745,
                "lng": 21.010029,
                "labeledLatLngs": [
                    {"label": "display", "lat": 52.228745, "lng": 21.010029}
                ],
                "distance": 165,
                "postalCode": "00-689",
                "cc": "PL",
                "city": "Warszawa",
                "state": "Województwo mazowieckie",
                "country": "Polska",
                "formattedAddress": [
                    "38 Poznańska",
                    "00-689 Warszawa",
                    "Polska",
                ],
            },
            "categories": [
                {
                    "id": "52e81612bcbc57f1066b7a04",
                    "name": "Polish Restaurant",
                    "pluralName": "Polish Restaurants",
                    "shortName": "Polish",
                    "icon": {
                        "suffix": ".png",
                    },
                }
            ],
            "photos": {"count": 0, "groups": []},
        },
        "referralId": "e-0-5c4231f5d3cce8002c16adad-0",
    },
    {
        "reasons": {
            "count": 0,
            "items": [
                {
                    "summary": "This spot is popular",
                    "type": "general",
                    "reasonName": "globalInteractionReason",
                }
            ],
        },
        "venue": {
            "id": "559ffcc3498eb8d1d43c225f",
            "name": "Soul Kitchen Bistro",
            "location": {
                "address": "Nowogrodzka 18A",
                "lat": 52.229366,
                "lng": 21.014921,
                "labeledLatLngs": [
                    {"label": "display", "lat": 52.229366, "lng": 21.014921}
                ],
                "distance": 218,
                "cc": "PL",
                "neighborhood": "Śródmieście Południowe",
                "city": "Warszawa",
                "state": "Województwo mazowieckie",
                "country": "Polska",
                "formattedAddress": ["Nowogrodzka 18A", "Warszawa", "Polska"],
            },
            "categories": [
                {
                    "id": "52e81612bcbc57f1066b79f1",
                    "name": "Bistro",
                    "pluralName": "Bistros",
                    "shortName": "Bistro",
                    "icon": {
                        "suffix": ".png",
                    },
                }
            ],
            "photos": {"count": 0, "groups": []},
        },
        "referralId": "e-0-559ffcc3498eb8d1d43c225f-1",
    },
    {
        "reasons": {
            "count": 0,
            "items": [
                {
                    "summary": "This spot is popular",
                    "type": "general",
                    "reasonName": "globalInteractionReason",
                }
            ],
        },
        "venue": {
            "id": "562fcc8d498eebd6fb16ec1a",
            "name": "N31",
            "location": {
                "address": "Nowogrodzka 31",
                "lat": 52.228924,
                "lng": 21.01328,
                "labeledLatLngs": [
                    {"label": "display", "lat": 52.228924, "lng": 21.01328}
                ],
                "distance": 139,
                "cc": "PL",
                "neighborhood": "Śródmieście Południowe",
                "country": "Polska",
                "formattedAddress": ["Nowogrodzka 31", "Polska"],
            },
            "categories": [
                {
                    "id": "4bf58dd8d48988d147941735",
                    "name": "Diner",
                    "pluralName": "Diners",
                    "shortName": "Diner",
                    "icon": {
                        "suffix": ".png",
                    },
                }
            ],
            "photos": {"count": 0, "groups": []},
        },
        "referralId": "e-0-562fcc8d498eebd6fb16ec1a-2",
    },
]


def test_get_venues():
    """Tests response given by Foursquare API."""
    test_place = PlacesApi(52.2297700, 21.0117800, 500, "food")

    result = test_place.get_venues(successful_response)

    assert isinstance(result[0]["id"], str)
    assert isinstance(result[0]["name"], str)
    assert isinstance(result[0]["categories"], str)
    assert isinstance(result[0]["address"], list)
    assert isinstance(result[0]["latitude"], float)
    assert isinstance(result[0]["longitude"], float)
    assert isinstance(result[0]["distance"], int)
