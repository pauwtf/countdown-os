# ============================================================
# COUNTDOWN OS — LAYOUT ENGINE
# Version: 1.2 Elegance
# ============================================================

from layout_tokens import (
    CANVAS,
    BACKGROUND,
    COVER,
    HEADER,
    GRADIENT,
    COUNTER,
    CONTENT,
    JOURNEY,
    FOOTER,
    TEST
)


# ============================================================
# POSITION RESOLUTION
# ============================================================

def resolve_position(parent_position, local_position):
    """
    Resuelve una posición parent-relative.

    absolute = parent + local
    """

    parent_x, parent_y = parent_position
    local_x, local_y = local_position

    try:
        parent_x = float(parent_x)
        parent_y = float(parent_y)
        local_x = float(local_x)
        local_y = float(local_y)

    except (TypeError, ValueError) as error:

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

    if progress is None:
        return 0.0

    try:
        progress = float(progress)

    except (TypeError, ValueError) as error:

        raise TypeError(
            f"Progress must be numeric: {progress}"
        ) from error

    return max(
        0.0,
        min(progress, 1.0)
    )


# ============================================================
# PLANE
# ============================================================

def resolve_plane_position(progress):

    progress = normalize_progress(progress)

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
                "width": BACKGROUND["width"],
                "height": BACKGROUND["height"]
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
                    "x": COVER["image"]["text"]["x"],
                    "y": COVER["image"]["text"]["y"]
                },

                "font_size": (
                    COVER["image"]["text"]["font_size"]
                ),

                "value": (
                    COVER["image"]["text"]["value"]
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

                "font_size": HEADER["title"]["font_size"],

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

                "font_size": HEADER["days"]["font_size"],

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
                "width": GRADIENT["vertical"]["width"],
                "height": GRADIENT["vertical"]["height"]
            }
        },

        "Horizontal": {

            "position": {
                "x": GRADIENT["horizontal"]["x"],
                "y": GRADIENT["horizontal"]["y"]
            },

            "GradientHorizontalShape": {

                "type": "rectangle",
                "width": GRADIENT["horizontal"]["width"],
                "height": GRADIENT["horizontal"]["height"]
            }
        }
    }


    # ========================================================
    # COUNTER
    # ========================================================

    layout["components"]["Counter"] = {

        "position": {
            "x": COUNTER["x"],
            "y": COUNTER["y"]
        },

        "DaysRemaining": {

            "position": {
                "x": COUNTER["days_remaining"]["x"],
                "y": COUNTER["days_remaining"]["y"]
            },

            "DaysRemainingText": {

                "font_size": (
                    COUNTER["days_remaining"]["font_size"]
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
    # JOURNEY CHILDREN
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


    plane_position = resolve_plane_position(
        event.get("progress")
    )


    # ========================================================
    # JOURNEY
    # ========================================================

    journey = {

        "position": journey_position,

        "Line": {

            "position": line_position,

            "JourneyLineShape": {

                "type": "rectangle",

                "width": JOURNEY["line"]["width"],
                "height": JOURNEY["line"]["height"]
            }
        },

        "Origin": {

            "position": origin_position,

            "OriginShape": {

                "type": "circle",

                "size": JOURNEY["origin"]["size"]
            }
        },

        "Plane": {

            "x_left": plane_position["x_left"],
            "x_right": plane_position["x_right"],
            "y": plane_position["y"],

            "PlaneText": {

                "font_size": JOURNEY["plane"]["font_size"],

                "value": "✈"
            }
        },

        "Hearts": {

            "position": hearts_position,

            "Destination": {

                "position": {
                    "x": JOURNEY["hearts"]["destination"]["x"],
                    "y": JOURNEY["hearts"]["destination"]["y"]
                },

                "DestinationText": {

                    "font_size": (
                        JOURNEY["hearts"]
                        ["destination"]
                        ["font_size"]
                    ),

                    "value": event.get(
                        "destinationDisplay",
                        ""
                    )
                }
            },

            "Arrival": {

                "position": {
                    "x": JOURNEY["hearts"]["arrival"]["x"],
                    "y": JOURNEY["hearts"]["arrival"]["y"]
                },

                "ArrivalText": {

                    "font_size": (
                        JOURNEY["hearts"]
                        ["arrival"]
                        ["font_size"]
                    ),

                    "value": event.get(
                        "arrivalDisplay",
                        ""
                    )
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

            "font_size": FOOTER["font_size"],

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

            "font_size": TEST["font_size"],

            "value": ""
        }
    }


    return layout