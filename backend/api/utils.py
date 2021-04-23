"""Retrieves and returns applications keys."""

import json


def get_api_key(key: str) -> str:
    """
    Retrieves and returns an API key

    Args:
        key (str): Key name for API key saved in file.

    Returns:
        str: API key
    """
    with open(r"api\secrets\api_keys.json") as api_keys:
        return json.loads(api_keys.read()).get(key)


def get_secret_key(key: str) -> str:
    """
    Retrieves and returns secret key

    Args:
        key (str): Key name for secret key saved in file.

    Returns:
        str: Secret key
    """
    with open(r"api\secrets\secret.json") as secret:
        return json.loads(secret.read()).get(key)
