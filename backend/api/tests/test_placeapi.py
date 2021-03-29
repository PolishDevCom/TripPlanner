import unittest

from api.placeapi import PlacesApiRequest


class TestConnectionToApi(unittest.TestCase):
    """
    Test module for connecting to FourSquare API
    """

    def setUp(self):
        self.test_places = PlacesApiRequest(
            52.2297700, 21.0117800, 500, 5, "food"
        )

    def test_places_response(self):
        response = self.test_places.response
        self.assertEqual(response["query"], "food")
        self.assertIsInstance(
            response["groups"][0]["items"][0]["venue"]["id"], str
        )
        self.assertIsInstance(
            response["groups"][0]["items"][0]["venue"]["name"], str
        )
        self.assertIsInstance(
            response["groups"][0]["items"][0]["venue"]["categories"][0][
                "name"
            ],
            str,
        )
        self.assertIsInstance(
            response["groups"][0]["items"][0]["venue"]["location"][
                "formattedAddress"
            ],
            list,
        )
        self.assertIsInstance(
            response["groups"][0]["items"][0]["venue"]["location"]["lat"],
            float,
        )
        self.assertIsInstance(
            response["groups"][0]["items"][0]["venue"]["location"]["lng"],
            float,
        )
        self.assertIsInstance(
            response["groups"][0]["items"][0]["venue"]["location"]["distance"],
            int,
        )
