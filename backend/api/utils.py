import json


def get_api_key(key):
    with open(r"api\secrets\api_keys.json") as api_keys:
        return json.loads(api_keys.read()).get(key)


def get_secret_key(key):
    with open(r"api\secrets\secret.json") as secret:
        return json.loads(secret.read()).get(key)
