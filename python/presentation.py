from display import prepare_display


def prepare_event(event, countdown):
    """
    Prepara los datos del evento para la capa de presentación.

    Combina:
    - datos originales del evento
    - datos calculados por countdown.py
    - valores preparados por display.py
    """

    display = prepare_display(
        title=event["title"],
        days_remaining=countdown["days_remaining"],
        progress=countdown["progress"],
        notes=event["notes"]
    )

    return {
        # ----------------------------------------------------
        # CORE DATA
        # ----------------------------------------------------

        "title": event["title"],
        "start_date": event["start_date"],
        "target_date": event["date"],
        "days_remaining": countdown["days_remaining"],
        "progress": countdown["progress"],

        # ----------------------------------------------------
        # EVENT DATA
        # ----------------------------------------------------

        "category": event["category"],
        "icon": event["icon"],
        "status": countdown["status"],
        "notes": event["notes"],

        # ----------------------------------------------------
        # DISPLAY DATA
        # ----------------------------------------------------

        "titleDisplay": display["titleDisplay"],
        "daysDisplay": display["daysDisplay"],
        "progressDisplay": display["progressDisplay"],
        "notesDisplay": display["notesDisplay"]
    }