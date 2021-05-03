"""Api's utils module"""

import os

import dotenv


def get_key(key: str) -> str:
    """Retrieves and returns keys from .env file."""
    dotenv.load_dotenv()
    return os.getenv(key)
