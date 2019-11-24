from .api import Issue
from db.helper import Insert


def get_timestamp_for_assignment(auth, issue_id):
    raw = Issue.changes(auth, issue_id)
    activities = raw["activities"]
    target_field = next((x for x in activities
          if x["$type"] == "CustomFieldActivityItem"
          and x["targetMember"] == "__CUSTOM_FIELD__Assignee_4"))

    if target_field is None:
        return None

    added = target_field["added"] if "added" in target_field else None
    if added is None:
        return None

    return target_field["timestamp"]


def add_pending_to_db(auth, issues):
    for issue in issues:
        issue_id = issue["id"]

        def has_user_condition(x):
            custom_field = x["projectCustomField"] if "projectCustomField" in x else None
            if custom_field is None:
                return False

            field = custom_field["field"]
            value = x["value"]
            return field["name"] == "Assignee" and value is not None

        try:
            user_id_container = next((x for x in issue["fields"] if has_user_condition(x)))
        except StopIteration:
            continue
        user_id = user_id_container["value"]["id"]

        timestamp = get_timestamp_for_assignment(auth, issue_id)
        Insert.newPendingIssue(user_id, issue_id, timestamp)

def sort_out_resolved_issues(auth, issues):
    # TODO: Filter issues to those in the database
    # TODO: Extract resolve time
    # TODO: Calculate points
    # TODO: Update database
    pass


def update_db(auth):
    raw = Issue.issues(auth)
    not_resolved = [x for x in raw if not x["resolved"]]

    resolved = [x for x in raw if x["resolved"]]
    # TODO: Extract log for resolved data

    add_pending_to_db(auth, not_resolved)
    sort_out_resolved_issues(auth, resolved)
    """
    The "root" function of this module.
    It will collect information on all issues on YouTrack, 
    """
    pass
