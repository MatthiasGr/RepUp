from .api import Issue
from db.helper import Insert, Query, Update


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
    issues = [x for x in issues if Query.isPending(x["id"])]
    for issue in issues:
        changes = Issue.changes(auth, issue["id"])
        print(changes)
        # Find resolved date
        resolved_ts = None
        try:
            container = next((x for x in reversed(changes["activities"]) if x["$type"] == "IssueResolvedActivityItem"))
            resolved_ts = container["timestamp"]
        except StopIteration:
            print("Should not happen")
            continue

        priority = "Normal"

        def check_for_prio(x):
            return x["$type"] == "CustomFieldActivityItem" and x["targetMember"] == "__CUSTOM_FIELD__Priority_1"
        try:
            custom_field = next((x for x in reversed(changes["activities"]) if check_for_prio(x)))
            priority = next((x["name"] for x in custom_field["added"]))
        except StopIteration:
            pass

        Update.close_pending(issue["id"], resolved_ts, priority)
    pass


def update_db(auth):
    raw = Issue.issues(auth)
    not_resolved = [x for x in raw if not x["resolved"]]

    resolved = [x for x in raw if x["resolved"]]

    add_pending_to_db(auth, not_resolved)
    sort_out_resolved_issues(auth, resolved)
