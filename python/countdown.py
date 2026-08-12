from datetime import date


# ============================================================
# ICON SYSTEM
# ============================================================

ICON_MAP = {
    "birthday": "🎂",
    "flight": "●",
    "landing": "●",
    "christmas": "🎄",
    "love": "♡"
}


def get_icon(category):
    """
    Returns the icon associated with an event category.
    """

    return ICON_MAP.get(category, "•")


# ============================================================
# EVENT SELECTION
# ============================================================

def get_active_event(events):
    active_events = [
        event for event in events
        if event["active"]
    ]

    if not active_events:
        return None

    return active_events[0]


# ============================================================
# COUNTDOWN ENGINE
# ============================================================

def calculate_countdown(event):
    today = date.today()

    target_date = date.fromisoformat(event["date"])

    days_remaining = (target_date - today).days

    # --------------------------------------------------------
    # PROGRESS
    # --------------------------------------------------------

    progress = None

    if event["start_date"]:
        start_date = date.fromisoformat(event["start_date"])

        total_duration = (target_date - start_date).days
        elapsed = (today - start_date).days

        if total_duration > 0:
            progress = elapsed / total_duration
            progress = max(0, min(progress, 1))

    # --------------------------------------------------------
    # STATUS
    # --------------------------------------------------------

    if days_remaining > 0:
        status = "ACTIVE"
    else:
        status = "COMPLETED"

    # --------------------------------------------------------
    # ICON
    # --------------------------------------------------------

    icon = get_icon(event["category"])

    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    return {
        "title": event["title"],
        "start_date": event["start_date"],
        "target_date": event["date"],
        "days_remaining": days_remaining,
        "progress": progress,
        "category": event["category"],
        "icon": icon,
        "status": status,
        "notes": event["notes"]
    }