
class YouTrackAuthorization(object):
    def __init__(self, token):
        self.token = token
        self.cookie = YouTrackAuthorization.refresh_authorization_impl(token)

    @staticmethod
    def refresh_authorization_impl(token):
        pass

    def refresh_authorization(self):
        return YouTrackAuthorization.refresh_authorization_impl(self.token)

    def get(self):
        return self.cookie
