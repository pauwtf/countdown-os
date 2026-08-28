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

from component_property_resolver import (
    ComponentPropertyResolver
)

from kwgt_coordinate_adapter import (
    adapt_directional_position,
    adapt_dual_x_position
)


# ============================================================
# POSITION RESOLUTION
# ============================================================

def resolve_position(
    parent_position,
    local_position
):
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
# KWGT POSITION
# ============================================================

def resolve_kwgt_position(
    position
):
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
# PROPERTY RESOLVER
# ============================================================

def get_property_resolver(
    component,
    fallback=None
):
    """
    Crea un ComponentPropertyResolver para un componente.
    """

    return ComponentPropertyResolver(
        component=component,
        fallback=fallback
    )


# ============================================================
# PROGRESS
# ============================================================

def normalize_progress(
    progress
):
    """
    Normaliza progress al rango 0..1.
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
        min(
            progress,
            1.0
        )
    )


# ============================================================
# PLANE
# ============================================================

def resolve_plane_position(
    progress
):
    """
    Calcula la posición dinámica del Plane.

    La posición continúa perteneciendo
    al Layout Engine.
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
    """

    return build_countdown_tree()


# ============================================================
# BUILD LAYOUT
# ============================================================

def build_layout(
    event
):

    # ========================================================
    # COMPONENT SYSTEM
    # ========================================================

    component_tree = get_component_tree()


    # ========================================================
    # COMPONENT REFERENCES
    # ========================================================

    background_component = (
        component_tree.find("Background")
    )

    cover_component = (
        component_tree.find("Cover")
    )

    cover_text_component = (
        component_tree.find("CoverText")
    )

    title_component = (
        component_tree.find("Title")
    )

    days_component = (
        component_tree.find("Days")
    )

    vertical_component = (
        component_tree.find("Vertical")
    )

    horizontal_component = (
        component_tree.find("Horizontal")
    )

    counter_component = (
        component_tree.find("Counter")
    )

    days_remaining_component = (
        component_tree.find("DaysRemaining")
    )

    content_component = (
        component_tree.find("Content")
    )

    journey_component = (
        component_tree.find("Journey")
    )

    line_component = (
        component_tree.find("Line")
    )

    origin_component = (
        component_tree.find("Origin")
    )

    plane_component = (
        component_tree.find("Plane")
    )

    hearts_component = (
        component_tree.find("Hearts")
    )

    destination_component = (
        component_tree.find("Destination")
    )

    arrival_component = (
        component_tree.find("Arrival")
    )

    footer_component = (
        component_tree.find("Footer")
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

    background_resolver = (
        get_property_resolver(
            background_component
        )
    )

    background_shape_type = (
        background_resolver.resolve_shape_type(
            "rectangle"
        )
    )

    background_width = (
        background_resolver.resolve_width(
            BACKGROUND["width"]
        )
    )

    background_height = (
        background_resolver.resolve_height(
            BACKGROUND["height"]
        )
    )

    background_opacity = (
        background_resolver.resolve_opacity(
            1.0
        )
    )

    background_visible = (
        background_resolver.resolve_visibility(
            True
        )
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

                "width": background_width,

                "height": background_height,

                "opacity": background_opacity,

                "visible": background_visible
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

    cover_resolver = (
        get_property_resolver(
            cover_text_component
            if cover_text_component is not None
            else cover_component
        )
    )

    cover_font_family = (
        cover_resolver.resolve_font_family(
            COVER["image"]["text"].get(
                "font_family",
                "Roboto"
            )
        )
    )

    cover_font_size = (
        cover_resolver.resolve_font_size(
            COVER["image"]["text"]["font_size"]
        )
    )

    cover_color = (
        cover_resolver.resolve_color(
            COVER["image"]["text"].get(
                "color",
                "#FFFFFF"
            )
        )
    )

    cover_opacity = (
        cover_resolver.resolve_opacity(
            COVER["image"]["text"].get(
                "opacity",
                0.30
            )
        )
    )

    cover_visible = (
        cover_resolver.resolve_visibility(
            True
        )
    )

    cover_align = (
        cover_resolver.resolve_alignment(
            COVER["image"]["text"].get(
                "align",
                "left"
            )
        )
    )

    cover_value = (
        cover_resolver.resolve(
            "value",
            COVER["image"]["text"]["value"]
        )
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

                    "x": (
                        COVER["image"]
                        ["text"]["x"]
                    ),

                    "y": (
                        COVER["image"]
                        ["text"]["y"]
                    )
                },

                "font_family": cover_font_family,

                "font_size": cover_font_size,

                "color": cover_color,

                "opacity": cover_opacity,

                "visible": cover_visible,

                "align": cover_align,

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


    # --------------------------------------------------------
    # TITLE PROPERTIES
    # --------------------------------------------------------

    title_resolver = (
        get_property_resolver(
            title_component
        )
    )

    title_font_family = (
        title_resolver.resolve_font_family(
            "Cutive Mono"
        )
    )

    title_font_size = (
        title_resolver.resolve_font_size(
            HEADER["title"]["font_size"]
        )
    )

    title_color = (
        title_resolver.resolve_color(
            "#FFFFFF"
        )
    )

    title_opacity = (
        title_resolver.resolve_opacity(
            0.86
        )
    )

    title_visible = (
        title_resolver.resolve_visibility(
            True
        )
    )

    title_align = (
        title_resolver.resolve_alignment(
            "left"
        )
    )


    # --------------------------------------------------------
    # DAYS PROPERTIES
    # --------------------------------------------------------

    days_resolver = (
        get_property_resolver(
            days_component
        )
    )

    days_font_family = (
        days_resolver.resolve_font_family(
            "Cutive Mono"
        )
    )

    days_font_size = (
        days_resolver.resolve_font_size(
            HEADER["days"]["font_size"]
        )
    )

    days_color = (
        days_resolver.resolve_color(
            "#FFFFFF"
        )
    )

    days_opacity = (
        days_resolver.resolve_opacity(
            1.0
        )
    )

    days_visible = (
        days_resolver.resolve_visibility(
            True
        )
    )

    days_align = (
        days_resolver.resolve_alignment(
            "left"
        )
    )

    days_value = (
        days_resolver.resolve(
            "value",
            "days"
        )
    )


    layout["components"]["Header"] = {

        "Title": {

            "position": title_position,

            "kwgt_position": resolve_kwgt_position(
                title_position
            ),

            "TitleText": {

                "font_family": title_font_family,

                "font_size": title_font_size,

                "color": title_color,

                "opacity": title_opacity,

                "visible": title_visible,

                "align": title_align,

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

                "font_family": days_font_family,

                "font_size": days_font_size,

                "color": days_color,

                "opacity": days_opacity,

                "visible": days_visible,

                "align": days_align,

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


    # --------------------------------------------------------
    # VERTICAL
    # --------------------------------------------------------

    vertical_resolver = (
        get_property_resolver(
            vertical_component
        )
    )

    vertical_type = (
        vertical_resolver.resolve_shape_type(
            "rectangle"
        )
    )

    vertical_width = (
        vertical_resolver.resolve_width(
            GRADIENT["vertical"]["width"]
        )
    )

    vertical_height = (
        vertical_resolver.resolve_height(
            GRADIENT["vertical"]["height"]
        )
    )

    vertical_radius = (
        vertical_resolver.resolve_radius(
            GRADIENT["vertical"].get(
                "radius",
                20
            )
        )
    )

    vertical_direction = (
        vertical_resolver.resolve_direction(
            "vertical"
        )
    )

    vertical_visible = (
        vertical_resolver.resolve_visibility(
            True
        )
    )


    # --------------------------------------------------------
    # HORIZONTAL
    # --------------------------------------------------------

    horizontal_resolver = (
        get_property_resolver(
            horizontal_component
        )
    )

    horizontal_type = (
        horizontal_resolver.resolve_shape_type(
            "rectangle"
        )
    )

    horizontal_width = (
        horizontal_resolver.resolve_width(
            GRADIENT["horizontal"]["width"]
        )
    )

    horizontal_height = (
        horizontal_resolver.resolve_height(
            GRADIENT["horizontal"]["height"]
        )
    )

    horizontal_radius = (
        horizontal_resolver.resolve_radius(
            GRADIENT["horizontal"].get(
                "radius",
                20
            )
        )
    )

    horizontal_direction = (
        horizontal_resolver.resolve_direction(
            "horizontal"
        )
    )

    horizontal_visible = (
        horizontal_resolver.resolve_visibility(
            True
        )
    )


    layout["components"]["Gradient"] = {

        "Vertical": {

            "position": vertical_position,

            "kwgt_position": resolve_kwgt_position(
                vertical_position
            ),

            "GradientVerticalShape": {

                "type": vertical_type,

                "width": vertical_width,

                "height": vertical_height,

                "radius": vertical_radius,

                "direction": vertical_direction,

                "visible": vertical_visible
            }
        },

        "Horizontal": {

            "position": horizontal_position,

            "kwgt_position": resolve_kwgt_position(
                horizontal_position
            ),

            "GradientHorizontalShape": {

                "type": horizontal_type,

                "width": horizontal_width,

                "height": horizontal_height,

                "radius": horizontal_radius,

                "direction": horizontal_direction,

                "visible": horizontal_visible
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


    days_remaining_resolver = (
        get_property_resolver(
            days_remaining_component
        )
    )

    days_remaining_font_family = (
        days_remaining_resolver.resolve_font_family(
            "Cutive Mono"
        )
    )

    days_remaining_font_size = (
        days_remaining_resolver.resolve_font_size(
            COUNTER[
                "days_remaining"
            ][
                "font_size"
            ]
        )
    )

    days_remaining_color = (
        days_remaining_resolver.resolve_color(
            "#FFFFFF"
        )
    )

    days_remaining_opacity = (
        days_remaining_resolver.resolve_opacity(
            1.0
        )
    )

    days_remaining_visible = (
        days_remaining_resolver.resolve_visibility(
            True
        )
    )

    days_remaining_align = (
        days_remaining_resolver.resolve_alignment(
            "left"
        )
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

                "font_family": (
                    days_remaining_font_family
                ),

                "font_size": (
                    days_remaining_font_size
                ),

                "color": (
                    days_remaining_color
                ),

                "opacity": (
                    days_remaining_opacity
                ),

                "visible": (
                    days_remaining_visible
                ),

                "align": (
                    days_remaining_align
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
    # LINE PROPERTIES
    # ========================================================

    line_resolver = (
        get_property_resolver(
            line_component
        )
    )

    line_type = (
        line_resolver.resolve_shape_type(
            "rectangle"
        )
    )

    line_width = (
        line_resolver.resolve_width(
            JOURNEY["line"]["width"]
        )
    )

    line_height = (
        line_resolver.resolve_height(
            JOURNEY["line"]["height"]
        )
    )

    line_radius = (
        line_resolver.resolve_radius(
            20
        )
    )

    line_color = (
        line_resolver.resolve_color(
            "#FFFFFF"
        )
    )

    line_opacity = (
        line_resolver.resolve_opacity(
            0.60
        )
    )

    line_visible = (
        line_resolver.resolve_visibility(
            True
        )
    )


    # ========================================================
    # ORIGIN PROPERTIES
    # ========================================================

    origin_resolver = (
        get_property_resolver(
            origin_component
        )
    )

    origin_type = (
        origin_resolver.resolve_shape_type(
            "circle"
        )
    )

    origin_size = (
        origin_resolver.resolve_size(
            JOURNEY["origin"]["size"]
        )
    )

    origin_color = (
        origin_resolver.resolve_color(
            "#FFFFFF"
        )
    )

    origin_opacity = (
        origin_resolver.resolve_opacity(
            1.0
        )
    )

    origin_visible = (
        origin_resolver.resolve_visibility(
            True
        )
    )


    # ========================================================
    # PLANE PROPERTIES
    # ========================================================

    plane_resolver = (
        get_property_resolver(
            plane_component
        )
    )

    plane_font_family = (
        plane_resolver.resolve_font_family(
            "Cutive Mono"
        )
    )

    plane_font_size = (
        plane_resolver.resolve_font_size(
            JOURNEY["plane"]["font_size"]
        )
    )

    plane_color = (
        plane_resolver.resolve_color(
            "#FFFFFF"
        )
    )

    plane_opacity = (
        plane_resolver.resolve_opacity(
            1.0
        )
    )

    plane_visible = (
        plane_resolver.resolve_visibility(
            True
        )
    )

    plane_align = (
        plane_resolver.resolve_alignment(
            "left"
        )
    )

    plane_value = (
        plane_resolver.resolve(
            "value",
            "✈"
        )
    )


    # ========================================================
    # DESTINATION PROPERTIES
    # ========================================================

    destination_resolver = (
        get_property_resolver(
            destination_component
        )
    )

    destination_font_family = (
        destination_resolver.resolve_font_family(
            "Cutive Mono"
        )
    )

    destination_font_size = (
        destination_resolver.resolve_font_size(
            JOURNEY[
                "hearts"
            ][
                "destination"
            ][
                "font_size"
            ]
        )
    )

    destination_color = (
        destination_resolver.resolve_color(
            "#FFFFFF"
        )
    )

    destination_opacity = (
        destination_resolver.resolve_opacity(
            1.0
        )
    )

    destination_visible = (
        destination_resolver.resolve_visibility(
            True
        )
    )

    destination_align = (
        destination_resolver.resolve_alignment(
            "left"
        )
    )

    destination_value = (
        destination_resolver.resolve(
            "value",
            "♡"
        )
    )


    # ========================================================
    # ARRIVAL PROPERTIES
    # ========================================================

    arrival_resolver = (
        get_property_resolver(
            arrival_component
        )
    )

    arrival_font_family = (
        arrival_resolver.resolve_font_family(
            "Cutive Mono"
        )
    )

    arrival_font_size = (
        arrival_resolver.resolve_font_size(
            JOURNEY[
                "hearts"
            ][
                "arrival"
            ][
                "font_size"
            ]
        )
    )

    arrival_color = (
        arrival_resolver.resolve_color(
            "#FFFFFF"
        )
    )

    arrival_opacity = (
        arrival_resolver.resolve_opacity(
            1.0
        )
    )

    arrival_visible = (
        arrival_resolver.resolve_visibility(
            True
        )
    )

    arrival_align = (
        arrival_resolver.resolve_alignment(
            "left"
        )
    )

    arrival_value = (
        arrival_resolver.resolve(
            "value",
            "❤️"
        )
    )


    # ========================================================
    # FOOTER PROPERTIES
    # ========================================================

    footer_resolver = (
        get_property_resolver(
            footer_component
        )
    )

    footer_font_size = (
        footer_resolver.resolve_font_size(
            FOOTER["font_size"]
        )
    )

    footer_color = (
        footer_resolver.resolve_color(
            "#FFFFFF"
        )
    )

    footer_opacity = (
        footer_resolver.resolve_opacity(
            1.0
        )
    )

    footer_visible = (
        footer_resolver.resolve_visibility(
            True
        )
    )

    footer_align = (
        footer_resolver.resolve_alignment(
            "left"
        )
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

                "height": line_height,

                "radius": line_radius,

                "color": line_color,

                "opacity": line_opacity,

                "visible": line_visible
            }
        },

        "Origin": {

            "position": origin_position,

            "kwgt_position": resolve_kwgt_position(
                origin_position
            ),

            "OriginShape": {

                "type": origin_type,

                "size": origin_size,

                "color": origin_color,

                "opacity": origin_opacity,

                "visible": origin_visible
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

                "font_family": plane_font_family,

                "font_size": plane_font_size,

                "color": plane_color,

                "opacity": plane_opacity,

                "visible": plane_visible,

                "align": plane_align,

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

                    "font_family": (
                        destination_font_family
                    ),

                    "font_size": (
                        destination_font_size
                    ),

                    "color": (
                        destination_color
                    ),

                    "opacity": (
                        destination_opacity
                    ),

                    "visible": (
                        destination_visible
                    ),

                    "align": (
                        destination_align
                    ),

                    "value": (
                        event.get(
                            "destinationDisplay",
                            destination_value
                        )
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

                    "font_family": (
                        arrival_font_family
                    ),

                    "font_size": (
                        arrival_font_size
                    ),

                    "color": (
                        arrival_color
                    ),

                    "opacity": (
                        arrival_opacity
                    ),

                    "visible": (
                        arrival_visible
                    ),

                    "align": (
                        arrival_align
                    ),

                    "value": (
                        event.get(
                            "arrivalDisplay",
                            arrival_value
                        )
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

            "color": footer_color,

            "opacity": footer_opacity,

            "visible": footer_visible,

            "align": footer_align,

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