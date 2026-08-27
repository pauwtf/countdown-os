def build_countdown_tree():
    """
    Construye la jerarquía visual de Countdown OS.

    Las propiedades visuales conocidas del widget
    se almacenan aquí.

    Las coordenadas continúan perteneciendo
    al Layout Engine.
    """

    # ========================================================
    # ROOT
    # ========================================================

    countdown = Component(
        "Countdown",
        properties={
            "type": "container"
        }
    )


    # ========================================================
    # BACKGROUND
    # ========================================================

    background = Component(
        "Background",
        properties={
            "type": "container"
        }
    )

    countdown.add_child(
        background
    )


    # ========================================================
    # COVER
    # ========================================================

    cover = Component(
        "Cover",
        properties={
            "type": "container"
        }
    )

    cover_text = Component(
        "CoverText",
        properties={
            "type": "text",
            "value": "♥",
            "font_family": "Roboto",
            "font_size": 240,
            "color": "#FFFFFF",
            "opacity": 0.30,
            "visible": True,
            "align": "left"
        }
    )

    cover.add_child(
        cover_text
    )

    countdown.add_child(
        cover
    )


    # ========================================================
    # HEADER
    # ========================================================

    header = Component(
        "Header",
        properties={
            "type": "container"
        }
    )


    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    title = Component(
        "Title",
        properties={
            "type": "text",
            "font_family": "Cutive Mono",
            "font_size": 18,
            "color": "#FFFFFF",
            "opacity": 0.86,
            "visible": True,
            "align": "left"
        }
    )


    # --------------------------------------------------------
    # DAYS
    # --------------------------------------------------------

    days = Component(
        "Days",
        properties={
            "type": "text",
            "font_family": "Cutive Mono",
            "font_size": 15,
            "color": "#FFFFFF",
            "opacity": 1.0,
            "visible": True,
            "align": "left",
            "value": "days"
        }
    )


    header.add_child(
        title
    )

    header.add_child(
        days
    )

    countdown.add_child(
        header
    )


    # ========================================================
    # GRADIENT
    # ========================================================

    gradient = Component(
        "Gradient",
        properties={
            "type": "container"
        }
    )


    # --------------------------------------------------------
    # VERTICAL
    # --------------------------------------------------------

    vertical = Component(
        "Vertical",
        properties={
            "type": "gradient",
            "shape_type": "rectangle",
            "width": 380,
            "height": 180,
            "direction": "vertical",
            "color_start": "#FFFFFF",
            "color_end": "#000000",
            "opacity": 1.0,
            "visible": True
        }
    )


    # --------------------------------------------------------
    # HORIZONTAL
    # --------------------------------------------------------

    horizontal = Component(
        "Horizontal",
        properties={
            "type": "gradient",
            "shape_type": "rectangle",
            "width": 380,
            "height": 180,
            "direction": "horizontal",
            "color_start": "#FFFFFF",
            "color_end": "#000000",
            "opacity": 1.0,
            "visible": True
        }
    )


    gradient.add_child(
        vertical
    )

    gradient.add_child(
        horizontal
    )

    countdown.add_child(
        gradient
    )


    # ========================================================
    # COUNTER
    # ========================================================

    counter = Component(
        "Counter",
        properties={
            "type": "container"
        }
    )


    days_remaining = Component(
        "DaysRemaining",
        properties={
            "type": "text",
            "font_family": "Cutive Mono",
            "font_size": 100,
            "color": "#FFFFFF",
            "opacity": 1.0,
            "visible": True,
            "align": "left"
        }
    )


    counter.add_child(
        days_remaining
    )

    countdown.add_child(
        counter
    )


    # ========================================================
    # CONTENT
    # ========================================================

    content = Component(
        "Content",
        properties={
            "type": "container"
        }
    )


    journey = Component(
        "Journey",
        properties={
            "type": "container"
        }
    )


    content.add_child(
        journey
    )

    countdown.add_child(
        content
    )


    # ========================================================
    # JOURNEY — LINE
    # ========================================================

    line = Component(
        "Line",
        properties={
            "type": "shape",
            "shape_type": "rectangle",
            "width": 258,
            "height": 1,
            "radius": 20,
            "color": "#FFFFFF",
            "opacity": 0.60,
            "visible": True
        }
    )


    # ========================================================
    # JOURNEY — ORIGIN
    # ========================================================

    origin = Component(
        "Origin",
        properties={
            "type": "shape",
            "shape_type": "circle",
            "size": 5,
            "color": "#FFFFFF",
            "opacity": 1.0,
            "visible": True
        }
    )


    # ========================================================
    # JOURNEY — PLANE
    # ========================================================

    plane = Component(
        "Plane",
        properties={
            "type": "text",
            "font_family": "Cutive Mono",
            "font_size": 30,
            "color": "#FFFFFF",
            "opacity": 1.0,
            "visible": True,
            "align": "left",
            "value": "✈"
        }
    )


    # ========================================================
    # JOURNEY — HEARTS
    # ========================================================

    hearts = Component(
        "Hearts",
        properties={
            "type": "container"
        }
    )


    # --------------------------------------------------------
    # DESTINATION
    # --------------------------------------------------------

    destination = Component(
        "Destination",
        properties={
            "type": "text",
            "font_family": "Cutive Mono",
            "font_size": 14,
            "color": "#FFFFFF",
            "opacity": 1.0,
            "visible": True,
            "align": "left",
            "value": "♡"
        }
    )


    # --------------------------------------------------------
    # ARRIVAL
    # --------------------------------------------------------

    arrival = Component(
        "Arrival",
        properties={
            "type": "text",
            "font_family": "Cutive Mono",
            "font_size": 14,
            "color": "#FFFFFF",
            "opacity": 1.0,
            "visible": True,
            "align": "left",
            "value": "❤️"
        }
    )


    hearts.add_child(
        destination
    )

    hearts.add_child(
        arrival
    )


    # ========================================================
    # ADD JOURNEY CHILDREN
    # ========================================================

    journey.add_child(
        line
    )

    journey.add_child(
        origin
    )

    journey.add_child(
        plane
    )

    journey.add_child(
        hearts
    )


    # ========================================================
    # FOOTER
    # ========================================================

    footer = Component(
        "Footer",
        properties={
            "type": "text",
            "visible": True,
            "opacity": 1.0
        }
    )

    countdown.add_child(
        footer
    )


    # ========================================================
    # RETURN TREE
    # ========================================================

    return countdown