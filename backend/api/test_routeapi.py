import pytest
import json
from .routeapi import RouteApiRequest


successful_respone = {"type": "FeatureCollection", "features": [{"bbox": [8.681436, 49.41461, 8.69198, 49.420514], "type":"Feature", "properties":{"segments": [{"distance": 1600.0, "duration": 265.0, "steps": [{"distance": 312.6, "duration": 75.0, "type": 11, "instruction": "Head north on Wielandtstraße", "name": "Wielandtstraße", "way_points": [0, 10]}, {"distance": 737.1, "duration": 106.1, "type": 1, "instruction": "Turn right onto Mönchhofstraße", "name": "Mönchhofstraße", "way_points": [10, 38]}, {"distance": 264.3, "duration": 38.5, "type": 0, "instruction": "Turn left onto Handschuhsheimer Landstraße, B 3", "name": "Handschuhsheimer Landstraße, B 3", "way_points": [38, 54]}, {"distance": 155.3, "duration": 14.0, "type": 5, "instruction": "Turn slight right onto Handschuhsheimer Landstraße, B 3", "name": "Handschuhsheimer Landstraße, B 3", "way_points": [54, 58]}, {"distance": 130.8, "duration": 31.4, "type": 0, "instruction": "Turn left onto Roonstraße", "name": "Roonstraße", "way_points": [58, 61]}, {"distance": 0.0, "duration": 0.0, "type": 10, "instruction": "Arrive at Roonstraße, straight ahead", "name": "-", "way_points": [61, 61]}]}], "summary":{"distance": 1600.0, "duration": 265.0}, "way_points": [0, 61]}, "geometry":{"coordinates": [[8.681496, 49.41461], [8.68149, 49.414711], [8.681441, 49.415655], [8.681436, 49.415747], [8.681455, 49.415835], [8.681509, 49.416087], [8.681642, 49.416498], [8.681671, 49.416588], [8.681701, 49.416684], [8.681875, 49.417287], [8.68189, 49.417394], [8.682045, 49.41739], [8.682107, 49.41739], [
    8.682461, 49.417389], [8.682563, 49.417388], [8.682676, 49.417387], [8.682782, 49.417388], [8.683371, 49.417368], [8.683592, 49.41736], [8.683763, 49.417362], [8.685222, 49.417366], [8.685359, 49.417364], [8.685511, 49.417366], [8.685713, 49.41737], [8.686395, 49.417364], [8.686722, 49.41737], [8.687335, 49.417352], [8.687474, 49.417348], [8.687598, 49.41735], [8.688256, 49.417361], [8.688813, 49.417381], [8.690001, 49.417413], [8.690227, 49.417428], [8.690338, 49.41743], [8.690482, 49.417401], [8.691467, 49.417155], [8.691735, 49.417102], [8.691957, 49.417117], [8.69198, 49.417121], [8.691941, 49.41722], [8.691817, 49.417369], [8.691427, 49.417726], [8.691072, 49.418051], [8.690968, 49.418158], [8.690936, 49.418188], [8.690939, 49.418208], [8.690939, 49.418296], [8.69092, 49.418378], [8.690912, 49.418411], [8.69067, 49.418981], [8.690664, 49.418992], [8.690614, 49.419093], [8.690547, 49.419174], [8.690479, 49.419204], [8.690446, 49.419218], [8.690275, 49.419577], [8.690123, 49.419833], [8.689854, 49.420216], [8.689652, 49.420514], [8.68963, 49.42051], [8.688601, 49.420393], [8.687872, 49.420318]], "type":"LineString"}}], "bbox": [8.681436, 49.41461, 8.69198, 49.420514], "metadata": {"attribution": "openrouteservice.org | OpenStreetMap contributors", "service": "routing", "timestamp": 1614100756243, "query": {"coordinates": [[8.681495, 49.41461], [8.687872, 49.420318]], "profile": "driving-car", "format": "json"}, "engine": {"version": "6.3.6", "build_date": "2021-02-21T01:31:06Z", "graph_date": "1970-01-01T00:00:00Z"}}}
error_response = {"error": {"code": 2004, "message": "Request parameters exceed the server configuration limits. The approximated route distance must not be greater than 6000000.0 meters."}, "info": {
    "engine": {"version": "6.3.6", "build_date": "2021-02-21T01:31:06Z"}, "timestamp": 1614100819473}}

good_object = RouteApiRequest(8.681495, 49.41461, 8.687872, 49.420318)
bad_object = RouteApiRequest(200, 200, 200, 200)


def test1_get_coordinates():
    r = RouteApiRequest.get_coordinates(successful_respone, True)
    assert r == [[8.681496, 49.41461], [8.68149, 49.414711], [8.681441, 49.415655], [8.681436, 49.415747], [8.681455, 49.415835], [8.681509, 49.416087], [8.681642, 49.416498], [8.681671, 49.416588], [8.681701, 49.416684], [8.681875, 49.417287], [8.68189, 49.417394], [8.682045, 49.41739], [8.682107, 49.41739], [8.682461, 49.417389], [8.682563, 49.417388], [8.682676, 49.417387], [8.682782, 49.417388], [8.683371, 49.417368], [8.683592, 49.41736], [8.683763, 49.417362], [8.685222, 49.417366], [8.685359, 49.417364], [8.685511, 49.417366], [8.685713, 49.41737], [8.686395, 49.417364], [8.686722, 49.41737], [8.687335, 49.417352], [8.687474, 49.417348], [8.687598, 49.41735], [8.688256, 49.417361], [8.688813, 49.417381], [
        8.690001, 49.417413], [8.690227, 49.417428], [8.690338, 49.41743], [8.690482, 49.417401], [8.691467, 49.417155], [8.691735, 49.417102], [8.691957, 49.417117], [8.69198, 49.417121], [8.691941, 49.41722], [8.691817, 49.417369], [8.691427, 49.417726], [8.691072, 49.418051], [8.690968, 49.418158], [8.690936, 49.418188], [8.690939, 49.418208], [8.690939, 49.418296], [8.69092, 49.418378], [8.690912, 49.418411], [8.69067, 49.418981], [8.690664, 49.418992], [8.690614, 49.419093], [8.690547, 49.419174], [8.690479, 49.419204], [8.690446, 49.419218], [8.690275, 49.419577], [8.690123, 49.419833], [8.689854, 49.420216], [8.689652, 49.420514], [8.68963, 49.42051], [8.688601, 49.420393], [8.687872, 49.420318]]


def test1_get_distance():
    r = RouteApiRequest.get_distance(successful_respone, True)
    assert r == 1600.0


def test2_get_coordinates():
    r = RouteApiRequest.get_coordinates(successful_respone, False)
    assert r == False


def test2_get_distance():
    r = RouteApiRequest.get_distance(successful_respone, False)
    assert r == False


def test1_obtain_api_key():
    try:
        with open("api_keys.json") as api_keys:
            assert good_object.api_key == json.loads(
                api_keys.read()).get("ROUTE_API_KEY")
    except:
        assert good_object.api_key == False


def test1_request_external_api():
    r = good_object.request_external_api()
    if good_object.api_key_valid:
        assert (type(r) == dict) == ("error" not in r)
    else:
        assert "error" in r


def test2_request_external_api():
    r = bad_object.request_external_api()
    assert "error" in r


def test1_is_reply_success():
    r = good_object.is_reply_success()
    assert r == True


def test2_is_reply_success():
    r = bad_object.is_reply_success()
    assert r == False
