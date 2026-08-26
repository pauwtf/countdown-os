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

from component import (
    build_countdown_tree
)

from kwgt_coordinate_adapter import (
    adapt_directional_position,
    adapt_dual_x_position
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
# KWGT POSITION
# ============================================================

def resolve_kwgt_position(position):
    """
    Convierte una posición interna del Layout Engine
    a coordenadas direccionales de KWGT.

    Countdown OS:

        +X = derecha
        -X = izquierda
        +Y = arriba
        -Y = abajo

    KWGT:

        x_right
        x_left
        y_up
        y_down

    La posición abstracta original permanece intacta.
    """

    return adapt_directional_position(
        position["x"],
        position["y"]
    )


# ============================================================
# COMPONENT PROPERTY
# ============================================================

def get_component_property(
    component,
    key,
    fallback=None
):
    """
    Obtiene una propiedad visual desde un Component.

    Si la propiedad todavía no existe,
    devuelve el valor fallback.

    Esto permite una migración gradual desde
    layout_tokens.py hacia Component System.
    """

    if component is None:
        return fallback

    return component.get_property(
        key,
        fallback
    )


# ============================================================
# PROGRESS
# ============================================================

def normalize_progress(progress):
    """
    Normaliza progress al rango 0..1.
    """

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
    """
    Calcula la posición dinámica del Plane.

    La posición continúa dependiendo de progress.
    Las propiedades visuales del Plane pertenecen
    al Component System.
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
# COMPONENT TREE
# ============================================================

def get_component_tree():
    """
    Devuelve el árbol estructural de Countdown OS.

    El Component System define la jerarquía
    y las propiedades visuales abstractas.
    """

    return build_countdown_tree()


# ============================================================
# BUILD LAYOUT
# ============================================================

def build_layout(event):

    # ========================================================
    # COMPONENT SYSTEM
    # ========================================================

    component_tree = get_component_tree()


    # ========================================================
    # COMPONENT REFERENCES
    # ========================================================

    background_component = component_tree.find(
        "Background"
    )

    cover_component = component_tree.find(
        "Cover"
    )

    title_component = component_tree.find(
        "Title"
    )

    days_component = component_tree.find(
        "Days"
    )

    vertical_component = component_tree.find(
        "Vertical"
    )

    horizontal_component = component_tree.find(
        "Horizontal"
    )

    counter_component = component_tree.find(
        "Counter"
    )

    days_remaining_component = component_tree.find(
        "DaysRemaining"
    )

    line_component = component_tree.find(
        "Line"
    )

    origin_component = component_tree.find(
        "Origin"
    )

    plane_component = component_tree.find(
        "Plane"
    )

    destination_component = component_tree.find(
        "Destination"
    )

    arrival_component = component_tree.find(
        "Arrival"
    )

    footer_component = component_tree.find(
        "Footer"
    )


    # ========================================================
    # ROOT LAYOUT
    # ========================================================

    layout = {

        "version": "1.2",

        "system": (
            "Countdown OS Layout System"
        ),

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

    background_position = {

        "x": BACKGROUND["x"],

        "y": BACKGROUND["y"]
    }

    background_type = get_component_property(
        background_component,
        "type",
        "container"
    )

    background_shape_type = get_component_property(
        background_component,
        "shape_type",
        "rectangle"
    )

    layout["components"]["Background"] = {

        "position": background_position,

        "kwgt_position": resolve_kwgt_position(
            background_position
        ),

        "Background_shape": {

            "position": {

                "x": 0,

                "y": 0
            },

            "BackgroundShape": {

                "type": background_shape_type,

                "width": BACKGROUND["width"],

                "height": BACKGROUND["height"]
            }
        }
    }


    # ========================================================
    # COVER
    # ========================================================

    cover_position = {

        "x": COVER["x"],

        "y": COVER["y"]
    }

    cover_value = get_component_property(
        cover_component,
        "value",
        COVER["image"]["text"]["value"]
    )

    cover_font_size = get_component_property(
        cover_component,
        "font_size",
        COVER["image"]["text"]["font_size"]
    )

    layout["components"]["Cover"] = {

        "position": cover_position,

        "kwgt_position": resolve_kwgt_position(
            cover_position
        ),

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

                "font_size": cover_font_size,

                "value": cover_value
            }
        }
    }


    # ========================================================
    # HEADER
    # ========================================================

    title_position = {

        "x": HEADER["title"]["x"],

        "y": HEADER["title"]["y"]
    }

    days_position = {

        "x": HEADER["days"]["x"],

        "y": HEADER["days"]["y"]
    }

    title_font_size = get_component_property(
        title_component,
        "font_size",
        HEADER["title"]["font_size"]
    )

    days_font_size = get_component_property(
        days_component,
        "font_size",
        HEADER["days"]["font_size"]
    )

    days_value = get_component_property(
        days_component,
        "value",
        "days"
    )

    layout["components"]["Header"] = {

        "Title": {

            "position": title_position,

            "kwgt_position": resolve_kwgt_position(
                title_position
            ),

            "TitleText": {

                "font_size": title_font_size,

                "value": event.get(
                    "titleDisplay",
                    ""
                )
            }
        },

        "Days": {

            "position": days_position,

            "kwgt_position": resolve_kwgt_position(
                days_position
            ),

            "DaysText": {

                "font_size": days_font_size,

                "value": days_value
            }
        }
    }


    # ========================================================
    # GRADIENT
    # ========================================================

    vertical_position = {

        "x": GRADIENT["vertical"]["x"],

        "y": GRADIENT["vertical"]["y"]
    }

    horizontal_position = {

        "x": GRADIENT["horizontal"]["x"],

        "y": GRADIENT["horizontal"]["y"]
    }

    vertical_type = get_component_property(
        vertical_component,
        "shape_type",
        "rectangle"
    )

    horizontal_type = get_component_property(
        horizontal_component,
        "shape_type",
        "rectangle"
    )

    layout["components"]["Gradient"] = {

        "Vertical": {

            "position": vertical_position,

            "kwgt_position": resolve_kwgt_position(
                vertical_position
            ),

            "GradientVerticalShape": {

                "type": vertical_type,

                "width": (
                    GRADIENT["vertical"]["width"]
                ),

                "height": (
                    GRADIENT["vertical"]["height"]
                )
            }
        },

        "Horizontal": {

            "position": horizontal_position,

            "kwgt_position": resolve_kwgt_position(
                horizontal_position
            ),

            "GradientHorizontalShape": {

                "type": horizontal_type,

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

    days_remaining_position = {

        "x": COUNTER["days_remaining"]["x"],

        "y": COUNTER["days_remaining"]["y"]
    }

    days_remaining_font_size = get_component_property(
        days_remaining_component,
        "font_size",
        COUNTER[
            "days_remaining"
        ][
            "font_size"
        ]
    )

    layout["components"]["Counter"] = {

        "position": counter_position,

        "kwgt_position": resolve_kwgt_position(
            counter_position
        ),

        "DaysRemaining": {

            "position": days_remaining_position,

            "kwgt_position": resolve_kwgt_position(
                days_remaining_position
            ),

            "DaysRemainingText": {

                "font_size": days_remaining_font_size,

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
    # JOURNEY PROPERTIES
    # ========================================================

    line_type = get_component_property(
        line_component,
        "shape_type",
        "rectangle"
    )

    line_width = get_component_property(
        line_component,
        "width",
        JOURNEY["line"]["width"]
    )

    line_height = get_component_property(
        line_component,
        "height",
        JOURNEY["line"]["height"]
    )

    origin_type = get_component_property(
        origin_component,
        "shape_type",
        "circle"
    )

    origin_size = get_component_property(
        origin_component,
        "size",
        JOURNEY["origin"]["size"]
    )

    plane_font_size = get_component_property(
        plane_component,
        "font_size",
        JOURNEY["plane"]["font_size"]
    )

    plane_value = get_component_property(
        plane_component,
        "value",
        "✈"
    )

    destination_font_size = get_component_property(
        destination_component,
        "font_size",
        JOURNEY[
            "hearts"
        ][
            "destination"
        ][
            "font_size"
        ]
    )

    arrival_font_size = get_component_property(
        arrival_component,
        "font_size",
        JOURNEY[
            "hearts"
        ][
            "arrival"
        ][
            "font_size"
        ]
    )

    footer_font_size = get_component_property(
        footer_component,
        "font_size",
        FOOTER["font_size"]
    )


    # ========================================================
    # JOURNEY
    # ========================================================

    journey = {

        "position": journey_position,

        "kwgt_position": resolve_kwgt_position(
            journey_position
        ),

        "Line": {

            "position": line_position,

            "kwgt_position": resolve_kwgt_position(
                line_position
            ),

            "JourneyLineShape": {

                "type": line_type,

                "width": line_width,

                "height": line_height
            }
        },

        "Origin": {

            "position": origin_position,

            "kwgt_position": resolve_kwgt_position(
                origin_position
            ),

            "OriginShape": {

                "type": origin_type,

                "size": origin_size
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

            "kwgt_position": (
                adapt_dual_x_position(
                    plane_position["x_left"],
                    plane_position["x_right"],
                    plane_position["y"]
                )
            ),

            "PlaneText": {

                "font_size": plane_font_size,

                "value": plane_value
            }
        },

        "Hearts": {

            "position": hearts_position,

            "kwgt_position": resolve_kwgt_position(
                hearts_position
            ),

            "Destination": {

                "position": {

                    "x": (
                        JOURNEY[
                            "hearts"
                        ][
                            "destination"
                        ][
                            "x"
                        ]
                    ),

                    "y": (
                        JOURNEY[
                            "hearts"
                        ][
                            "destination"
                        ][
                            "y"
                        ]
                    )
                },

                "DestinationText": {

                    "font_size": destination_font_size,

                    "value": event.get(
                        "destinationDisplay",
                        ""
                    )
                }
            },

            "Arrival": {

                "position": {

                    "x": (
                        JOURNEY[
                            "hearts"
                        ][
                            "arrival"
                        ][
                            "x"
                        ]
                    ),

                    "y": (
                        JOURNEY[
                            "hearts"
                        ][
                            "arrival"
                        ][
                            "y"
                        ]
                    )
                },

                "ArrivalText": {

                    "font_size": arrival_font_size,

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

        "kwgt_position": resolve_kwgt_position(
            content_position
        ),

        "journey": journey
    }


    # ========================================================
    # FOOTER
    # ========================================================

    footer_position = {

        "x": FOOTER["x"],

        "y": FOOTER["y"]
    }

    layout["components"]["Footer"] = {

        "position": footer_position,

        "kwgt_position": resolve_kwgt_position(
            footer_position
        ),

        "FooterText": {

            "font_size": footer_font_size,

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


    # ========================================================
    # COMPONENT TREE VALIDATION
    # ========================================================

    expected_components = [

        "Background",
        "Cover",
        "Header",
        "Gradient",
        "Counter",
        "Content",
        "Footer"

    ]

    for component_name in expected_components:

        if component_tree.find(
            component_name
        ) is None:

            raise ValueError(
                "Component System is missing "
                f"component: {component_name}"
            )


    return layout