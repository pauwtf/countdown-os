def format_title(title):
    """
    Prepara el título para su presentación visual.

    Por ahora conserva el título original.
    La lógica de división de líneas podrá evolucionar
    posteriormente según las necesidades del widget.
    """

    if not title:
        return ""

    return title.strip()


def format_days(days_remaining):
    """
    Prepara los días restantes para su presentación.
    """

    if days_remaining is None:
        return ""

    return str(days_remaining)


def format_progress(progress):
    """
    Prepara el progreso para su presentación visual.

    Recibe un valor normalizado entre 0 y 1
    y devuelve un porcentaje entero.
    """

    if progress is None:
        return ""

    percentage = round(progress * 100)

    return f"{percentage}%"


def format_notes(notes):
    """
    Prepara las notas para el footer.
    """

    if not notes:
        return ""

    return notes.strip()


def prepare_display(event, countdown):
    """
    Genera los valores preparados para presentación visual.
    """

    return {
        "titleDisplay": format_title(event["title"]),
        "daysDisplay": format_days(
            countdown["days_remaining"]
        ),
        "progressDisplay": format_progress(
            countdown["progress"]
        ),
        "notesDisplay": format_notes(
            event["notes"]
        )
    }