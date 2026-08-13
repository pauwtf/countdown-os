def prepare_event(event, countdown):
    """
    Prepara los datos del evento para la capa de presentación.

    Esta capa separa:
    - datos originales del evento
    - datos calculados por countdown.py
    - datos preparados para el JSON/UI
    """

    return {
        "title": event["title"],
        "start_date": countdown["start_date"],
        "target_date": countdown["target_date"],
        "days_remaining": countdown["days_remaining"],
        "progress": countdown["progress"],
        "category": event["category"],
        "icon": event["icon"],
        "status": countdown["status"],
        "notes": event["notes"]
    }