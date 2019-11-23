
class YouTrackAuthorization(object):
    def __init__(self, token):
        self.token = YouTrackAuthorization.refresh_authorization_impl(token)

    @staticmethod
    def refresh_authorization_impl(token):
        return token

    def refresh_authorization(self):
        return YouTrackAuthorization.refresh_authorization_impl(self.token)

    def get(self):
        return self.token
