def format_title(title):
    """
    Prepara un título para su presentación visual.
    """

    if not title:
        return ""

    return title.strip()


def format_days(days_remaining):
    """
    Prepara los días restantes para su presentación visual.
    """

    if days_remaining is None:
        return ""

    return str(days_remaining)


def format_progress(progress):
    """
    Convierte un progreso normalizado entre 0 y 1
    en un porcentaje entero para presentación.
    """

    if progress is None:
        return ""

    percentage = round(progress * 100)

    return f"{percentage}%"


def format_notes(notes):
    """
    Prepara las notas para su presentación en el Footer.
    """

    if not notes:
        return ""

    return notes.strip()


def prepare_display(
    title,
    days_remaining,
    progress,
    notes
):
    """
    Genera los valores preparados para presentación visual.

    Esta función no conoce el origen de los datos.
    Solo transforma valores para la capa de UI.
    """

    return {
        "titleDisplay": format_title(title),
        "daysDisplay": format_days(days_remaining),
        "progressDisplay": format_progress(progress),
        "notesDisplay": format_notes(notes)
    }