# ============================================================
# COUNTDOWN OS — LAYOUT ENGINE
# Version: 1.2 Elegance
# ============================================================

from layout_tokens import (
    CANVAS,
    HEADER,
    COUNTER,
    JOURNEY,
    FOOTER,
    COVER
)


# ============================================================
# POSITION RESOLUTION
# ============================================================

def resolve_position(parent_position, local_position):
    """
    Resuelve la posición de un elemento hijo.

    Child Position =
    Parent Position + Local Offset
    """

    parent_x, parent_y = parent_position
    local_x, local_y = local_position

    return {
        "x": parent_x + local_x,
        "y": parent_y + local_y
    }


# ============================================================
# PROGRESS NORMALIZATION
# ============================================================

def normalize_progress(progress):
    """
    Garantiza que progress esté entre 0 y 1.
    """

    if progress is None:
        return 0

    return max(0, min(progress, 1))


# ============================================================
# PLANE POSITION
# ============================================================

def resolve_plane_position(progress):
    """
    Convierte progress en posición horizontal del Plane.
    """

    progress = normalize_progress(progress)

    plane = JOURNEY["plane"]

    x_left = plane["travel"] * progress

    return {
        "x_left": x_left,
        "x_right": plane["x_right"],
        "y": plane["y"]
    }


# ============================================================
# LAYOUT BUILDER
# ============================================================

def build_layout(event):
    """
    Construye la geometría resuelta de Countdown OS.

    Recibe datos preparados por Presentation/Display.
    """

    layout = {
        "canvas": {
            "width": CANVAS["width"],
            "height": CANVAS["height"],
            "anchor": CANVAS["anchor"]
        },

        "components": {}
    }

    # ========================================================
    # HEADER
    # ========================================================

    layout["components"]["header"] = {

        "title": {
            "position": {
                "x": HEADER["title"]["x"],
                "y": HEADER["title"]["y"]
            },

            "font_size": HEADER["title"]["font_size"],

            "text": event.get(
                "titleDisplay",
                ""
            )
        },

        "days": {
            "position": {
                "x": HEADER["days"]["x"],
                "y": HEADER["days"]["y"]
            },

            "font_size": HEADER["days"]["font_size"],

            "text": "days"
        }
    }

    # ========================================================
    # COUNTER
    # ========================================================

    counter_position = {
        "x": COUNTER["x"],
        "y": COUNTER["y"]
    }

    days_position = resolve_position(
        counter_position,
        (
            COUNTER["days"]["x"],
            COUNTER["days"]["y"]
        )
    )

    layout["components"]["counter"] = {

        "position": counter_position,

        "days": {
            "position": days_position,

            "font_size": COUNTER["days"]["font_size"],

            "text": event.get(
                "daysDisplay",
                ""
            )
        }
    }

    # ========================================================
    # JOURNEY
    # ========================================================

    journey_position = {
        "x": JOURNEY["x"],
        "y": JOURNEY["y"]
    }

    line = JOURNEY["line"]

    origin = JOURNEY["origin"]

    hearts = JOURNEY["hearts"]

    line_position = resolve_position(
        journey_position,
        (
            line["x"],
            line["y"]
        )
    )

    origin_position = resolve_position(
        journey_position,
        (
            origin["x"],
            origin["y"]
        )
    )

    hearts_position = resolve_position(
        journey_position,
        (
            hearts["x"],
            hearts["y"]
        )
    )

    destination_position = resolve_position(
        hearts_position,
        (0, 0)
    )

    arrival_position = resolve_position(
        hearts_position,
        (0, 0)
    )

    layout["components"]["journey"] = {

        "position": journey_position,

        "line": {
            "position": line_position,
            "width": line["width"],
            "height": line["height"]
        },

        "origin": {
            "position": origin_position,
            "size": origin["size"]
        },

        "plane": resolve_plane_position(
            event.get("progress")
        ),

        "hearts": {
            "position": hearts_position,

            "destination": {
                "position": destination_position
            },

            "arrival": {
                "position": arrival_position
            }
        }
    }

    # ========================================================
    # FOOTER
    # ========================================================

    layout["components"]["footer"] = {

        "position": {
            "x": FOOTER["x"],
            "y": FOOTER["y"]
        },

        "font_size": FOOTER["font_size"],

        "text": event.get(
            "notesDisplay",
            ""
        )
    }

    # ========================================================
    # COVER
    # ========================================================

    layout["components"]["cover"] = {

        "position": {
            "x": COVER["x"],
            "y": 0
        },

        "font_size": COVER["font_size"]
    }

    return layout