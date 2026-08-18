def parse_event(event):
    """
    Convierte un evento de la API de Notion
    en el modelo interno de Countdown OS.
    """

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

        # ----------------------------------------------------
        # BASIC DATA
        # ----------------------------------------------------

        "title": (
            title[0]["plain_text"]
            if title
            else ""
        ),

        "date": (
            date["start"]
            if date
            else None
        ),

        "start_date": (
            start_date["start"]
            if start_date
            else None
        ),

        # ----------------------------------------------------
        # EVENT METADATA
        # ----------------------------------------------------

        "category": (
            category["name"]
            if category
            else None
        ),

        "icon": (
            icon["name"]
            if icon
            else ""
        ),

        # ----------------------------------------------------
        # STATE
        # ----------------------------------------------------

        "active": active,
        "visible": visible,

        # ----------------------------------------------------
        # CONFIGURATION
        # ----------------------------------------------------

        "repeat": (
            repeat["name"]
            if repeat
            else None
        ),

        "priority": (
            priority["name"]
            if priority
            else None
        ),

        # ----------------------------------------------------
        # NOTES
        # ----------------------------------------------------

        "notes": (
            notes[0]["plain_text"]
            if notes
            else ""
        )
    }


def parse_events(events):
    """
    Convierte una lista de eventos de Notion
    en una lista de eventos internos.
    """

    return [
        parse_event(event)
        for event in events
    ]