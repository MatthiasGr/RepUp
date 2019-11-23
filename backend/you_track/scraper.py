from .api import Issue


def update_db(auth):
    raw = Issue.issues(auth)
    print()
    """
    The "root" function of this module.
    It will collect information on all issues on YouTrack, 
    """
    pass
