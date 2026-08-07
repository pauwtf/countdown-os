from datetime import date


def calculate_countdown(event):
    target_date = date.fromisoformat(event["date"])
    today = date.today()

    days_remaining = (target_date - today).days

    return {
        "title": event["title"],
        "target_date": event["date"],
        "days_remaining": days_remaining
    }


def get_active_event(events):
    active_events = [event for event in events if event["active"]]

    if not active_events:
        return None

    return active_events[0]
