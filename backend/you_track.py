# This file contains a wrapper for a subset of the YouTrack API
# It contains just the functions we need

import requests


def api_call(auth, method, endpoint, payload):
    req = requests.request(method, endpoint)
    req.headers.update(
        Authorization=auth.get(),
        Accept="application/json, text/plain, */*",
        ContentType="application/json"
    )
    pass
