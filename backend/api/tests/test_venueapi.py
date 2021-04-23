"""Tests for api/venueapi.py."""

from api.venueapi import VenueApi


def test_get_details():
    """Tests get_details()."""
    test_venue = VenueApi("4c55b289f5f3d13ad7f539fc")

    result = test_venue.get_details(succesfull_venue_response)

    assert isinstance(result["name"], str)
    assert isinstance(result["address"], list)
    assert isinstance(result["latitude"], float)
    assert isinstance(result["longitude"], float)
    assert isinstance(result["categories"], list)
    assert isinstance(result["photo"], str)
    assert isinstance(result["attributes"], list)


def test_get_similar_venues():
    """Tests get_similar_venues()"""
    test_venue = VenueApi("4c55b289f5f3d13ad7f539fc")

    result = test_venue.get_similar_venues(succesfull_similar_venues)
    assert isinstance(result[0]["id"], str)
    assert isinstance(result[0]["name"], str)
    assert isinstance(result[0]["address"], list)
    assert isinstance(result[0]["latitude"], float)
    assert isinstance(result[0]["longitude"], float)
    assert isinstance(result[0]["category"], str)


succesfull_venue_response = {
    "id": "4c55b289f5f3d13ad7f539fc",
    "name": "Kino Pod Baranami",
    "contact": {
        "phone": "+48124230768",
        "formattedPhone": "+48 12 423 07 68",
        "twitter": "kinopodbaranami",
        "facebook": "29546594493",
        "facebookUsername": "kinopodbaranami",
        "facebookName": "Kino Pod Baranami",
    },
    "location": {
        "address": "Rynek Główny 27",
        "lat": 50.061604,
        "lng": 19.935257,
        "labeledLatLngs": [
            {"label": "display", "lat": 50.061604, "lng": 19.935257}
        ],
        "postalCode": "31-010",
        "cc": "PL",
        "city": "Kraków",
        "state": "Województwo małopolskie",
        "country": "Polska",
        "formattedAddress": ["Rynek Główny 27", "31-010 Kraków", "Polska"],
    },
    "canonicalUrl": "https://foursquare.com/kinopodbaranami",
    "categories": [
        {
            "id": "4bf58dd8d48988d17e941735",
            "name": "Indie Movie Theater",
            "pluralName": "Indie Movie Theaters",
            "shortName": "Indie Movies",
            "icon": {"suffix": ".png"},
        }
    ],
    "stats": {"tipCount": 25},
    "url": "http://www.kinopodbaranami.pl",
    "likes": {
        "count": 195,
        "groups": [{"type": "others", "count": 195, "items": []}],
        "summary": "195 Likes",
    },
    "rating": 8.7,
    "ratingColor": "73CF42",
    "ratingSignals": 233,
    "beenHere": {
        "count": 0,
        "unconfirmedCount": 0,
        "lastCheckinExpiredAt": 0,
    },
    "specials": {"count": 0, "items": []},
    "photos": {
        "count": 65,
        "groups": [
            {
                "type": "venue",
                "name": "Venue photos",
                "count": 65,
                "items": [
                    {
                        "id": "525046df8bbd25fc4789aa4d",
                        "createdAt": 1380992735,
                        "source": {
                            "name": "Foursquare Web",
                            "url": "https://foursquare.com",
                        },
                        "prefix": "https://fastly.4sqi.net/img/general/",
                        "width": 650,
                        "height": 421,
                        "visibility": "public",
                    }
                ],
            }
        ],
    },
    "venuePage": {"id": "61078362"},
    "reasons": {
        "count": 1,
        "items": [
            {
                "summary": "Lots of people like this place",
                "type": "general",
                "reasonName": "rawLikesReason",
            }
        ],
    },
    "storeId": "",
    "page": {
        "user": {
            "firstName": "Kino Pod Baranami",
            "countryCode": "PL",
            "type": "venuePage",
            "venue": {"id": "4c55b289f5f3d13ad7f539fc"},
            "tips": {"count": 1},
            "lists": {
                "groups": [{"type": "created", "count": 2, "items": []}]
            },
            "bio": "",
        }
    },
    "hereNow": {"count": 0, "summary": "Nobody here", "groups": []},
    "createdAt": 1280684681,
    "tips": {
        "count": 25,
        "groups": [
            {
                "type": "others",
                "name": "All tips",
                "count": 25,
                "items": [
                    {
                        "id": "4ff729cee4b01992aa9840e3",
                        "createdAt": 1341598158,
                        "type": "user",
                        "lang": "en",
                        "likes": {
                            "count": 8,
                            "groups": [
                                {
                                    "type": "others",
                                    "count": 8,
                                    "items": [
                                        {
                                            "firstName": "Baranov",
                                            "lastName": "M",
                                            "countryCode": "NL",
                                        },
                                        {
                                            "firstName": "Marcin",
                                            "lastName": "C",
                                            "countryCode": "PL",
                                        },
                                        {
                                            "firstName": "Fyodor",
                                            "lastName": "Z",
                                            "countryCode": "ID",
                                        },
                                        {
                                            "firstName": "Mary",
                                            "lastName": "?",
                                            "countryCode": "JP",
                                        },
                                    ],
                                }
                            ],
                            "summary": "8 likes",
                        },
                        "agreeCount": 8,
                        "disagreeCount": 0,
                        "todo": {"count": 1},
                        "user": {
                            "firstName": "Irek",
                            "lastName": "S",
                            "countryCode": "PL",
                        },
                    }
                ],
            }
        ],
    },
    "shortUrl": "http://4sq.com/bnFOaq",
    "timeZone": "Europe/Warsaw",
    "listed": {
        "count": 106,
        "groups": [
            {
                "type": "others",
                "name": "Lists from other people",
                "count": 106,
                "items": [
                    {
                        "id": "4fddf650e4b082d076bd5ccb",
                        "name": "KRK",
                        "description": "",
                        "type": "others",
                        "user": {
                            "firstName": "dominika",
                            "lastName": "b",
                            "countryCode": "PL",
                        },
                        "url": "/user/15741139/list/krk",
                        "createdAt": 1339946576,
                        "updatedAt": 1406135191,
                        "followers": {"count": 12},
                        "listItems": {
                            "count": 60,
                            "items": [
                                {
                                    "id": "v4c55b289f5f3d13ad7f539fc",
                                    "createdAt": 1339946796,
                                }
                            ],
                        },
                    },
                    {
                        "id": "5a4758d19cadd921f24a3cc3",
                        "name": "Krakov Tekso list",
                        "description": "",
                        "type": "others",
                        "user": {
                            "firstName": "Aleksey",
                            "lastName": "T",
                            "countryCode": "UA",
                        },
                        "url": "/user/52767703/list/krakov-tekso-list",
                        "createdAt": 1514625233,
                        "updatedAt": 1539328112,
                        "photo": {
                            "id": "525be4a6498e5d8e921b1937",
                            "createdAt": 1381754022,
                            "prefix": "https://fastly.4sqi.net/img/general/",
                            "width": 960,
                            "height": 720,
                            "visibility": "public",
                        },
                        "followers": {"count": 9},
                        "listItems": {
                            "count": 25,
                            "items": [
                                {
                                    "id": "v4c55b289f5f3d13ad7f539fc",
                                    "createdAt": 1539255710,
                                }
                            ],
                        },
                    },
                    {
                        "id": "5144a40fe4b0c0b7eb1b57f3",
                        "name": "Travellers Inn Kraków Kit",
                        "type": "others",
                        "user": {
                            "firstName": "Zofia",
                            "lastName": "P",
                            "countryCode": "PL",
                        },
                        "createdAt": 1363452943,
                        "updatedAt": 1381491810,
                        "photo": {
                            "id": "5144a67c582f8dddaa88c8a7",
                            "createdAt": 1363453564,
                            "prefix": "https://fastly.4sqi.net/img/general/",
                            "width": 1200,
                            "height": 1200,
                            "visibility": "public",
                        },
                        "followers": {"count": 15},
                        "listItems": {
                            "count": 73,
                            "items": [
                                {
                                    "id": "t5252d93911d27af63d7802da",
                                    "createdAt": 1381161724,
                                    "photo": {
                                        "id": "5217813dbce6bd87ba105f90",
                                        "createdAt": 1377272125,
                                        "width": 850,
                                        "height": 315,
                                        "visibility": "public",
                                    },
                                }
                            ],
                        },
                    },
                    {
                        "id": "4eac8786b634339687616f11",
                        "name": "Best of Kraków",
                        "description": "",
                        "type": "others",
                        "user": {
                            "firstName": "Roberto",
                            "lastName": "Y",
                            "countryCode": "SG",
                        },
                        "url": "/user/6584096/list/best-of-krak%C3%B3w",
                        "createdAt": 1319929734,
                        "updatedAt": 1515355412,
                        "photo": {
                            "id": "5076d058e4b0c314980d969d",
                            "createdAt": 1349963864,
                            "prefix": "https://fastly.4sqi.net/img/general/",
                            "width": 540,
                            "height": 720,
                            "visibility": "public",
                        },
                        "followers": {"count": 18},
                        "listItems": {
                            "count": 23,
                            "items": [
                                {
                                    "id": "v4c55b289f5f3d13ad7f539fc",
                                    "createdAt": 1351463653,
                                }
                            ],
                        },
                    },
                ],
            }
        ],
    },
    "popular": {
        "timeframes": [
            {
                "days": "Today",
                "open": [{"renderedTime": "5:00 PM–Midnight"}],
                "segments": [],
            },
            {
                "days": "Fri",
                "open": [{"renderedTime": "4:00 PM–11:00 PM"}],
                "segments": [],
            },
            {
                "days": "Sat",
                "open": [{"renderedTime": "Noon–Midnight"}],
                "segments": [],
            },
            {
                "days": "Sun",
                "open": [{"renderedTime": "Noon–10:00 PM"}],
                "segments": [],
            },
            {
                "days": "Mon–Tue",
                "open": [{"renderedTime": "5:00 PM–10:00 PM"}],
                "segments": [],
            },
            {
                "days": "Wed",
                "open": [{"renderedTime": "6:00 PM–10:00 PM"}],
                "segments": [],
            },
        ]
    },
    "seasonalHours": [],
    "pageUpdates": {"count": 0, "items": []},
    "inbox": {"count": 0, "items": []},
    "attributes": {
        "groups": [
            {
                "type": "reservations",
                "name": "Reservations",
                "summary": "Reservations",
                "count": 3,
                "items": [
                    {"displayName": "Reservations", "displayValue": "Yes"}
                ],
            },
            {
                "type": "payments",
                "name": "Credit Cards",
                "summary": "Credit Cards",
                "count": 5,
                "items": [
                    {
                        "displayName": "Credit Cards",
                    }
                ],
            },
            {
                "type": "wifi",
                "name": "Wi-Fi",
                "summary": "Free Wi-Fi",
                "count": 1,
                "items": [{"displayName": "Wi-Fi", "displayValue": "Free"}],
            },
        ]
    },
    "bestPhoto": {
        "id": "525046df8bbd25fc4789aa4d",
        "createdAt": 1380992735,
        "source": {"name": "Foursquare Web", "url": "https://foursquare.com"},
        "prefix": "https://fastly.4sqi.net/img/general/",
        "suffix": "/61078362_tTh4qbeKrGDLnLrIHPCyM1Ji1ZXiS7og0MupFMgfj14.jpg",
        "width": 650,
        "height": 421,
        "visibility": "public",
    },
    "colors": {
        "highlightColor": {
            "photoId": "525046df8bbd25fc4789aa4d",
            "value": -14153720,
        },
        "highlightTextColor": {
            "photoId": "525046df8bbd25fc4789aa4d",
            "value": -1,
        },
        "algoVersion": 3,
    },
}

succesfull_similar_venues = [
    {
        "id": "4f3a9ddfe4b059425acebb2a",
        "name": "Kinokawiarnia KiKa",
        "location": {
            "address": "Ignacego Krasickiego, 31-000 Kraków",
            "lat": 50.0418,
            "lng": 19.940666,
            "labeledLatLngs": [
                {"label": "display", "lat": 50.0418, "lng": 19.940666}
            ],
            "cc": "PL",
            "city": "Kraków",
            "state": "Województwo małopolskie",
            "country": "Polska",
            "formattedAddress": [
                "Ignacego Krasickiego, 31-000 Kraków",
                "Kraków",
                "Polska",
            ],
        },
        "categories": [
            {
                "id": "4bf58dd8d48988d17e941735",
                "name": "Indie Movie Theater",
                "pluralName": "Indie Movie Theaters",
                "shortName": "Indie Movies",
                "icon": {
                    "suffix": ".png",
                },
            }
        ],
    },
    {
        "id": "4bc01f14abf495217cecbe93",
        "name": "Cinema City",
        "location": {
            "address": "Podgórska 34",
            "crossStreet": "Galeria Kazimierz",
            "lat": 50.053875,
            "lng": 19.954483,
            "labeledLatLngs": [
                {"label": "display", "lat": 50.053875, "lng": 19.954483}
            ],
            "postalCode": "31-536",
            "cc": "PL",
            "city": "Kraków",
            "state": "Województwo małopolskie",
            "country": "Polska",
            "formattedAddress": [
                "Podgórska 34 (Galeria Kazimierz)",
                "31-536 Kraków",
                "Polska",
            ],
        },
        "categories": [
            {
                "id": "4bf58dd8d48988d17f941735",
                "name": "Movie Theater",
                "pluralName": "Movie Theaters",
                "shortName": "Movie Theater",
                "icon": {
                    "suffix": ".png",
                },
            }
        ],
    },
    {
        "id": "4be5961abcef2d7ff1f803e5",
        "name": "Kino Mikro",
        "location": {
            "address": "Lea 5",
            "lat": 50.069458,
            "lng": 19.923832,
            "labeledLatLngs": [
                {"label": "display", "lat": 50.069458, "lng": 19.923832}
            ],
            "postalCode": "30-046",
            "cc": "PL",
            "city": "Kraków",
            "state": "Województwo małopolskie",
            "country": "Polska",
            "formattedAddress": ["Lea 5", "30-046 Kraków", "Polska"],
        },
        "categories": [
            {
                "id": "4bf58dd8d48988d17f941735",
                "name": "Movie Theater",
                "pluralName": "Movie Theaters",
                "shortName": "Movie Theater",
                "icon": {
                    "suffix": ".png",
                },
            }
        ],
    },
    {
        "id": "4be19a607cb6d13a7f24be2d",
        "name": "KIJÓW.CENTRUM",
        "location": {
            "address": "Krasińskiego 34",
            "lat": 50.05852,
            "lng": 19.925306,
            "labeledLatLngs": [
                {"label": "display", "lat": 50.05852, "lng": 19.925306}
            ],
            "cc": "PL",
            "city": "Kraków",
            "state": "Województwo małopolskie",
            "country": "Polska",
            "formattedAddress": ["Krasińskiego 34", "Kraków", "Polska"],
        },
        "categories": [
            {
                "id": "4bf58dd8d48988d17f941735",
                "name": "Movie Theater",
                "pluralName": "Movie Theaters",
                "shortName": "Movie Theater",
                "icon": {
                    "suffix": ".png",
                },
            }
        ],
    },
]
