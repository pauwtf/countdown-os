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

def resolve_position(
    parent_position,
    local_position
):
    """
    Parent-relative positioning.

    Absolute position =
    Parent position + Local position
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

    progress = normalize_progress(
        progress
    )

    plane = JOURNEY["plane"]

    return {
        "x_left": (
            plane["travel"] *
            progress
        ),

        "x_right": plane["x_right"],

        "y": plane["y"]
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

    layout["components"]["background"] = {
        "position": {
            "x": BACKGROUND["x"],
            "y": BACKGROUND["y"]
        },

        "width": BACKGROUND["width"],
        "height": BACKGROUND["height"]
    }

    # ========================================================
    # COVER
    # ========================================================

    cover_position = {
        "x": COVER["x"],
        "y": COVER["y"]
    }

    layout["components"]["cover"] = {

        "position": cover_position,

        "image": {

            "position": {
                "x": COVER["image"]["x"],
                "y": COVER["image"]["y"]
            },

            "text": {
                "position": {
                    "x": COVER["image"]["text"]["x"],
                    "y": COVER["image"]["text"]["y"]
                },

                "font_size": (
                    COVER["image"]["text"]
                    ["font_size"]
                ),

                "text": COVER["image"]["text"]
                ["value"]
            }
        }
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

            "text": {
                "font_size": (
                    HEADER["title"]["font_size"]
                ),

                "value": event.get(
                    "titleDisplay",
                    ""
                )
            }
        },

        "days": {

            "position": {
                "x": HEADER["days"]["x"],
                "y": HEADER["days"]["y"]
            },

            "text": {
                "font_size": (
                    HEADER["days"]["font_size"]
                ),

                "value": "days"
            }
        }
    }

    # ========================================================
    # GRADIENT
    # ========================================================

    layout["components"]["gradient"] = {

        "vertical": {
            "position": {
                "x": GRADIENT["vertical"]["x"],
                "y": GRADIENT["vertical"]["y"]
            }
        },

        "horizontal": {
            "position": {
                "x": GRADIENT["horizontal"]["x"],
                "y": GRADIENT["horizontal"]["y"]
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

    layout["components"]["counter"] = {

        "position": counter_position,

        "days_remaining": {

            "position": {
                "x": COUNTER["days_remaining"]["x"],
                "y": COUNTER["days_remaining"]["y"]
            },

            "text": {

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
    # JOURNEY COMPONENT
    # ========================================================

    journey = {

        "position": journey_position,

        "line": {

            "position": line_position,

            "shape": {

                "width": (
                    JOURNEY["line"]["width"]
                ),

                "height": (
                    JOURNEY["line"]["height"]
                )
            }
        },

        "origin": {

            "position": origin_position,

            "shape": {

                "size": (
                    JOURNEY["origin"]["size"]
                )
            }
        },

        "plane": {

            **resolve_plane_position(
                event.get("progress")
            ),

            "text": {
                "value": "✈",
                "font_size": (
                    JOURNEY["plane"]["font_size"]
                )
            }
        },

        "hearts": {

            "position": hearts_position,

            "destination": {

                "position": {
                    "x": 0,
                    "y": 0
                },

                "text": {
                    "font_size": (
                        JOURNEY["hearts"]
                        ["destination"]
                        ["font_size"]
                    ),

                    "value": ""
                }
            },

            "arrival": {

                "position": {
                    "x": 0,
                    "y": 0
                },

                "text": {
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

    layout["components"]["content"] = {

        "position": content_position,

        "journey": journey
    }

    # ========================================================
    # FOOTER
    # ========================================================

    layout["components"]["footer"] = {

        "position": {
            "x": FOOTER["x"],
            "y": FOOTER["y"]
        },

        "text": {

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
        "position": {
            "x": TEST["x"],
            "y": TEST["y"]
        }
    }

    return layout