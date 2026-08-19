from copy import deepcopy


# ============================================================
# CANVAS
# ============================================================

CANVAS = {
    "width": 400,
    "height": 200,
    "anchor": "center"
}


# ============================================================
# LAYOUT TOKENS
# ============================================================

LAYOUT_TOKENS = {
    "header": {
        "title": {
            "x": 175,
            "y": -125,
            "font_size": 18
        },
        "days": {
            "x": 50,
            "y": 21,
            "font_size": 15
        }
    },

    "counter": {
        "x": 195,
        "y": -20,
        "days": {
            "x": 0,
            "y": 0,
            "font_size": 100
        }
    },

    "journey": {
        "x": 0,
        "y": 0,

        "line": {
            "x": 20,
            "y": 100,
            "width": 258,
            "height": 1
        },

        "origin": {
            "x": 275,
            "y": 100,
            "size": 5
        },

        "plane": {
            "x_right": 275,
            "y": 93,
            "travel": 520,
            "font_size": 30
        },

        "hearts": {
            "x": -245,
            "y": 100
        }
    },

    "footer": {
        "x": 200,
        "y": -125,
        "font_size": 10
    },

    "cover": {
        "x": -300,
        "font_size": 240
    }
}


# ============================================================
# POSITION RESOLUTION
# ============================================================

def resolve_position(parent_position, local_position):
    """
    Resuelve la posición absoluta de un elemento
    a partir de la posición de su padre y su offset local.
    """

    parent_x, parent_y = parent_position
    local_x, local_y = local_position

    return {
        "x": parent_x + local_x,
        "y": parent_y + local_y
    }


# ============================================================
# PLANE POSITION
# ============================================================

def resolve_plane_position(progress):
    """
    Convierte progress (0 → 1) en una posición X
    para el Plane.
    """

    if progress is None:
        progress = 0

    progress = max(0, min(progress, 1))

    travel = LAYOUT_TOKENS["journey"]["plane"]["travel"]

    return {
        "x_left": travel * progress,
        "x_right": LAYOUT_TOKENS["journey"]["plane"]["x_right"],
        "y": LAYOUT_TOKENS["journey"]["plane"]["y"]
    }


# ============================================================
# BUILD LAYOUT
# ============================================================

def build_layout(event):
    """
    Construye la geometría resuelta del widget.

    Recibe datos preparados por Presentation/Display.
    """

    layout = {
        "canvas": deepcopy(CANVAS),
        "components": {}
    }

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    layout["components"]["header"] = {
        "title": {
            "position": {
                "x": LAYOUT_TOKENS["header"]["title"]["x"],
                "y": LAYOUT_TOKENS["header"]["title"]["y"]
            },
            "font_size": LAYOUT_TOKENS["header"]["title"]["font_size"],
            "text": event.get("titleDisplay", "")
        },

        "days": {
            "position": {
                "x": LAYOUT_TOKENS["header"]["days"]["x"],
                "y": LAYOUT_TOKENS["header"]["days"]["y"]
            },
            "font_size": LAYOUT_TOKENS["header"]["days"]["font_size"],
            "text": "days"
        }
    }

    # --------------------------------------------------------
    # COUNTER
    # --------------------------------------------------------

    counter_position = {
        "x": LAYOUT_TOKENS["counter"]["x"],
        "y": LAYOUT_TOKENS["counter"]["y"]
    }

    layout["components"]["counter"] = {
        "position": counter_position,
        "days": {
            "position": {
                "x": counter_position["x"],
                "y": counter_position["y"]
            },
            "font_size": LAYOUT_TOKENS["counter"]["days"]["font_size"],
            "text": event.get("daysDisplay", "")
        }
    }

    # --------------------------------------------------------
    # JOURNEY
    # --------------------------------------------------------

    journey_position = {
        "x": LAYOUT_TOKENS["journey"]["x"],
        "y": LAYOUT_TOKENS["journey"]["y"]
    }

    line = LAYOUT_TOKENS["journey"]["line"]

    origin = LAYOUT_TOKENS["journey"]["origin"]

    hearts = LAYOUT_TOKENS["journey"]["hearts"]

    layout["components"]["journey"] = {
        "position": journey_position,

        "line": {
            "position": resolve_position(
                journey_position,
                (line["x"], line["y"])
            ),
            "width": line["width"],
            "height": line["height"]
        },

        "origin": {
            "position": resolve_position(
                journey_position,
                (origin["x"], origin["y"])
            ),
            "size": origin["size"]
        },

        "plane": resolve_plane_position(
            event.get("progress")
        ),

        "hearts": {
            "position": resolve_position(
                journey_position,
                (hearts["x"], hearts["y"])
            ),

            "destination": {
                "position": {
                    "x": resolve_position(
                        journey_position,
                        (hearts["x"], hearts["y"])
                    )["x"],
                    "y": resolve_position(
                        journey_position,
                        (hearts["x"], hearts["y"])
                    )["y"]
                }
            }
        }
    }

    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    layout["components"]["footer"] = {
        "position": {
            "x": LAYOUT_TOKENS["footer"]["x"],
            "y": LAYOUT_TOKENS["footer"]["y"]
        },
        "font_size": LAYOUT_TOKENS["footer"]["font_size"],
        "text": event.get("notesDisplay", "")
    }

    # --------------------------------------------------------
    # COVER
    # --------------------------------------------------------

    layout["components"]["cover"] = {
        "position": {
            "x": LAYOUT_TOKENS["cover"]["x"],
            "y": 0
        },
        "font_size": LAYOUT_TOKENS["cover"]["font_size"]
    }

    return layout