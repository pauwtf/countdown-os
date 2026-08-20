# ============================================================
# COUNTDOWN OS — LAYOUT ENGINE
# Version: 1.2 Elegance
# ============================================================

"""
Layout Engine de Countdown OS.

Responsabilidades:
- Resolver posiciones parent-relative.
- Normalizar progress.
- Calcular la posición dinámica del Plane.
- Construir la jerarquía de layout correspondiente a KWGT.
- Mantener separados datos, geometría y presentación.
"""


# ============================================================
# CANVAS
# ============================================================

CANVAS = {
    "width": 400,
    "height": 200,
    "anchor": "center"
}


# ============================================================
# STATIC LAYOUT TOKENS
# ============================================================

BACKGROUND = {
    "x": 0,
    "y": 0,
    "width": 400,
    "height": 200
}


COVER = {
    "x": -300,
    "y": 0,

    "image": {
        "x": 0,
        "y": 0,

        "text": {
            "x": 0,
            "y": 0,
            "font_size": 240,
            "value": "♡"
        }
    }
}


HEADER = {

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
}


GRADIENT = {

    "vertical": {
        "x": 0,
        "y": 0,
        "width": 400,
        "height": 200
    },

    "horizontal": {
        "x": 0,
        "y": 0,
        "width": 400,
        "height": 200
    }
}


COUNTER = {

    "x": 195,
    "y": -20,

    "days_remaining": {

        "x": 0,
        "y": 0,

        "font_size": 100
    }
}


CONTENT = {
    "x": 0,
    "y": 0
}


JOURNEY = {

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
        "travel": 520,
        "x_right": 275,
        "y": 93,
        "font_size": 30
    },

    "hearts": {

        "x": -245,
        "y": 100,

        "destination": {
            "x": 0,
            "y": 0,
            "font_size": 14
        },

        "arrival": {
            "x": 0,
            "y": 0,
            "font_size": 14
        }
    }
}


FOOTER = {
    "x": 200,
    "y": -125,
    "font_size": 10
}


TEST = {
    "x": 0,
    "y": 0,
    "font_size": 10
}


# ============================================================
# POSITION RESOLUTION
# ============================================================

def resolve_position(
    parent_position,
    local_position
):
    """
    Resuelve una posición relativa al parent.

    Fórmula:

        absolute = parent + local
    """

    parent_x, parent_y = parent_position
    local_x, local_y = local_position

    try:
        parent_x = float(parent_x)
        parent_y = float(parent_y)

        local_x = float(local_x)
        local_y = float(local_y)

    except (
        TypeError,
        ValueError
    ) as error:

        raise TypeError(
            "Layout coordinates must be numeric. "
            f"parent={parent_position}, "
            f"local={local_position}"
        ) from error

    return {
        "x": parent_x + local_x,
        "y": parent_y + local_y
    }


# ============================================================
# PROGRESS
# ============================================================

def normalize_progress(progress):
    """
    Normaliza progress al rango 0 → 1.
    """

    if progress is None:
        return 0.0

    try:
        progress = float(progress)

    except (
        TypeError,
        ValueError
    ) as error:

        raise TypeError(
            f"Progress must be numeric: {progress}"
        ) from error

    return max(
        0.0,
        min(progress, 1.0)
    )


# ============================================================
# PLANE POSITION
# ============================================================

def resolve_plane_position(progress):
    """
    Convierte progress en posición horizontal
    del Plane.

    travel = 520

    progress = 0
        → X Left = 0

    progress = 0.5
        → X Left = 260

    progress = 1
        → X Left = 520
    """

    progress = normalize_progress(
        progress
    )

    return {
        "x_left": (
            JOURNEY["plane"]["travel"]
            * progress
        ),

        "x_right": (
            JOURNEY["plane"]["x_right"]
        ),

        "y": (
            JOURNEY["plane"]["y"]
        )
    }


# ============================================================
# BUILD LAYOUT
# ============================================================

def build_layout(event):
    """
    Construye el Layout Contract interno.

    La estructura producida aquí corresponde
    directamente con la jerarquía real de KWGT.
    """

    # ========================================================
    # ROOT
    # ========================================================

    layout = {

        "canvas": {
            "width": CANVAS["width"],
            "height": CANVAS["height"],
            "anchor": CANVAS["anchor"]
        },

        "components": {}
    }


    # ========================================================
    # BACKGROUND
    # ========================================================

    layout["components"]["Background"] = {

        "position": {
            "x": BACKGROUND["x"],
            "y": BACKGROUND["y"]
        },

        "Background_shape": {

            "position": {
                "x": 0,
                "y": 0
            },

            "BackgroundShape": {

                "type": "rectangle",

                "width": (
                    BACKGROUND["width"]
                ),

                "height": (
                    BACKGROUND["height"]
                )
            }
        }
    }


    # ========================================================
    # COVER
    # ========================================================

    layout["components"]["Cover"] = {

        "position": {
            "x": COVER["x"],
            "y": COVER["y"]
        },

        "coverImage": {

            "position": {
                "x": COVER["image"]["x"],
                "y": COVER["image"]["y"]
            },

            "coverText": {

                "position": {
                    "x": (
                        COVER["image"]["text"]["x"]
                    ),

                    "y": (
                        COVER["image"]["text"]["y"]
                    )
                },

                "font_size": (
                    COVER["image"]["text"]
                    ["font_size"]
                ),

                "value": (
                    COVER["image"]["text"]
                    ["value"]
                )
            }
        }
    }


    # ========================================================
    # HEADER
    # ========================================================

    layout["components"]["Header"] = {

        "Title": {

            "position": {
                "x": HEADER["title"]["x"],
                "y": HEADER["title"]["y"]
            },

            "TitleText": {

                "font_size": (
                    HEADER["title"]
                    ["font_size"]
                ),

                "value": event.get(
                    "titleDisplay",
                    ""
                )
            }
        },

        "Days": {

            "position": {
                "x": HEADER["days"]["x"],
                "y": HEADER["days"]["y"]
            },

            "DaysText": {

                "font_size": (
                    HEADER["days"]
                    ["font_size"]
                ),

                "value": "days"
            }
        }
    }


    # ========================================================
    # GRADIENT
    # ========================================================

    layout["components"]["Gradient"] = {

        "Vertical": {

            "position": {
                "x": GRADIENT["vertical"]["x"],
                "y": GRADIENT["vertical"]["y"]
            },

            "GradientVerticalShape": {

                "type": "rectangle",

                "width": (
                    GRADIENT["vertical"]["width"]
                ),

                "height": (
                    GRADIENT["vertical"]["height"]
                )
            }
        },

        "Horizontal": {

            "position": {
                "x": GRADIENT["horizontal"]["x"],
                "y": GRADIENT["horizontal"]["y"]
            },

            "GradientHorizontalShape": {

                "type": "rectangle",

                "width": (
                    GRADIENT["horizontal"]["width"]
                ),

                "height": (
                    GRADIENT["horizontal"]["height"]
                )
            }
        }
    }


    # ========================================================
    # COUNTER
    # ========================================================

    counter_position = {
        "x": COUNTER["x"],
        "y": COUNTER["y"]
    }


    layout["components"]["Counter"] = {

        "position": counter_position,

        "DaysRemaining": {

            "position": {
                "x": COUNTER["days_remaining"]["x"],
                "y": COUNTER["days_remaining"]["y"]
            },

            "DaysRemainingText": {

                "font_size": (
                    COUNTER["days_remaining"]
                    ["font_size"]
                ),

                "value": event.get(
                    "daysDisplay",
                    ""
                )
            }
        }
    }


    # ========================================================
    # CONTENT
    # ========================================================

    content_position = {
        "x": CONTENT["x"],
        "y": CONTENT["y"]
    }


    # ========================================================
    # JOURNEY
    # ========================================================

    journey_position = resolve_position(

        (
            content_position["x"],
            content_position["y"]
        ),

        (
            JOURNEY["x"],
            JOURNEY["y"]
        )
    )


    # ========================================================
    # LINE
    # ========================================================

    line_position = resolve_position(

        (
            journey_position["x"],
            journey_position["y"]
        ),

        (
            JOURNEY["line"]["x"],
            JOURNEY["line"]["y"]
        )
    )


    # ========================================================
    # ORIGIN
    # ========================================================

    origin_position = resolve_position(

        (
            journey_position["x"],
            journey_position["y"]
        ),

        (
            JOURNEY["origin"]["x"],
            JOURNEY["origin"]["y"]
        )
    )


    # ========================================================
    # HEARTS
    # ========================================================

    hearts_position = resolve_position(

        (
            journey_position["x"],
            journey_position["y"]
        ),

        (
            JOURNEY["hearts"]["x"],
            JOURNEY["hearts"]["y"]
        )
    )


    # ========================================================
    # PLANE
    # ========================================================

    plane_position = resolve_plane_position(
        event.get("progress")
    )


    # ========================================================
    # JOURNEY TREE
    # ========================================================

    journey = {

        "position": journey_position,

        "Line": {

            "position": line_position,

            "JourneyLineShape": {

                "type": "rectangle",

                "width": (
                    JOURNEY["line"]["width"]
                ),

                "height": (
                    JOURNEY["line"]["height"]
                )
            }
        },

        "Origin": {

            "position": origin_position,

            "OriginShape": {

                "type": "circle",

                "size": (
                    JOURNEY["origin"]["size"]
                )
            }
        },

        "Plane": {

            "x_left": (
                plane_position["x_left"]
            ),

            "x_right": (
                plane_position["x_right"]
            ),

            "y": (
                plane_position["y"]
            ),

            "PlaneText": {

                "font_size": (
                    JOURNEY["plane"]["font_size"]
                ),

                "value": "✈"
            }
        },

        "Hearts": {

            "position": hearts_position,

            "Destination": {

                "position": {
                    "x": (
                        JOURNEY["hearts"]
                        ["destination"]["x"]
                    ),

                    "y": (
                        JOURNEY["hearts"]
                        ["destination"]["y"]
                    )
                },

                "DestinationText": {

                    "font_size": (
                        JOURNEY["hearts"]
                        ["destination"]
                        ["font_size"]
                    ),

                    "value": ""
                }
            },

            "Arrival": {

                "position": {
                    "x": (
                        JOURNEY["hearts"]
                        ["arrival"]["x"]
                    ),

                    "y": (
                        JOURNEY["hearts"]
                        ["arrival"]["y"]
                    )
                },

                "ArrivalText": {

                    "font_size": (
                        JOURNEY["hearts"]
                        ["arrival"]
                        ["font_size"]
                    ),

                    "value": ""
                }
            }
        }
    }


    layout["components"]["Content"] = {

        "position": content_position,

        "journey": journey
    }


    # ========================================================
    # FOOTER
    # ========================================================

    layout["components"]["Footer"] = {

        "position": {

            "x": FOOTER["x"],
            "y": FOOTER["y"]
        },

        "FooterText": {

            "font_size": (
                FOOTER["font_size"]
            ),

            "value": event.get(
                "notesDisplay",
                ""
            )
        }
    }


    # ========================================================
    # TEST
    # ========================================================

    layout["components"]["test"] = {

        "TestText": {

            "font_size": (
                TEST["font_size"]
            ),

            "value": ""
        }
    }


    # ========================================================
    # RETURN
    # ========================================================

    return layout