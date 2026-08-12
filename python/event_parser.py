def parse_event(event):
    properties = event["properties"]

    title = properties["Event"]["title"]
    date = properties["Date"]["date"]
    start_date = properties["Start Date"]["date"]
    category = properties["Category"]["select"]
    icon = properties["Icon"]["select"]
    active = properties["Active"]["checkbox"]
    visible = properties["Visible"]["checkbox"]
    repeat = properties["Repeat"]["select"]
    priority = properties["Priority"]["select"]
    notes = properties["Notes"]["rich_text"]

    return {
        "id": event["id"],
        "title": title[0]["plain_text"] if title else "",
        "date": date["start"] if date else None,
        "start_date": start_date["start"] if start_date else None,
        "category": category["name"] if category else None,
        "icon": icon["name"] if icon else "",
        "active": active,
        "visible": visible,
        "repeat": repeat["name"] if repeat else None,
        "priority": priority["name"] if priority else None,
        "notes": notes[0]["plain_text"] if notes else ""
    }


def parse_events(events):
    return [parse_event(event) for event in events]