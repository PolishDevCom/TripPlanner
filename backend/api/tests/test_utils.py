"""Tests api/utils.py"""

from api.utils import get_api_key, get_secret_key


def test_get_api_key():
    """Tests get_api_key()"""
    test_api_key = get_api_key("FOURSQUARE_API_KEY")
    assert test_api_key is not None


def test_get_secret_key():
    """Tests get_secret_key()"""
    test_secret_key = get_secret_key("FOURSQUARE_API_SECRET")
    assert test_secret_key is not None
