# This file contains a wrapper for a subset of the YouTrack API
# It contains just the functions we need

import requests
import json
from .auth import YouTrackAuthorization

STATUS_UNAUTHORIZED = 401
# FIXME: This should be injected
YOUTRACK_URL = "repup.myjetbrains.com/youtrack"


def api_call(auth, method, endpoint, payload=None, params=None):
    res = requests.request(
        method, endpoint,
        headers={
            "Authorization": "Bearer {}".format(auth.get()),
            "Accept": "application/json, text/plain, */*",
            "ContentType": "application/json"
        },
        json=payload,
        params=params
    )

    if res.status_code == STATUS_UNAUTHORIZED:
        print(res.text)
        raise Exception("OAuth is not implemented yet")
        # auth.refresh_authorization()
        # This cannot fail, right?
        # res = api_call(auth, method, endpoint, payload, params)

    if res.status_code < 200 or res.status_code >= 300:
        raise Exception("API Request failed: {}", res)
    return res


class User(object):
    @staticmethod
    def check_token(auth):
        status = api_call(auth, "GET", "https://{}/api/admin/users/me".format(YOUTRACK_URL)).status_code
        return 200 <= status < 300

    @staticmethod
    def info(auth, id):
        return api_call(auth, "GET", "https://{}/api/admin/users/{}".format(YOUTRACK_URL, id), params={"fields": "name"}).json()


class Issue(object):
    @staticmethod
    def changes(auth, id):
        return api_call(
            auth,
            "GET",
            "https://{}/api/issues/{}/activitiesPage".format(YOUTRACK_URL, id),
            params=[
                ("categories", "IssueCreatedCategory"),
                ("categories", "IssueResolvedCategory"),
                ("categories", "CustomFieldCategory"),
                ("fields", "activities(removed(id,name),added(id,name),timestamp,targetMember)")
            ]
        ).json()

    @staticmethod
    def issues(auth):
        return api_call(
            auth,
            "GET",
            "https://{}/api/issues".format(YOUTRACK_URL),
            params={"fields": "id,resolved,fields(projectCustomField(field(name)),value(name))"}
        ).json()
