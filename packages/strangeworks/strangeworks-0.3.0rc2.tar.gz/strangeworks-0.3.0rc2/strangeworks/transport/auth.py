"""auth.py."""
from urllib.parse import urljoin

import requests
from requests.exceptions import RequestException

from strangeworks.errors.error import StrangeworksError


def get_token(api_key: str, base_url: str) -> str:
    """Obtain a bearer token using an API key."""
    auth_url = urljoin(base_url, "users/token")
    try:
        res = requests.post(auth_url, json={"key": api_key})
        if res.status_code != 200:
            raise StrangeworksError.authentication_error(
                message="Unable to exchange api key for bearer token"
            )
        payload = res.json()
        auth_token = payload.get("accessToken")
        return auth_token

    except RequestException:
        raise StrangeworksError.authentication_error()(
            message="Unable to obtain bearer token using api key."
        )
