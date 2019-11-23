# This file contains a wrapper for a subset of the YouTrack API
# It contains just the functions we need

import requests

STATUS_UNAUTHORIZED = 401


def api_call(auth, method, endpoint, payload, params=None):
    res = requests.request(
        method, endpoint,
        headers={
            "Authorization": auth.get(),
            "Accept": "application/json, text/plain, */*",
            "ContentType": "application/json"
        },
        json=payload,
        params=params
    )

    if res.status_code == STATUS_UNAUTHORIZED:
        # TODO: THIS MUST THROW!
        auth.refresh_authorization()
        # This cannot fail, right?
        api_call(auth, method, endpoint, payload, params)
    pass
